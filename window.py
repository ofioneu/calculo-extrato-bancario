import PySimpleGUI as sg
import pandas as pd

BAR_WIDTH = 50      # width of each bar
BAR_SPACING = 100    # space between each bar
EDGE_OFFSET = 20     # offset from the left edge for first bar
GRAPH_SIZE= DATA_SIZE = (300,300)       # size in pixels
bcols = ['green', 'red']

def calcular(path):
    df= pd.read_csv(path, encoding='latin-1', index_col=False)

    c = 0
    d =0

    for i in df['Valor']:
        if i > 0:
            c+=i
        
        else:
            d+=i*-1
    return([round(c,2),round(d,2)])

sg.theme('Light brown 1')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('ENTRE COM O CAMINHO CSV')], 
            [sg.Input(visible=False, enable_events=True, key='-IN-'), sg.FilesBrowse()],
            [sg.Graph(GRAPH_SIZE, (0,0), DATA_SIZE, k='-GRAPH-')],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)
graph = window['-GRAPH-']       # type: sg.Graph
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    
    arq = values['-IN-']
    
    if event == 'Ok':
        valores=calcular(arq)
        graph.erase()
        for i in range(2):
            
            graph.draw_rectangle(top_left=(i*BAR_SPACING + EDGE_OFFSET, valores[i]/50),
                             bottom_right=(i*BAR_SPACING + EDGE_OFFSET + BAR_WIDTH, 0),
                             fill_color=bcols[i])
                             # fill_color=sg.theme_button_color()[1])
            print(valores[i])

            graph.draw_text(text=str(valores[i]), location=(i*BAR_SPACING+EDGE_OFFSET+25, valores[i]/46), font='_ 14')


window.close()