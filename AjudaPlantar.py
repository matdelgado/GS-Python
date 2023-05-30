class AjudaPlantar:
    def __init__(self):
        self.__bdAjuda = []
    def ajudaPlantar(self,  nome, conhecimento, data, horario):
        self.__nome = nome
        self.__conhecimento = conhecimento
        self.__data = data
        self.__horario = horario
        self.__bdAjuda.append([self.__nome, self.__conhecimento, self.__data, self.__horario])
    def procuraAjudaPlantar(self, nome):
        for i in self.__bdAjuda:
            if self.__nome in i:
                return i
        return False