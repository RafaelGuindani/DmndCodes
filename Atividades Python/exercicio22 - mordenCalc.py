
from turtle import clear


while True:
    operadores = input('\nSelecione uma opção:\n'
                    '+ Adição\n'
                    '- Subtração\n'
                    '* Multiplicação\n'
                    '/ Divisão\n'
                    '% Percentual\n'
                    '\nS para Sair\n'
                    '\n>: ').lower()

    if operadores == 's':
            exit ()

    valorA = int(input('\nDigite o 1º Valor: '))
    valorB = int(input('\nDigite o 2º Valor: '))

    if operadores == '-':
            res = valorA - valorB
            print(f'\nO resultado da subtração\n{valorA} menos {valorB} é: {res}\n')

    elif operadores == '+':
            res = valorA + valorB
            print(f'\nO resultado da soma\n{valorA} mais {valorB} é: {res}\n')

    elif operadores == '*':
            res = valorA * valorB
            print(f'\nO resultado da multiplicação\n{valorA} multiplicado por {valorB} é: {res}\n')

    elif operadores == '/':
            res = valorA / valorB
            print(f'\nO resultado da divisão\n{valorA} dividido por {valorB} é: {res}\n')

    elif operadores == '%':
            res = valorB - ((valorA / 100) * valorB)
            print(f'\nO percentual\n{valorA}% de {valorB} é: {res}\n')

    else:
        print('Dados Incorretos')
        exit()

