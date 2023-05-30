class Donatario:
    def __init__(self):
        self.__donatarioBd = []
    def adicionaUsuarios(self, nome, cidade, cpf, email, endereco, telefone):
        self.__nome = nome
        self.__cidade = cidade
        self.__cpf = cpf
        self.__email = email
        self.__endereco = endereco
        self.__telefone = telefone
        self.__donatarioBd.append([self.__cpf, self.__nome, self.__cidade, self.__email, self.__endereco, self.__telefone])
    def buscaUsuarios(self, documento):
        for i in self.__donatarioBd:
            if documento in i:
                return True
        return False