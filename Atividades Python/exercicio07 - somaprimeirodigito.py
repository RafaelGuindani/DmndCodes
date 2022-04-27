#Instructions
#Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
#Warning. Your program should work for different inputs. e.g. any two-digit number.
doisdigitos = input('Insira um número com 2 digitos:\n>: ')

primeiro_numero = doisdigitos[0]
segundo_numero = doisdigitos[1]

resultado = int(primeiro_numero) + int(segundo_numero)

print(f'Primeiro Número: {primeiro_numero}')
print(f'Segundo Número: {segundo_numero}')

print(f'A soma entre os primeiros números é: {resultado}')


