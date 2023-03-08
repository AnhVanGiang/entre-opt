import PySimpleGUI as sg
from utils import Utils


class TeacherPage:
    def __init__(self, subjects=["a", "b", "c", "d"]) -> None:
        self.subjects = subjects
        self.qual_cbs = ["cb_bachelor", "cb_master", "cb_phd"]
        self.days = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday"
        ]
        self.allowed_files = [
            ".pdf",
            ".doc",
        ]

    def _working_factor_layout(self):
        layout = [
            [sg.Text("What is your FTE ?")],
            [sg.Input(key="fte")],
            [sg.Button("Submit")],
        ]

        return layout
    
    def _pref(self):
        layout = [
            [sg.Text("Preferred free days new school year ?")],
            [Utils.create_frame_checkboxes(self.days)],
            [sg.Button("Submit", key="submit_pref")],
        ]

        return layout
    
    def _qualifications_layout(self):
        layout = [
            [sg.Text("What is your highest qualification ?")],
            [sg.Checkbox("Bachelor", key="cb_bachelor", enable_events=True),
             sg.Checkbox("Master", key="cb_master", enable_events=True),
             sg.Checkbox("PhD", key="cb_phd", enable_events=True),],
            [sg.Text("Which subjects are you allowed to teach ?")],
            [Utils.create_frame_checkboxes(self.subjects)],
            [sg.Button("Submit", key="submit_qual")],
        ]

        return layout

    def _subjects_layout(self):
        layout = [
            [sg.Text("Choose the subjects you teach ?")],
            [Utils.create_frame_checkboxes(self.subjects)],
            [sg.Button("Submit", key="submit_subjects")],
            ]

        return layout
    
    def _doc(self):
        layout = [
            [sg.Text("Upload your documents here")],
            [sg.Input(key="doc"), sg.FileBrowse()],
            [sg.Button("Submit", key="submit_doc")],
        ]

        return layout

    def _layout(self):
        layout = [
            [sg.TabGroup([[sg.Tab('Working factor', self._working_factor_layout()),
                           sg.Tab('Subjects', self._subjects_layout()),
                           sg.Tab('Qualifications', self._qualifications_layout()),
                           sg.Tab('Preferred free days', self._pref()),
                           sg.Tab('Documents', self._doc())]]),],
        ]
        return layout

    def run(self):
        window = sg.Window("Teacher page", self._layout(), right_click_menu_tearoff=True, grab_anywhere=True,
                           resizable=True, margins=(0, 0), use_custom_titlebar=True, finalize=True, keep_on_top=True)
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED or event == "Quit":
                break
            elif event == "Submit":
                # print(values["fte"])
                pass 
            elif event == "submit_subjects":
                pass 
            elif event in self.qual_cbs:
                # print(event)
                for cb in self.qual_cbs:
                    if cb != event:
                        window[cb].update(value=False)
            elif event == "submit_qual":
                pass
            elif event == "submit_pref":
                pass
            elif event == "submit_doc":
                if not (values["doc"].endswith(tuple(self.allowed_files))):
                    sg.PopupNoWait("Please select a pdf or docx file", title="Error", keep_on_top=True)
                    Utils.open_ltg()
                pass 

        window.close()


if __name__ == "__main__":
    TeacherPage().run()
