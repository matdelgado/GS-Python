class Estoque:
    def __init__(self):
        self.estoque = []
    def adicionaEstoque(self, documento, tipo, quantidade, local):
        self.__documento = documento
        self.__tipo = tipo
        self.__quantidade = quantidade
        self.__local = local
        self.__status = "DISPONÍVEL"
        self.estoque.append([self.__documento, self.__tipo, self.__quantidade, self.__local, self.__status])
    def ConsultaEstoque(self, item):
        for i in self.estoque:
            if item in i:
                return True
        return False
    def retiraEstoque(self, item):
        for i in self.estoque:
            if item in i:
                self.estoque.pop(i)
                return True
        return False
    def reservaObjeto(self, documento, item):
        for i in self.estoque:
            if item in i:
                i[0] = documento
                i[4] = "RESERVADO"