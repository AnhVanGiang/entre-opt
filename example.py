import PySimpleGUI as sg

left_frame_layout = [[sg.Text('Left Frame')]]
right_frame_layout = [[sg.Text('Right Frame')]]

layout = [
    [sg.Frame('Left Frame', left_frame_layout), sg.Frame('Right Frame', right_frame_layout)]
]

window = sg.Window('Window with Left Frame', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()