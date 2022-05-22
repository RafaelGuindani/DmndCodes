"""Json API"""
"""https://jsonapi.org - site com exemplos"""

import json
import jsonpickle

#dumps() -> faz formatação para o formato JSON (aspas duplas)
#em python podemos trabalhar com JSON e PICKLE juntos, podendo desserializar e serializar objetos
# pip install jsonpickle

class Usuario:

    def __init__(self,nome,sobrenome,idade,):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__idade = idade

    @property
    def nome(self):
        return self.__nome
    @property
    def sobrenome(self):
        return self.__sobrenome
    @property
    def idade(self):
        return self.__idade

usuario = Usuario('Rafael','Guindani','35')
with open('usuario.json','w') as arq:
    arq.write(jsonpickle.encode(usuario)) #encode é utilizado para criar dicionário json
