
while True:

    valorA = int(input('\nDigite o 1º Valor: '))
    valorB = int(input('\nDigite o 2º Valor: '))

    operadores = input('\nSelecione uma opção:\n'
                    '+ Adição\n'
                    '- Subtração\n'
                    '* Multiplicação\n'
                    '/ Divisão\n'
                    '\nS Sair\n'
                    '\n>: ').lower()

    if operadores == '-':
            res = valorA - valorB
            print(f'\nO resultado da subtração é: {res}\n')

    elif operadores == '+':
            res = valorA + valorB
            print(f'\nO resultado da soma é: {res}\n')

    elif operadores == '*':
            res = valorA * valorB
            print(f'\nO resultado da multiplicação é: {res}\n')

    elif operadores == '/':
            res = valorA / valorB
            print(f'\nO resultado da divisão é: {res}\n')

    elif operadores == 's':
        exit ()

    else:
        print('Dados Incorretos')
        exit()

