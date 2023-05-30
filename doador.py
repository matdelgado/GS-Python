class Doador:
    def __init__(self):
        self.__doadoresBd = []
    def adicionaUsuarios(self, nome, cidade, documento, email, endereco, telefone):
        self.__nome = nome
        self.__cidade = cidade
        self.__documento = documento
        self.__email = email
        self.__endereco = endereco
        self.__telefone = telefone
        self.__doadoresBd.append([self.__documento, self.__nome, self.__cidade, self.__email, self.__endereco, self.__telefone])
    def buscaUsuarios(self, documento):
        for i in self.__doadoresBd:
            if documento in i:
                return True
        return False