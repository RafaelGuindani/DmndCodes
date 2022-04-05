import random
from numpy.core.defchararray import isnumeric
resposta = random.randint(0, 11)
while True:
    user_setnumber = input('Entre 0 e 11, advinhe qual o número,\n:> ')
    integer = isnumeric(user_setnumber)
    if integer == True:
        x = int( user_setnumber )
        if x == resposta:
            print(f'{resposta} Numero exato,\nMuito bem.')
            break
        elif x < resposta:
            print('Vamos tentar novamente, uma dica:\nMuito baixo...')
        elif x > resposta:
            print('Oh Nooo... Muito Alto!\n Mais uma chance:')
    else:
        print('Somente números são aceitos! tente novamente.')
    

