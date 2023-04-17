from PySimpleGUI import PySimpleGUI as tela
import funcsAdaptadas


# Layout/Funcs
def janelaInicial():
    layout = [
    [tela.Button("Cadastrar", size=(65, 1), pad= (5, 5), font=("arial black", 12))],
    [tela.Button("Buscar",  size=(65, 1), pad= (5, 5), font=("arial black", 12))],
    [tela.Button("Editar",  size=(65, 1), pad= (5, 5), font=("arial black", 12))],
    [tela.Button("Deletar",  size=(65, 1), pad= (5, 5), font=("arial black", 12))]
    ]
    return tela.Window("Menu", layout=layout, finalize=True, size=(500, 200))


def janelaBuscar():
    layout = [
        [tela.Text("Deseja buscar por : ", font=("arial black", 14))],
        [tela.Button("Marca", size=(65, 1), pad= (1, 8), font=("arial black", 12))],
        [tela.Button("Modelo", size=(65, 1), pad= (1, 8), font=("arial black", 12))],
        [tela.Button("Motor", size=(65, 1), pad= (1, 8), font=("arial black", 12))],
        [tela.Button("Ano", size=(65, 1), pad= (1, 8), font=("arial black", 12))],
        [tela.Button("Voltar",size=(5, 1), pad= (1, 1), font=("arial black", 12))]

    ]
    return tela.Window("Buscar", layout=layout, finalize=True, size=(500, 300))


def janelaBuscarFiltro(filtro):
    layout = [
        [tela.Text("Insira as informações do veículo: ", font=("arial black", 14))],
        [tela.Text("Filtro", size=(5, 1), pad= (1, 30), font=("arial black", 12)), tela.Input(key="Filtro", font=("arial black", 12))],
        [tela.Button("Voltar", font=("arial black", 12)), tela.Button("Buscar", font=("arial black", 12))]
    ]
    return tela.Window("Filtro de busca", layout=layout, finalize=True, size=(500, 200))


def janelaCadastrar():
    layout = [
        [tela.Text("Insira as informações do veículo: ", font=("arial black", 14))],
        [tela.Text("Marca:  ", font=("arial black", 12)), tela.Input(key="novaMarca", pad= (5, 5), font=("arial black", 12))],
        [tela.Text("Modelo:", font=("arial black", 12)), tela.Input(key="novoModelo" , pad= (5, 5), font=("arial black", 12))],
        [tela.Text("Motor:   ", font=("arial black", 12)), tela.Input(key="novoMotor", pad= (5, 5), font=("arial black", 12))],
        [tela.Text("Ano:      ", font=("arial black", 12)), tela.Input(key="novoAno", pad= (5, 5), font=("arial black", 12))],
        [tela.Button("Voltar", font=("arial black", 12)), tela.Button("Cadastrar", font=("arial black", 12))]
    ]
    return tela.Window("Cadastro", layout=layout, finalize=True, size=(500, 250))


def janelaEditar():
    layout = [
        [tela.Text("Informe o CHASSI do veículo: ", font=("arial black", 14))],
        [tela.Text("Chassi: ", size=(5, 1), pad= (1, 35), font=("arial black", 12)), tela.Input(key="chassiEditar", font=("arial black", 12))],
        [tela.Button("Voltar", size=(5, 1), pad= (1, 8), font=("arial black", 12)), tela.Button("Editar", font=("arial black", 12))]
    ]
    return tela.Window("Edição", layout=layout, finalize=True, size=(500, 200))


def janelaEditarInfos():
    layout = [
        [tela.Text("Insira as novas informações do veículo: ",pad= (5, 10),font=("arial black", 14))],
        [tela.Text("Marca:  ",pad= (5, 8), font=("arial black", 12)), tela.Input(key="novaMarca", pad= (5, 8), font=("arial black", 12))],
        [tela.Text("Modelo:",pad= (5, 8), font=("arial black", 12)), tela.Input(key="novoModelo",pad= (5, 8),font=("arial black", 12))],
        [tela.Text("Motor:   ",pad= (5, 8), font=("arial black", 12)), tela.Input(key="novoMotor",pad= (5, 8),font=("arial black", 12))],
        [tela.Text("Ano:      ",pad= (5, 8),font=("arial black", 12)), tela.Input(key="novoAno",pad= (5, 8),font=("arial black", 12))],
        [tela.Button("Voltar",pad= (5, 8), font=("arial black", 12)), tela.Button("Editar", pad= (5, 8),font=("arial black", 12))]
    ]
    return tela.Window("Edição de Infos", layout=layout, finalize=True, size=(500, 300))


