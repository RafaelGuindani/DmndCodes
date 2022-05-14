from time import sleep

def fatorial(n=1, show=False):
    f = 1
    for i in range(n, 0, -1):
        f = f * i
        if show:
            print(f, end=" ", flush=True)
            sleep(2)
    print(f'\nO fatorial {n}! é {f}')

while True:
    operadores = input('\nSelecione uma opção:\n'
                    '+ Adição\n'
                    '- Subtração\n'
                    '* Multiplicação\n'
                    '/ Divisão\n'
                    'Comparação\n'
                    'Fatorial\n'
                    '% Percentual\n'
                    'AM2 Area\n'
                    '\nS para Sair\n'
                    '\n>: ').lower()

    if operadores == 's':
            exit ()

    if operadores == '-':
            valorA = int(input('\nDigite o 1º Valor: '))
            valorB = int(input('\nDigite o 2º Valor: '))
            res = valorA - valorB
            print(f'\nO resultado da subtração\n{valorA} menos {valorB} é: {res}\n')

    elif operadores == '+':
            valorA = int(input('\nDigite o 1º Valor: '))
            valorB = int(input('\nDigite o 2º Valor: '))
            res = valorA + valorB
            print(f'\nO resultado da soma\n{valorA} mais {valorB} é: {res}\n')

    elif operadores == '*':
            valorA = int(input('\nDigite o 1º Valor: '))
            valorB = int(input('\nDigite o 2º Valor: '))
            res = valorA * valorB
            print(f'\nO resultado da multiplicação\n{valorA} multiplicado por {valorB} é: {res}\n')

    elif operadores == '/':
            valorA = int(input('\nDigite o 1º Valor: '))
            valorB = int(input('\nDigite o 2º Valor: '))
            res = valorA / valorB
            print(f'\nO resultado da divisão\n{valorA} dividido por {valorB} é: {res}\n')

    elif operadores == 'comparação':
            valorA = int(input('\nDigite o 1º Valor: '))
            valorB = int(input('\nDigite o 2º Valor: '))
            if valorA > valorB:
                print(f'\nO valor {valorA} é maior que {valorB}\n')
            if valorA < valorB:
                print(f'\nO valor {valorB} é maior que {valorA}\n')
            if valorA == valorB:
                print(f'\nO valor {valorA} é igual a {valorB}\n')

    elif operadores == 'fatorial':
            # Main
            n = int(input('Digite um número: '))

            # Mostrando numeros
            fatorial(n,show=True)


    elif operadores == '%':
            valorA = int(input('\nDigite o 1º Valor: '))
            valorB = int(input('\nDigite o 2º Valor: '))
            res = valorB - ((valorA / 100) * valorB)
            print(f'\nO percentual\n{valorA}% de {valorB} é: {res}\n')

    elif operadores == 'm2':
            valorA = int(input('\nDigite a largura: '))
            valorB = int(input('\nDigite o comprimento: '))
            res = valorA * valorB
            print(f'\nLargura {valorA} multiplicado pelo Comprimento {valorB}\n'
                  f'A Area em metros quadrados é: {res}M²\n')

    else:
        print('Dados Incorretos')
        exit()

