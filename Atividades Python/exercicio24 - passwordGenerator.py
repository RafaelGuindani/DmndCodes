import random
from collections import OrderedDict

quantidadeDeNumeros = int(input("\nInforme a quantidade de números:\n"))
quantidadeDeLetras = int(input("\nInforme a quantidade de letras:\n"))
quantidadeDeSimbolos = int(input("\nInforme a quantidade de simbolos:\n"))

numeros = ['9', '1', '2', '3', '4', '5', '6', '7', '8', '0']
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
          'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
          'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
          'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
          'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
          'Y', 'Z']
simbolos = ['!', '<', '>', '@', '#', '$', '%', '&', '|', '^',
            '*', '(', ')', '/', '+', '-', '.', '?', '°','²',
            '³', '£', '¢', '¬', ',']
password_list = []

for char in range(1, quantidadeDeNumeros +1):
    password_list.append(random.choice(numeros))

for char in range(1, quantidadeDeLetras +1):
    password_list.append(random.choice(letras))

for char in range(1, quantidadeDeSimbolos +1):
    password_list.append(random.choice(simbolos))

random.shuffle(password_list)
print("")

password = ""
for char in password_list:
    password += char

final_password = list(OrderedDict.fromkeys(password))
random.shuffle(final_password)

password2 = ""
for char in final_password:
    password2 += char

soma = len(password)
soma2 = len(password2)


print(f"Sua senha contém {soma} caracteres: {password}\n"
      f"ou contendo {soma2} caracteres: {password2}")
