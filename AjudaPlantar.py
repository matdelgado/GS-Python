class AjudaPlantar:
    def __init__(self, nome, conhecimento, data, horario):
        self.__nome = nome
        self.__conhecimento = conhecimento
        self.__data = data
        self.__horario = horario
    def ajudaPlantar(self):
        bdAjuda = {}
        bdAjuda[self.__nome] = self.__conhecimento, self.__data, self.__horario
        return bdAjuda[self.__nome]