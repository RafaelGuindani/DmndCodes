print('Seja bem vindo!!!')
print('Ao Guindaverse WORLLLLD!!!')

print('Para acessar a montanha russa, por gentileza me informe a sua altura'
      '[ex:1.50]')
altura = float(input('>:'))
print('Por gentileza, informe também a sua idade:')
idade = int(input('>:'))

if ((altura < 1.30) and (idade < 10)):
    print('Infelizmente não pode acessar a montanha russa.\nRecomendo brinquedos da ala norte.')
    print('O ingresso para crianças custa: R$ 5,90')
else:
      print('O Ingresso para adultos custa: R$ 11,90')
      print('Divirta-se, não esqueça do cinto de segurança!!!')
