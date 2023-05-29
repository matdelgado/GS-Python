from doador import *
from donatario import *
from alimento import *
from estoque import *
from evento import *
from AjudaPlantar import *
import time

escolha_opcao = int(input("Olá, esse é o projeto Alimentando Futuros!\nVocê deseja doar ou ser um donatário? \n\n 1 - Doar\n 2 - Donatário\n\nInsira a opção: "))
time.sleep(2)

if escolha_opcao == 1:
    nome = input("Certo, por favor, insira o seu nome: ")
    cidade = input("Por favor, insira a cidade da doação que deseja efetuar: ")
    documento = input("Por favor, insira o seu CPF ou CNPJ: ")
    email = input("Insira o seu e-mail: ")
    endereco = input("Por favor, insira o seu endereço: ")
    telefone = input("Por favor, insira o seu telefone: ")

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
    elif desejo == 2:
        contribuicao_tipo_material = input("\nInsira o tipo do material: ")
        quantidade_material = int(input("Insira a quantidade de material: "))
        local_material = input("Insira o local para retirada do material: ")
        adiciona_estoque = Estoque(nome, contribuicao_tipo_material, quantidade_material, local_material).adicionaEstoque()
        print("\nMuito obrigado pela sua solicitação de doação, em breve um de nossos agentes estará entrando em contato para mais informações sobre a coleta.")
        time.sleep(2)
        print("\nDados:\n\nNome: {}\nTipo de material: {}\nQuantidade de material: {}\nLocal do material: {}".format(nome, adiciona_estoque[0], adiciona_estoque[1], adiciona_estoque[2]))
    elif desejo == 3:
        ajudante_conhecimento = input("Insira a área que deseja apoiar: ")
        data_ajuda = input("Insira a data que você terá disponibilidade: ")
        horario_ajuda = input("Insira o horário que você possui disponibilidade, na data informada: ")
        ajuda_plantar = AjudaPlantar(nome, ajudante_conhecimento, data_ajuda, horario_ajuda).ajudaPlantar()
        print("\nMuito obrigado pela vontade em ajudar, em breve um de nossos agentes estará entrando em contato para mais informações sobre a ajuda oferecida")
        time.sleep(2)
        print("\nDados:\n\nNome: {}\nÁrea de ajuda: {}\nData informada: {}\nHorário de disponibilidade: {}".format(nome, ajuda_plantar[0], ajuda_plantar[1], ajuda_plantar[2]))

    else:
        print("Opção inválida, tente novamente.")

    
# elif escolha_opcao == 2:
#     print("a")
# else:
#     print("\nSolução inválida, tente novamente.")