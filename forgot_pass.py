import PySimpleGUI as sg


class ForgotPass:
    def __init__(self) -> None:
        pass

    def _layout(self):
        layout = [
            [sg.Text("Enter your email address")],
            [sg.Input(key="email")],
            [sg.Button("Send email")],
        ]
        return layout

    def run(self):
        window = sg.Window("Forgot password", self._layout(), right_click_menu_tearoff=True, grab_anywhere=True,
                           resizable=True, margins=(0, 0), use_custom_titlebar=True, finalize=True, keep_on_top=True)
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED or event == "Quit":
                break
            elif event == "Send email":
                pass

        window.close()


if __name__ == "__main__":
    ForgotPass().run()