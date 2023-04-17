from tinydb import Query, TinyDB

import random
bd = TinyDB("Banco de Dado.json")
carro = Query()

def getVeicByChassi(info):
    return bd.search(carro.chassi == info)

def cadastrarVeic(tempMarca, tempModelo, tempMotor, tempAno):
    bd.insert({"marca":tempMarca, "modelo":tempModelo, "motor":tempMotor, "ano":tempAno, "chassi":random.randrange(1000,1000000,9876)})
    return "Veículo Cadastrado com sucesso."

def exibir(info):
    retorno = str("")
    formatacao = info
    for y in range(0, len(formatacao)):
        exib = formatacao[y]
        retorno = retorno + "\n" + "Marca: " + exib["marca"] + "\n" + "Modelo:" + exib["modelo"] + "\n" + "Motor:" + exib["motor"] + "\n" + "Ano:" + str(exib["ano"]) + "\n" + "Chassi:" + str(exib["chassi"]) + "\n"
    return retorno

def checarVeic(info, valor):
    if info.lower() == "marca":
        return exibir(bd.search(carro.marca == valor.lower()))
    elif info.lower() == "modelo":
        return exibir(bd.search(carro.modelo == valor.lower()))
    elif info.lower() == "motor":
        return exibir(bd.search(carro.motor == valor.lower()))
    elif info.lower() == "ano":
        return exibir(bd.search(carro.ano == int(valor)))
    else:
        return "Erro"

def editarVeic(chassi, tempMarca, tempModelo, tempMotor, tempAno):
    
    return bd.upsert({"marca":tempMarca, "modelo":tempModelo, "motor":tempMotor, "ano":tempAno}, carro.chassi == chassi)

def deletarVeic(chassi):
    return bd.remove(carro.chassi == chassi)