class Evento:
    def __init__(self, nome, data, horario, local, objetivo):
        self.__nome = nome
        self.__data = data
        self.__horario = horario
        self.__local = local
        self.__objetivo = objetivo
    def criaEvento(self):
        evento_list = {}
        evento_list[self.__nome] = self.__data, self.__horario, self.__local, self.__objetivo
        return evento_list[self.__nome]