def janelaDeletar():
    layout = [
        [tela.Text("Insira o CHASSI do veículo: ", font=("arial black", 14))],
        [tela.Text("Chassi: ", size=(5, 1), pad= (1, 39), font=("arial black", 12)), tela.Input(key="chassiDeletar", font=("arial black", 12))],
        [tela.Button("Voltar", font=("arial black", 12)), tela.Button("Deletar", font=("arial black", 12))]
    ]
    return tela.Window("Deletar", layout=layout, finalize=True, size=(500, 200))


def janelaLogin():
    layout = [
        [tela.Text("Usuário", font=("arial black", 12)), tela.Input(key="novoUsuario", font=("arial black", 12))],
        [tela.Text("Senha  ", font=("arial black", 12)), tela.Input(key="novaSenha", password_char="*", font=("arial black", 12))] ,
        [],

        [tela.Button("Entrar", font=("arial black", 12), size= (50, 1),pad=(0, 25))],
        [tela.Text("Sistema para Cadastro", font=("arial black", 16))],
        [tela.Text("                De ", font=("arial black", 16))],
        [tela.Text("     Veículos", font=("arial black", 24))],
            ]
    return tela.Window("Login", layout=layout, finalize=True, size= (300, 300))


# Eventos
janelaLogin = janelaLogin()
janelaMenu = janelaInicial()
janelaMenu.hide()
janelaCadastro = janelaCadastrar()
janelaCadastro.hide()
janelaBusca = janelaBuscar()
janelaBusca.hide()
janelaBuscaFiltro = janelaBuscarFiltro("")
janelaBuscaFiltro.hide()
janelaEdicao = janelaEditar()
janelaEdicao.hide()
janelaEdicaoInfo = janelaEditarInfos()
janelaEdicaoInfo.hide()
janelaDeleta = janelaDeletar()
janelaDeleta.hide()

marcaOn = False
modeloOn = False
motorOn = False
anoOn = False
erroDigitagem = False

