from doador import *
from donatario import *
from alimento import *
from estoque import *
from evento import *
import time

escolha_opcao = int(input("Olá, esse é o projeto Alimentando Futuros!\nVocê deseja doar ou ser um donatário? \n\n 1 - Doar\n 2 - Donatário\n\nInsira a opção: "))
time.sleep(2)

if escolha_opcao == 1:
    nome = input("Certo, por favor, insira o seu nome: ")
    cidade = input("Por favor, insira a cidade da doação que deseja efetuar: ")
    documento = input("Por favor, insira o seu CPF ou CNPJ: ")
    email = input("Insira o seu e-mail: ")
    endereco = input("Por favor, insira o seu endereço: ")

    time.sleep(1)
    desejo = int(input("Assinale a opção desejada:\n\n1 - Criar um evento\n2 - Contribuição de materiais para plantação\n3 - Quero ajuda a plantar.\n\nInsira a opção: "))
    time.sleep(1)

    if desejo == 1:
        data_evento = input("\nInsira a data do evento: ")
        horario_evento = input("Insira o horário do evento: ")
        local_evento = input("Insira o local do evento: ")
        objetivo_evento = input("Insira o objetivo do evento: ")
        evento_class = Evento(nome ,data_evento, horario_evento, local_evento, objetivo_evento).criaEvento()
        time.sleep(1)
        print("\nO seu evento foi criado com os seguintes dados: \n\nResponsável: {}\nData: {}\nHorário: {}, \nLocal: {}\nObjetivo do evento: {}".format(nome,evento_class[0], evento_class[1], evento_class[2], evento_class[3]))


    



# elif escolha_opcao == 2:
#     print("a")
# else:
#     print("\nSolução inválida, tente novamente.")