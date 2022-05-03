print('\nBem vindo(a)\nAqui a pizza está quentinha e a massa é bem fofinha\n')
print('Deseja acessar o menu personalizado ou da promoção?\n')
valor_total = 0
bem_vindo = input('1 - Menu personalizado,\n'
                  '2 - Pizza da promoção\n>: ')
if bem_vindo == '2':
    # Sabores de pizza da promoção:
    da_promocao = print('Selecione um dos sabores:')
    lista_promocao = input('1 - Calabresa,\n'
                           '2 - Portuguesa,\n'
                           '3 - Marguerita\n>: ')
    promocao = 15.90
    if lista_promocao == '1':
        print (f'O sabor selecionado foi: Calabresa\nO valor promocional é: {promocao}')
    elif lista_promocao == '2':
        print (f'O sabor selecionado foi: Portuguesa\nO valor promocional é: {promocao}')
    elif lista_promocao == '3':
        print (f'O sabor selecionado foi: Marguerita\nO valor promocional é: {promocao}')
else:

    print('Selecione o tamanho da sua fome:')
    tamanho_pizza = input('(P)equena\n(M)édia\n(G)rande\n(E)stou com muita fome\
    \nDigite >: ').lower()

    if tamanho_pizza == 'p':
        p = 19.90
        valor_total += p
        print(f'\nO Valor atual é de: {valor_total}')

    elif tamanho_pizza == 'm':
        m = 27.90
        valor_total += m
        print(f'\nO Valor atual é de: {valor_total}')

    elif tamanho_pizza == 'g':
        g = 39.90
        valor_total += g
        print(f'\nO Valor atual é de: {valor_total}')

    elif tamanho_pizza == 'e':
        e = 79.90
        valor_total += e
        print(f'\nO Valor atual é de: {valor_total}')
    #: Massa
    print('Dica: Observe as iniciais, e as utilize para definir uma escolha:')
    massa = input('Você deseja a massa:\n(F)ina ou (E)ncorpada\nDigite >: ').lower()
    if massa == 'e':
        encorpada = 5.90
        valor_total += encorpada
        print(f'\nO Valor atual é de: {valor_total}')
    #: Borda
    borda = input('Voce deseja a borda:\n(E)special ou (S)imples\nDigite >: ').lower()
    if borda == 'e':
        borda_especial = 9.90
        valor_total += borda_especial
        print(f'\nO Valor atual é de: {valor_total}')


    print(f'\nO Valor a ser pago é de: {valor_total}')



