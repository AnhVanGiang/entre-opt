import PySimpleGUI as sg
import webbrowser

class Utils:
    def __init__(self) -> None:
        pass

    @staticmethod
    def create_frame_checkboxes(items=[1,2,3,4], size=(400, 300)):
        return sg.Frame('Subjects', layout=[[
                sg.Column([
                    [sg.Checkbox(f'{subject}', key=f'{subject}')] for subject in items
                ], scrollable=True, vertical_scroll_only=True, size=size)]])

    @staticmethod
    def open_ltg():
        webbrowser.open_new('https://www.youtube.com/watch?v=0KJZtcbZvgM&list=PPSV')

    @staticmethod
    def make_dummy_table(size=10):
        return sg.Table(values=[[f'Row {j}'] + ['' for _ in range(size)] for j in range(size)], headings=[''] + [f'Column {i}' for i in range(1, size)], num_rows=size, key='table')
    
    @staticmethod
    def check_extension(filename, ext = ['.xlsx', '.csv']):
        return any([filename.endswith(e) for e in ext])
    
    @staticmethod
    def make_table(df):
        return sg.Table(values=df.values.tolist(), headings=df.columns.tolist(), num_rows=df.shape[0], key='table')
    
    @staticmethod
    def dict_to_str(dic):
        s = ""
        mc = max([len(v) for v in dic.values()])
        for k, v in dic.items():
            s += f"{k}: {v} \n"
            s += "-" * (10*mc + 1) + "\n"
        return s, mc 
