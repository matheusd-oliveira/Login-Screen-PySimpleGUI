from PySimpleGUI import PySimpleGUI as sg
#                   Criando uma Tela:

# Layout 
sg.theme('Reddit')  # Escolhendo o tema da tela.

layout = [
    [sg.Text('Usuário'), sg.Input(key = 'usuario', size=(20,1))],
    [sg.Text('Senha  '), sg.Input(key = 'senha', password_char = '*', size=(20,1))],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]
# Janela
janela = sg.Window('Login Screen', layout)

# Criando uma segunda tela
sg.theme('Reddit')  # Escolhendo o tema da tela.

layout2 = [
    [sg.Text('Bem vindo, Matheus!')],
    [sg.Button('Sair')]
]

janela2 = sg.Window('Logged', layout2)

# Ler os eventos
while True:
    eventos, valores = janela.read()    # Fazendo um unpacking
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'matheus' and valores['senha'] == '123456':
            janela.close() 

    eventos2 , valores2 = janela2.read()
    if eventos == 'Sair':
        break