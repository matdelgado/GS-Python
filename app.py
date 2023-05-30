from Doador import *
from Donatario import *
from Estoque import *
from Evento import *
from AjudaPlantar import *
import time

escolha_opcao = int(input("Olá, esse é o projeto Alimentando Futuros!\nVocê deseja doar ou ser um donatário? \n\n 1 - Doar\n 2 - Donatário\n\nInsira a opção: "))

if escolha_opcao == 1 or escolha_opcao == 2:
    while True:
        verifica_base = int(input("Você já é usuário de nosso sistema?\n\n1 - SIM\n2 - NÃO \nAssinale a opção: "))
        if verifica_base == 1 or verifica_base == 2:
            nome = input("Certo, Insira o seu nome: ")
            cidade = input("Insira a cidade da doação que deseja efetuar: ")
            documento = input("Insira o seu CPF ou CNPJ: ")
            email = input("Insira o seu e-mail: ")
            endereco = input("Insira o seu endereço: ")
            telefone = input("Insira o seu telefone: ")
            if escolha_opcao == 1:
                A = Doador()
                if verifica_base == 1:
                    if (A.buscaUsuarios(documento)):
                        print("Usuário encontrado, bem-vindo {}!".format(nome))
                        break
                    else:
                        print("Usuário não encontrado na base de dados, tente novamente.")
                        exit()
                elif verifica_base == 2:
                    A.adicionaUsuarios(nome, cidade, documento, email, endereco, telefone)
                    print("Usuário cadastrado com sucesso!")
                    break
            elif escolha_opcao == 2:
                A = Donatario()
                if verifica_base == 1:
                    if (A.buscaUsuarios(documento)):
                        print("Usuário encontrado, bem-vindo {}!".format(nome))
                        break
                    else:
                        print("Usuário não encontrado na base de dados, tente novamente.")
                        exit()
                elif escolha_opcao == 2:
                    A.adicionaUsuarios(nome, cidade, documento, email, endereco, telefone)
                    print("Usuário cadastrado com sucesso!")
                    break
        else:
            print("Opção inválida! ")
            exit()
else:
    print("Opção inválida!")
    exit()
if escolha_opcao == 1:
    time.sleep(1)
    desejo = int(input("Assinale a opção desejada:\n\n1 - Criar um evento beneficente\n2 - Contribuição de materiais para plantação\n3 - Quero ajuda a plantar.\n\nInsira a opção: "))
    time.sleep(1)
    if desejo == 1:
        data_evento = input("\nInsira a data do evento: ")
        horario_evento = input("Insira o horário do evento: ")
        local_evento = input("Insira o local do evento: ")
        objetivo_evento = input("Insira o objetivo do evento: ")
        evento = Evento()
        evento.criaEvento(nome ,data_evento, horario_evento, local_evento, objetivo_evento)
        evento_dados = evento.buscaEvento(nome)
        time.sleep(1)
        print("\nO seu evento foi criado com os seguintes dados: \n\nResponsável: {}\nData: {}\nHorário: {}, \nLocal: {}\nObjetivo do evento: {}".format(nome,evento_dados[0], evento_dados[1], evento_dados[2], evento_dados[3]))
    elif desejo == 2:
        contribuicao_tipo_material = input("\nInsira o tipo do material: ")
        quantidade_material = int(input("Insira a quantidade de material: "))
        local_material = input("Insira o local para retirada do material: ")
        adiciona_estoque = Estoque().adicionaEstoque(documento, contribuicao_tipo_material, quantidade_material, local_material)
        print("\nMuito obrigado pela sua solicitação de doação, em breve um de nossos agentes estará entrando em contato para mais informações sobre a coleta.")
        time.sleep(2)
        print("\nDados:\n\nNome: {}\nTipo de material: {}\nQuantidade de material: {}\nLocal do material: {}".format(nome, adiciona_estoque[0], adiciona_estoque[1], adiciona_estoque[2]))
    elif desejo == 3:
        ajudante_conhecimento = input("Insira a área que deseja apoiar: ")
        data_ajuda = input("Insira a data que você terá disponibilidade: ")
        horario_ajuda = input("Insira o horário que você possui disponibilidade, na data informada: ")
        ajuda_plantar = AjudaPlantar()
        ajuda_plantar.ajudaPlantar(nome, ajudante_conhecimento, data_ajuda, horario_ajuda)
        ajuda = ajuda_plantar.procuraAjudaPlantar(nome)
        print(ajuda)
        print("\nMuito obrigado pela vontade em ajudar, em breve um de nossos agentes estará entrando em contato para mais informações sobre a ajuda oferecida")
        time.sleep(2)
        print("\nDados:\n\nNome: {}\nÁrea de ajuda: {}\nData informada: {}\nHorário de disponibilidade: {}".format(nome, ajuda[0], ajuda[1], ajuda[2]))
    else:
        print("Opção inválida, tente novamente.")
elif escolha_opcao == 2:
    time.sleep(1)
    desejo = input("Insira o material necessário: ")
    time.sleep(1)
    material_busca = Estoque().ConsultaEstoque(desejo)
    if material_busca == True:
        reserva_material = Estoque().reservaObjeto(documento, desejo)
        print("Certo, o seu objeto foi localizado, um de nossos agentes entrará em contato com você para mais informações sobre a retirada.")
    else:
        print("Material não encontrado, tente novamente mais tarde.")
else:
    print("\nSolução inválida, tente novamente.")