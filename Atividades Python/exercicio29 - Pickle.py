"""
    Pickle
- O objetivo do Pickle é realizar a serialização ou desserialização dos dados recebidos como objeto.
- Seu conteudo não é entendível para a leitura humana.
Obs: Apenas faça leitura de arquivos quando você tiver certeza se a fonte é confiavel, pois pode conter dados maliciosos.

# escrevendo em arquivos pickle.
"""

import pickle

class Filme:
    def __init__(self,nome,personagem):

        self.__nome = nome
        self.__personagem = personagem

    @property
    def nome(self):
        return self.__nome

    @property
    def personagem(self):
        return self.__personagem


filme1 = Filme("007", "James Bond")
filme2 = Filme("Matrix", "Neo")

with open("filmes.pkl", "wb") as arq:
    pickle.dump((filme1, filme2), arq) #DUMP - Transforma o conteudo em binário, Cria a serialização do objeto.