while True:
    window, evento, valores = tela.read_all_windows()
    if window == janelaLogin and evento == tela.WIN_CLOSED:
        break
    if window == janelaMenu and evento == tela.WIN_CLOSED:
        break
    if window == janelaCadastro and evento == tela.WIN_CLOSED:
        break
    if window == janelaBusca and evento == tela.WIN_CLOSED:
        break
    if window == janelaBuscaFiltro and evento == tela.WIN_CLOSED:
        break
    if window == janelaEdicao and evento == tela.WIN_CLOSED:
        break
    if window == janelaEdicaoInfo and evento == tela.WIN_CLOSED:
        break
    if window == janelaDeleta and evento == tela.WIN_CLOSED:
        break

    # Janelas Login
    if window == janelaLogin and evento == "Entrar":
        if valores["novoUsuario"] == "admin" and valores["novaSenha"] == "admin":
            janelaLogin.hide()
            janelaMenu.un_hide()
        else:
            tela.popup("Usuario ou senha incorretos.", font= ( "arial black", 12))

    # Janelas Busca
    if window == janelaMenu and evento == "Buscar":
        janelaBusca.un_hide()
        janelaMenu.hide()

    if window == janelaBusca and evento == "Marca":
        marcaOn = True
        janelaBuscaFiltro.un_hide()
        janelaBusca.hide()
    if window == janelaBuscaFiltro and evento == "Buscar" and marcaOn:
        tela.popup(funcsAdaptadas.checarVeic("marca", valores["Filtro"]), font= ("arial black", 12))
        marcaOn = False

    if window == janelaBusca and evento == "Modelo":
        modeloOn = True
        janelaBuscaFiltro.un_hide()
        janelaBusca.hide()
    if window == janelaBuscaFiltro and evento == "Buscar" and modeloOn:
        tela.popup(funcsAdaptadas.checarVeic("modelo", valores["Filtro"]), font= ("arial black", 12))
        modeloOn = False

    if window == janelaBusca and evento == "Motor":
        motorOn = True
        janelaBuscaFiltro.un_hide()
        janelaBusca.hide()
    if window == janelaBuscaFiltro and evento == "Buscar" and motorOn:
        tela.popup(funcsAdaptadas.checarVeic("motor", valores["Filtro"]), font= ("arial black", 8))
        motorOn = False

    if window == janelaBusca and evento == "Ano":
        anoOn = True
        janelaBuscaFiltro.un_hide()
        janelaBusca.hide()
    if window == janelaBuscaFiltro and evento == "Buscar" and anoOn:
        tela.popup(funcsAdaptadas.checarVeic("ano", int(valores["Filtro"])), font= ("arial black", 12))
        anoOn = False

    if window == janelaBuscaFiltro and evento == "Voltar":
        janelaBuscaFiltro.hide()
        janelaBusca.un_hide()

    if window == janelaBusca and evento == "Voltar":
        janelaBusca.hide()
        janelaMenu.un_hide()

    # Janelas Cadastro
    if window == janelaMenu and evento == "Cadastrar":
        janelaCadastro.un_hide()
        janelaMenu.hide()
    if window == janelaCadastro and evento == "Cadastrar":
        if valores["novoAno"] == '' or None:
            tela.popup("houve erro de digitação, tente novamente", font= ( "arial black", 12))
            erroDigitagem = True
        if erroDigitagem != True:
            if valores["novaMarca"] and valores["novoModelo"] and valores["novoMotor"] and int(valores["novoAno"]) != None or "0":
                tela.popup(funcsAdaptadas.cadastrarVeic(valores["novaMarca"], valores["novoModelo"], valores["novoMotor"],
                                                        int(valores["novoAno"])), font= ( "arial black", 12))
            else:
                tela.popup("houve erro de digitação, tente novamente", font= ( "arial black", 12))
        erroDigitagem = False
    if window == janelaCadastro and evento == "Voltar":
        janelaCadastro.hide()
        janelaMenu.un_hide()

    # Janelas Edição
    if window == janelaMenu and evento == "Editar":
        janelaEdicao.un_hide()
        janelaMenu.hide()
    if window == janelaEdicao and evento == "Editar":
        if valores["chassiEditar"] != None or '':
            if funcsAdaptadas.getVeicByChassi(int(valores["chassiEditar"])) != []:
                tempChassi = int(valores["chassiEditar"])
                janelaEdicaoInfo.un_hide()
                janelaEdicao.hide()
            else:
                tela.popup("Veículo não encontrado", font= ( "arial black", 12))
        else:
            tela.popup("Digite um chassi válido", font= ( "arial black", 12))
    if window == janelaEdicaoInfo and evento == "Editar":
        if valores["novaMarca"] and valores["novoModelo"] and valores["novoMotor"] and int(valores["novoAno"]) != None:
            funcsAdaptadas.editarVeic(tempChassi, valores["novaMarca"], valores["novoModelo"], valores["novoMotor"],
                                      int(valores["novoAno"]))
            tela.popup("Veículo atualizado com sucesso.", font= ( "arial black", 12))
        else:
            tela.popup("Por favor insira dados válidos", font= ( "arial black", 12))
    if window == janelaEdicaoInfo and evento == "Voltar":
        janelaEdicaoInfo.hide()
        janelaEdicao.un_hide()
    if window == janelaEdicao and evento == "Voltar":
        janelaEdicao.hide()
        janelaMenu.un_hide()

    # Janelas Deletar
    if window == janelaMenu and evento == "Deletar":
        janelaDeleta.un_hide()
        janelaMenu.hide()
    if window == janelaDeleta and evento == "Deletar":
        if valores["chassiDeletar"] != None or '':
            if funcsAdaptadas.getVeicByChassi(int(valores["chassiDeletar"])) != []:
                funcsAdaptadas.deletarVeic(int(valores["chassiDeletar"]))
                tela.popup("Veículo deletado com sucesso.", font= ( "arial black", 12))
            else:
                tela.popup("Veículo não encontrado.", font= ( "arial black", 12))
        else:
            tela.popup("Insira um chassi válido.", font= ( "arial black", 12))
    if window == janelaDeleta and evento == "Voltar":
        janelaDeleta.hide()
        janelaMenu.un_hide()