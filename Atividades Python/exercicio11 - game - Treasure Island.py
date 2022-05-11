print('Bem-vindo à TREASURE ISLAND.\nSua missão é encontrar o TESOURO.')
print('Você está em uma encruzilhada. Onde você deseja ir?')
escolha = input('Escolha uma opção: [Direita] ou [Esquerda]\n>:').lower()
if escolha == 'direita':
    print('Hmmm escolha interessante...')
    escolha2 = input('Você caminhou e caminhou, chegou a um lago. Há uma ilha no meio do lago.\nEscolha [Esperar] para esperar por um barco ou [Nadar] para nadar\n>:').lower()
    if escolha2 == 'esperar':
        escolha3 = input("Você chega na ilha ileso, levado por um barco. Nesta ilha há uma casa com 3 portas.\nUma [vermelha], uma [Amarela] e uma [Azul].\n Qual cor você escolhe?\n>:").lower()
        if escolha3 == 'vermelha':
            print("É uma sala cheia de fogo. Fim de jogo.")
        elif escolha3 == 'amarela':
            print("Você encontrou o tesouro! Você ganhou!")
            print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
            row1 = ["⬜️", "⬜️", "⬜️"]
            row2 = ["⬜️", "⬜️", "⬜️"]
            row3 = ["⬜️", "⬜️", "⬜️"]
            map = [row1, row2, row3]
            print (f"{row1}\n{row2}\n{row3}")
            posicao = input ("Aonde gostaria de guardar o seu tesouro?\n>: ")
            horizontal = int (posicao [0])
            vertical = int (posicao [1])
            map [vertical - 1] [horizontal - 1] = "❌   "
            print (f"{row1}\n{row2}\n{row3}")

        elif escolha3 == 'azul':
            print("Você entra em uma sala de feras. Fim de jogo.")
        else:
            print("Você escolheu uma porta que não existe. Fim de jogo.")
    else:
        print('Você é atacado por uma truta brava. Fim de jogo.')
else:
    print('Audaciosa escolha... foi instinto?')
    print('Você foi pelo caminho a esquerda, e logo a frente\nCaiu em um buraco e morreu.')
    print('Fim de jogo')