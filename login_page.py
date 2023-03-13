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


        layout = [
            [col_logins],
            [[sg.Button("Learn more about us"), sg.Button("Tutorial")]],
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
            elif event == "admin_login":
                LogInForm(login_type="admin", parent=window).run()
            elif event == "Learn more about us":
                pass
            # window["output1"].update(values["input1"])

        window.close()


if __name__ == "__main__":
    LogInPage().run()
