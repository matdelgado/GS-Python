class Estoque:
    def __init__(self, nome, tipo, quantidade, local):
        self.__nome = nome
        self.__tipo = tipo
        self.__quantidade = quantidade
        self.__local = local
    def adicionaEstoque(self):
        __materiais_estoque = {}
        __materiais_estoque[self.__nome] = self.__tipo, self.__quantidade, self.__local 
        return __materiais_estoque[self.__nome]