class Evento:
    def __init__(self, ):
        self.evento_list = []
    def criaEvento(self, nome, data, horario, local, objetivo):
        self.__nome = nome
        self.__data = data
        self.__horario = horario
        self.__local = local
        self.__objetivo = objetivo
        self.evento_list.append([self.__nome, self.__data, self.__horario, self.__local, self.__objetivo])
    def buscaEvento(self, nome):
        for i in self.evento_list:
            if nome in i:
                return i
        return False