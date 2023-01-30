import PySimpleGUI as sg


layout = [
    [sg.Text('Meu texto', size=(20, 1), key='-TEXT-')],
    [
        sg.CB('Negrito', key='-BOLD-', change_submits=True),
        sg.CB('Itálico', key='-ITALIC-', change_submits=True),
        sg.CB('Sublinhado', key='-UNDERLINE-', change_submits=True)
    ],
    [
        sg.Slider((6, 50), default_value=12, size=(14, 20), orientation='h',
                  key='-SLIDER-', change_submits=True),
        sg.Text('Tamanho da fonte')
    ],
    [
        sg.Text('Detalhe da fonte: '),
        sg.Text('', size=(25, 1), key='-FONT-')
    ],
    [sg.Button('Sair')]
]

window = sg.Window('Detalhes da fonte', layout)
elemento_texto = window['-TEXT-']

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Sair'):
        break

    font = 'Arial '
    font += str(int(values['-SLIDER-']))
    if values['-BOLD-']:
        font += ' bold'
    if values['-ITALIC-']:
        font += ' italic'
    if values['-UNDERLINE-']:
        font += ' underline'       

        elemento_texto.update(font=font)
        window['-FONT-'].update('"'+font+'"')

    window.close()         
