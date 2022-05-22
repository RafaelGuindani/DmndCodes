import pickle

class Filme:

    @property
    def nome(self):
        return self.__nome

    @property
    def personagem(self):
        return self.__personagem


with open("filmes.pickle", "rb") as arq:
    filme1,filme2 = pickle.load(arq) #Descarrega o arquivo aplicando a desserialização
    print(f'O Filme {filme1.nome} teve o personagem {filme1.personagem}')
    print (f'O Filme {filme2.nome} teve o personagem {filme2.personagem}')