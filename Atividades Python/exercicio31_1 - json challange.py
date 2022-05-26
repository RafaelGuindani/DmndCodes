import json
import jsonpickle

#Leitura de Json

class RPA:

    @property
    def name(self):
        return self.__name

    @property
    def lastname(self):
        return self.__lastname

    @property
    def company(self):
        return self.__company

    @property
    def rolecompany(self):
        return self.__rolecompany

    @property
    def address(self):
        return self.__address

    @property
    def email(self):
        return self.__email

    @property
    def phoneNumber(self):
        return self.__phoneNumber

with open("challange.json") as arq:
    read = jsonpickle.decode(arq.read())
    a = -1
    for i in range(9):
        a = a + 1
        challange = read [a]

        print(challange.name)
        print (challange.lastname)