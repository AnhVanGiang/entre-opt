import PySimpleGUI as sg
from utils import Utils
import time 
from solver import Solver


class AdminPage:
    def __init__(self, size=(400, 300)) -> None:
        self.size = size

    def _data_layout(self, n_teachers=4):
        layout = [
            [sg.Text("Select a teacher to see the data")],
            [sg.Listbox(values=[f"Teacher {i}" for i in range(n_teachers)], size=(
                20, 10), key="teacher_list", enable_events=True)],
            [sg.Button("View data", key="view_data")]
        ]

        return layout

    def _advanced_layout(self):
        layout = [
            [sg.Frame("Math formulation", layout=[
                [sg.Image(filename="form.png", size= (480, 400), key="formulation")],
            ]),
                sg.Frame("Stuff", layout=[
                    [sg.Text("Choose an algorithm")],
                    [sg.Combo(["Genetic algorithm", "Simulated annealing"],
                              key="algorithm")],
                    [sg.Button("Run", key="run_algo")]]), ],
            [sg.Button("Add constraint", key="add_constraint")]]
        return layout

    def _statistics_layout(self):
        layout = [
            [sg.Text("Statistics")],
            [sg.Text("Number of teachers: "), sg.Text("0", key="n_teachers")],
            [sg.Text("Number of subjects: "), sg.Text("0", key="n_subjects")],
            [sg.Text("Number of classes: "), sg.Text("0", key="n_classes")],
            [sg.Text("Number of students: "), sg.Text("0", key="n_students")],
            [sg.Text("Number of constraints: "),
             sg.Text("0", key="n_constraints")],
            [sg.Button("Export as", key="export_as")],
            [sg.Button("Simulate", key="simulate")],
        ]
        return layout

    def _layout(self):
        layout = [[sg.Menu([['File', ["Add file", 'Exit']], ['Edit', ['Edit Me', ]]],  k='-CUST MENUBAR-',p=0)],
                  [sg.TabGroup([[sg.Tab('Data', self._data_layout()),
                                 sg.Tab("Advanced", self._advanced_layout()),
                                 sg.Tab("Statistics", self._statistics_layout()),
                                 sg.Tab("Formation", self._formation_layout())]]), ],
                  ]

        return layout

    def _formation_layout(self):
        layout = [
            [sg.Frame("Teacher allocation", layout=[
                [sg.Multiline(size=(80, 20), key="formation_text")],
            ])],
            [sg.Input(key="doc"), sg.FileBrowse()],
            [sg.Button("solve", key="solve_model")],
            [sg.Text("Model solve status: "), sg.Text("0", key="solve_status")],
            [sg.Text('Solving time: '), sg.Text("0", key="solve_time")],]

        return layout


    def run(self):
        window = sg.Window('SchEDU', self._layout(), right_click_menu_tearoff=True, grab_anywhere=True,
                           resizable=True, margins=(0, 0), use_custom_titlebar=True, finalize=True, keep_on_top=False)
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED or event == "Quit":
                break
            elif event == "solve_model":
                doc = values["doc"]
                start_t = time.time()
                res = Solver().solve(doc)
                end_t = time.time()
                window["n_teachers"].update(len(res["teachers"]))
                window["n_subjects"].update(len(res["classes"]))
                window["n_classes"].update(len(res["classes_levels"]))
                window["n_constraints"].update(len(res["model"].constraints))
                window["solve_status"].update(res["status"])
                window["solve_time"].update(round(end_t - start_t, 3))
                s, mc = Utils().dict_to_str(res["dic"])
                window["formation_text"].update(value=s,  append=True)
                # window["form_canvas"].draw_image(filename='form.png', location=(0, 0))

            # window["output1"].update(values["input1"])

        window.close()


if __name__ == "__main__":
    AdminPage().run()
