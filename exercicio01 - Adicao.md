#: Função soma.
def soma():
#: comentário sobre adição.
    print('*'*60)
    print("Esta é uma das operações básicas da aritmética."
          "\nNa sua forma mais simples, a adição combina dois números em um único número,"
          "\ndenominado soma, total ou resultado.")
    print('*'*60)
    print('')
#: Questionario para saber quantos valores iremos calcular.    
    inf_val = int(input('Adição: utilizaremos quantos números?  '))
    print('')
    print(f'iremos somar 0{inf_val} números')
    qtd_val = 0
    for i in range(0, inf_val):
#: Inclusão dos valores.
        qtd_val += int(input('Insira o valor número 0'+str(i + 1)+': > '))
    print('')
#: Resultado final.    
    print(f'O resultado é: {qtd_val}')
soma()