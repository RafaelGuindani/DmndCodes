print('Seja bem vindo!!!')
print('Ao Guindaverse WORLLLLD!!!')

print('Para acessar a montanha russa, por gentileza me informe a sua altura'
      '[ex:1.50]')
try:
      altura = float(input('>:'))
except ValueError:
      print('Por gentileza, siga o padrão. Exemplo: 1.50')
      altura = float(input('Informe a sua altura\n>:'))

print('Por gentileza, informe também a sua idade:')
try:
      idade = int(input('>:'))
except ValueError:
      print('Por gentileza, siga o padrão. Exemplo: 15')
      idade = int(input('Informe a sua idade\n>:'))

if ((altura > 1.30) and (idade >= 10)):

      ingresso_adulto = 11.90
      x = "{:.2f}".format(ingresso_adulto)

      print(f'O Ingresso para adultos custa: R$ {x}')
      print('Deseja também obter fotos das atividades em que participar?')
      fotos_adultos = input(f' as fotos custam + R$ {x}\nSim ou Não?').lower()

      if fotos_adultos == 'sim':
            ingresso_adulto += ingresso_adulto
            x = "{:.2f}".format(ingresso_adulto)
            print(f'O total a ser pago é R$ {x}')
            print('Divirta-se!!!')
      else:
            print(f'O total a ser pago é R$ {x}')
            print('Divirta-se!!!')
else:
      ingresso_kids = 5.90
      y =  "{:.2f}".format(ingresso_kids)

      print('Infelizmente não pode acessar a montanha russa.\
            \nRecomendo brinquedos da ala norte.')
      print(f'O ingresso para acessar o setor infantil custa: R${y}')
      print('Deseja também obter fotos das atividades em que participar?')
      fotos_kids = input(f' as fotos custam + R$ {y}\nSim ou Não?').lower()
      
      if fotos_kids == 'sim':
            ingresso_kids += ingresso_kids
            y = "{:.2f}".format(ingresso_kids)
            print(f'O total a ser pago é R$ {y}')
            print('Divirta-se!!!')
      else:
            ingresso_kids = "{:.2f}".format(y)
            print(f'O total a ser pago é R$ {ingresso_kids}')
            print('Divirta-se!!!')   
