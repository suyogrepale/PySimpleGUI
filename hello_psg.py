import PySimpleGUI as sg    

layout=[
    [sg.Text("Hello from PySimpleGUI")],
    [sg.Button("OK")]
]

window =sg.Window("Demo",layout)

while True:
    event,values=window.read()
    #End program if user closes window Or
    #presses Ok button
    if event=="OK" or event == sg.WIN_CLOSED:
        break

window.close()