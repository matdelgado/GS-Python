class Doador:
    def __init__(self, nome, cidade, documento, email, endereco, telefone):
        self.__nome = nome
        self.__cidade = cidade
        self.__documento = documento
        self.__email = email
        self.__endereco = endereco
        self.__telefone = telefone
    def bdUsuarios(self):
        bd_usuarios = {}
        bd_usuarios[self.__nome] = self.__cidade, self.__documento, self.__email, self.__endereco, self.__telefone
        return bd_usuarios[self.__nome]