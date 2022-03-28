#Se a conta foi R$ 150,00, divida entre 5 pessoas, com 12% de gorjeta.
#Cada pessoa deve pagar (150,00 / 5) * 1,12 = 33,6
#Arredonde o resultado para 2 casas decimais.

print(" ","¨¨"*28)
conta = float(input('Qual o total gasto?\nR$:  '))
totalpessoas = int(input('Pretende dividir a conta com quantas pessoas?\n>: '))
totalgorjeta = int(input('Selecione, quanto de gorjeta almeja aplicar (ex:12)\n>: '))

percentual_gorjeta = totalgorjeta/100
conta_com_gorjeta = conta * percentual_gorjeta
totalconta = conta + conta_com_gorjeta
valor_por_pessoa = totalconta / totalpessoas
valorfinal = round(valor_por_pessoa, 2)

valorfinal = "{:.2f}".format(valorfinal)
totalpessoas = "{:0>2}".format(totalpessoas)

print(f'A conta sera dividida entre {totalpessoas} pessoa(s), e o valor ficou: R${valorfinal}')