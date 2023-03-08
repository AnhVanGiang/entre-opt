import PySimpleGUI as sg
from login_form import LogInForm


class LogInPage:
    def __init__(self) -> None:
        pass

    def _layout(self):
        col_logins = sg.Column([
            [sg.Button("Teacher login", size=(10, 2), key="teacher_login")],
            [sg.Button("Admin login", size=(10, 2), key="admin_login")],
        ], vertical_alignment="center", justification="center")

        col_learn_more = sg.Column([
            [sg.Button("Learn more about us"), sg.Button("Forgot password", key="forgot_pass")],
        ], vertical_alignment="left", justification="left")

        col_tutorial = sg.Column([
            [sg.Button("Tutorial", size=(6, 2))],
        ], vertical_alignment="center", justification="right")

        layout = [
            [col_tutorial],
            [col_logins],
            [col_learn_more],
        ]

        return layout

    def run(self):
        window = sg.Window('SchEDU', self._layout(), right_click_menu_tearoff=True, grab_anywhere=True,
                           resizable=True, margins=(0, 0), use_custom_titlebar=True, finalize=True, keep_on_top=False)
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED or event == "Quit":
                break
            elif event == "teacher_login":
                LogInForm(login_type="teacher", parent=window).run()
            elif event == "Admin login":
                pass
            elif event == "Learn more about us":
                pass
            # window["output1"].update(values["input1"])

        window.close()


if __name__ == "__main__":
    LogInPage().run()
