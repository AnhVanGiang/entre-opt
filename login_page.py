import PySimpleGUI as sg


class LogInPage:
    def __init__(self) -> None:
        pass 

    def layout(self):
        layout = [
            [sg.Text("Login page", size=(10, 3), expand_x=True, expand_y=True)],
            [sg.Button("Teacher login", size=(10, 2), expand_x=True, expand_y=True)],
            [sg.Button("Admin login", size=(10, 2), expand_x=True, expand_y=True)],
        ]

        return layout

    def run(self):
        window = sg.Window("ScheDU", self.layout())
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED or event == "Quit":
                break 
            elif event == "Teacher login":
                pass
            elif event == "Admin login":
                pass
            # window["output1"].update(values["input1"])
        
        window.close()


LogInPage().run()