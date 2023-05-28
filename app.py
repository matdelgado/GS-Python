from doador import *
from donatario import *
from alimento import *
from estoque import *

escolha_opcao = int(input("Olá, esse é o projeto Alimentando Futuros!\nVocê deseja doar ou ser um donatário? \n\n 1 - Doar\n 2 - Donatário\n\nInsira a opção:"))

if escolha_opcao == 1:
    nome = input("Certo, por favor, insira o seu nome: ")
    cidade = input("Por favor, insira a cidade da doação que deseja efetuar: ")
    documento = input("Por favor, insira o seu CPF ou CNPJ.")
    email = input("Insira o seu e-mail!")
    endereco = input("Por favor, insira o seu endereço.")

    desejo = int(input("Assinale a opção desejada:\n\n1 - Criar um evento\n2 - Contribuição de materiais para plantação\n3 - Quero ajuda a plantar."))

    if desejo == 1:


    



elif escolha_opcao == 2:
    print("a")
else:
    print("\nSolução inválida, tente novamente.")