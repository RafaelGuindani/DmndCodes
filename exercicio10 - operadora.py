#Uma operadora de telefonia cobra R$ 50,00 por um plano básico que dá direito as 100 minutos de telefone.
#Cada minuto excedido custa R$2,00
#Faça um programa para ler a quantidade de minutos consumidos e demonstre o valor a ser pado.

consumo = int(input('Digite a quantidade de minutos consumidos\n>: '))
valor = float(50.0)

if consumo >100:
    valortotal = valor + (consumo-100) * 2.0
    valortotal = "{:.2f}".format(valortotal)

    print('Para 100 minutos o valor é de R$ 50,00')
    print(f'Foi consumido o total de {consumo} minutos ')
    print(f'O valor a ser pago é R$ {valortotal}')
else:
    print(f'o valor a ser pago é R$ {valor}')