#Crie um programa usando matemática e f-Strings que nos diga quantos dias,
#semanas, meses nos restam se vivermos até os 90 anos.
#Levará sua idade atual como entrada e enviará uma mensagem com nosso 
#tempo restante neste formato:
#Você tem x dias, y semanas e z meses restantes.

idade = int(input('Por gentileza, insira a sua idade (ex:25):\n>: '))

#dados_de_um_ano:
anos = int(90 - idade)
dias = int(anos * 365)
meses = int(anos * 12)
semanas = int(anos * (dias/7))
horas = int(anos * (dias*24))
minutos = int(anos * (horas*60))
segundos = int(anos * (minutos*60))



print(f'voce tem {meses} meses;\n{semanas} semanas;\n{dias} dias;')
print(f'{horas} horas;\n{minutos} minutos;\n{segundos} segundos.')
print('Até alcançar a idade de 90 Anos.\nAproveite!!!')