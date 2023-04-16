import PySimpleGUI as sg

notas = []
pesos = []

def media_ponderada(notas, pesos):
    mult = [x * y for x, y in zip(notas, pesos)]
    media = sum(mult) / sum(pesos)
    return f'{media:.2f}'


layout = [
    [sg.Text('Digite suas notas:')],
    [sg.InputText(key='nota1', size=(5, 6)), sg.Text('1º nota'), sg.InputText(key='nota2', size=(5, 6)), sg.Text('2º nota'), sg.InputText(key='nota3', size=(5, 6)), sg.Text('3º nota'), sg.InputText(key='nota4', size=(5, 6)), sg.Text('4º nota'), sg.Button('NOTA')],
    [sg.Text('Digite seus pesos:')],
    [sg.InputText(key='peso1', size=(5, 6)), sg.Text('1º peso'), sg.InputText(key='peso2', size=(5, 6)), sg.Text('2º peso'), sg.InputText(key='peso3', size=(5, 6)), sg.Text('3º peso'), sg.InputText(key='peso4', size=(5, 6)), sg.Text('4º peso'), sg.Button('PESO')],
    [sg.Button('CALCULAR'), sg.Button('CANCELAR')],
    [sg.Text('', key='media')]
    ]
janela = sg.Window('Média Ponderada', layout)

while True:
    event, vals = janela.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'CANCELAR':
        notas.clear()
        pesos.clear()
        print(notas)
        print(pesos)
    if event == 'NOTA':
        pegar_nota1 = vals['nota1']
        notas.append(float(pegar_nota1))
        pegar_nota2 = vals['nota2']
        notas.append(float(pegar_nota2))
        pegar_nota3 = vals['nota3']
        if pegar_nota3 == '':
            pass
        else:
            notas.append(float(pegar_nota3))
        pegar_nota4 = vals['nota4']
        if pegar_nota4 == '':
            pass
        else:
            notas.append(float(pegar_nota4))
        print(notas)
    if event == 'PESO':
        pegar_peso1 = vals['peso1']
        pesos.append(float(pegar_peso1))
        pegar_peso2 = vals['peso2']
        pesos.append(float(pegar_peso2))
        pegar_peso3 = vals['peso3']
        if pegar_peso3 == '':
            pass
        else:
            pesos.append(float(pegar_peso3))
        pegar_peso4 = vals['peso4']
        if pegar_peso4 == '':
            pass
        else:
            pesos.append(float(pegar_peso4))
        print(pesos)
    if event == 'CALCULAR':
        try:
            janela['media'].update(f'Média Ponderada: {media_ponderada(notas, pesos)}')
        except ZeroDivisionError:
            janela['media'].update('Digite suas notas e seus pesos')

janela.close()
