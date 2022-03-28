#Instruções
#Escreva um programa que calcule o Índice de Massa Corporal (IMC) a partir do peso e da altura de um usuário.
print('Quer descobrir seu IMC?')
peso = float(input('Por gentileza, insira o seu peso (ex:80.5):\n>: '))
altura = float(input('Agora insira a sua altura (ex:1.70):\n>: '))

imc = peso/(altura ** 2)
resultado = int(imc)

if resultado <18.5:
    print(f'Seu IMC é {resultado}\nAvaliação: Magreza,menor que 18,5 kg/m2;')
elif resultado <24.9:
    print(f'Seu IMC é {resultado}\nAvaliação: Normal,está entre 18,5 e 24,9 kg/m2;')
elif resultado <30:
    print(f'Seu IMC é {resultado}\nAvaliação: Sobrepeso,está entre 24,9 e 30 kg/m2;')
else:
    print(f'Seu IMC é {resultado}\nAvaliação: Obesidade, é maior que 30 kg/m2.')
