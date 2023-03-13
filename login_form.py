import PySimpleGUI as sg
from forgot_pass import ForgotPass
from utils import Utils
from teacher_page import TeacherPage
from admin_page import AdminPage

class LogInForm:
    def __init__(self, login_type, parent) -> None:
        self.login_type = login_type
        self.parent = parent

    def _check_password(self, email, password):
        if email == "joe" and password == "mama":
            return True
        return False

    def _layout(self):
        layout = [
            [sg.Text("Enter your email address")],
            [sg.Input(key="email")],
            [sg.Text("Enter your password")],
            [sg.Input(key="password", password_char="*")],
            [sg.Button("Log in", key="log_in")],
            [sg.Button("Forgot password", key="forgot_pass")]
        ]
        return layout
    
    def run(self):
        window = sg.Window(f"{self.login_type} login", self._layout(), right_click_menu_tearoff=True, grab_anywhere=True,
                           resizable=True, margins=(0, 0), use_custom_titlebar=True, finalize=True, keep_on_top=True)
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED or event == "Quit":
                break
            elif event == "log_in":
                # print(values["email"], values["password"])
                if self._check_password(values["email"], values["password"]):
                    # print("Logged in")
                    # sg.PopupNoWait("You are logged in", title="Success", keep_on_top=True)
                    if self.login_type == "teacher":
                        window.close()
                        self.parent.close()
                        TeacherPage().run()
                    elif self.login_type == "admin":
                        window.close()
                        self.parent.close()
                        AdminPage().run()
                else:
                    sg.PopupNoWait("WRONG !!!!", title="IDIOT", keep_on_top=True)
                    Utils.open_ltg()
            elif event == "forgot_pass":
                window.hide()
                ForgotPass().run()
                window.un_hide()

        window.close()


if __name__ == "__main__":
    LogInForm().run()