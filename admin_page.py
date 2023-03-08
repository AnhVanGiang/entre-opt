import PySimpleGUI as sg
from utils import Utils


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
                [sg.Canvas(background_color='white', size=(
                    600, 400), key="add_teacher_canvas")],
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
            [sg.Text("Number of lessons: "), sg.Text("0", key="n_lessons")],
            [sg.Button("Export as", key="export_as")],
            [sg.Button("Simulate", key="simulate")],
        ]
        return layout

    def _layout(self):
        layout = [[sg.Menu([['File', ['Exit']], ['Edit', ['Edit Me', ]]],  k='-CUST MENUBAR-',p=0)],
                  [sg.TabGroup([[sg.Tab('Data', self._data_layout()),
                                 sg.Tab("Advanced", self._advanced_layout()),
                                 sg.Tab("Statistics", self._statistics_layout()),
                                 sg.Tab("Formation", self._formation_layout())]]), ],
                  ]

        return layout

    def _formation_layout(self):
        layout = [
            [sg.Frame("Math formulation", layout=[
                [Utils.make_dummy_table()],
            ])]]

        return layout


    def run(self):
        window = sg.Window('SchEDU', self._layout(), right_click_menu_tearoff=True, grab_anywhere=True,
                           resizable=True, margins=(0, 0), use_custom_titlebar=True, finalize=True, keep_on_top=False)
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED or event == "Quit":
                break
            # window["output1"].update(values["input1"])

        window.close()


if __name__ == "__main__":
    AdminPage().run()
