import pandas as pd
import numpy as np
import pulp


class Solver:
    def __init__(self) -> None:
        pass

    def get_dat(self, f):
        df1 = pd.read_excel(f, sheet_name='hours').fillna(0)
        df2 = pd.read_excel(f, sheet_name='Data')

        df1.set_index('Unnamed: 0', inplace=True)

        classes_hours = df1.values.reshape(1, -1)

        df2 = df2.iloc[1:]
        df2 = df2.loc[:, ~df2.columns.str.contains('^Unnamed')]

        df2 = df2.dropna(how='all')

        contract_hours_per_teacher = df2["Contract hours per week"].values

        teachers = df2["Teacher"].values

        classes = df1.index.values
        levels = df1.columns.values

        df2["allowed"] = df2[["c1", "c2", "c3", "c4"]].apply(
            lambda x: [i for i in x if i is not np.NaN and i in classes], axis=1)

        allowed = np.zeros((len(teachers), classes_hours.shape[1]))

        for i in range(len(teachers)):
            for j in range(len(df2.iloc[i]["allowed"])):
                # print(df2.iloc[i]["allowed"][j])
                start_ind = np.where(classes == df2.iloc[i]["allowed"][j])[
                                     0][0] * len(levels)
                allowed[i][start_ind: start_ind + len(levels)] = 1

        return allowed, contract_hours_per_teacher, classes_hours, teachers, classes, levels

    def solve(self, f):
        allowed, contract_hours_per_teacher, classes_hours, teachers, classes, levels = self.get_dat(
            f)
        prob = pulp.LpProblem("Teacher_Allocation", pulp.LpMinimize)
        classes_levels = [f"{c}_{l}" for c in classes for l in levels]

        allowed = pulp.makeDict([teachers, classes_levels], allowed, 0)

        teacher_alloc = pulp.LpVariable.dicts("teacher_alloc",
                                 (teachers,
                                 classes_levels),
                                 cat="Binary")

        y = pulp.LpVariable("y", 0)
        z = pulp.LpVariable.dicts("z",
                     classes_levels,
                     cat="Binary")

        hours_class = pulp.makeDict(
            [classes_levels], classes_hours.flatten(), 0)

        M2 = len(teachers) * len(classes_levels) + 1
        M1 = M2

        T = classes_hours.sum()

        contract_hours = pulp.makeDict(
            [teachers], contract_hours_per_teacher, 0)

        prob += (y, "Objective function")

        for t in teachers:
            prob += (pulp.lpSum([teacher_alloc[t][c] * hours_class[c] -
                     contract_hours[t] for c in classes_levels]) <= y)

        prob += (pulp.lpSum([teacher_alloc[t][c] * hours_class[c]
                 for c in classes_levels for t in teachers]) == T)

        for c in classes_levels:
            prob += (pulp.lpSum([teacher_alloc[t][c] for t in teachers]) <= 1)

            prob += (1 - M1 * z[c] <= hours_class[c])

            prob += (
                pulp.lpSum([teacher_alloc[t][c]
                           for t in teachers]) <= M2 * (1 - z[c])
            )

        for t in teachers:
            for c in classes_levels:
                prob += (teacher_alloc[t][c] <= allowed[t][c])

        prob.solve()

        res_dict = {}
        for t in teachers:
            res_dict[t] = []
            for c in classes_levels:
                if teacher_alloc[t][c].value() == 1:
                    res_dict[t].append(c)
        

        return {
            "status": pulp.LpStatus[prob.status],
            "model": prob,
            "teacher_alloc": teacher_alloc,
            "hours_class": hours_class,
            "classes_levels": classes_levels,
            "classes": classes,
            "levels": levels,
            "teachers": teachers,
            "contract_hours": contract_hours,
            "classes_hours": classes_hours,
            "allowed": allowed,
            "dic": res_dict,
        }