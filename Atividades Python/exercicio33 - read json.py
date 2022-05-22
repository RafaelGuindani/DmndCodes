import jsonpickle

class Usuario:

    @property
    def nome(self):
        return self.__nome
    @property
    def sobrenome(self):
        return self.__sobrenome
    @property
    def idade(self):
        return self.__idade
#Leitura de Json

with open("usuario.json") as arq:
    leitura = jsonpickle.decode(arq.read())
    print(leitura)
    print(leitura.nome)
    print(leitura.sobrenome)
    print(leitura.idade)