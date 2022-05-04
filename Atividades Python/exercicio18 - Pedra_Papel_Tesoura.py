import time

print("Bem vindo(a) ao joguinho de pedra, papel, tesoura.")

contador_de_vitorias = 0
contador_de_empates = 0
contador_de_derrotas = 0
vidas_do_computador = 7
vidas_do_jogador = 5
lista_senha = []

while True:
    print("Antes de iniciarmos, me ajude com algumas informações:")
    print("Para encerrar digite: Sair")
    acesso = input("voce já tem acesso?\nSim\nNao\n>: ").lower()
    if acesso == "sair":
        exit()
    if acesso == "nao":
        print("Vamos criar o seu acesso:")
        usuario = input ("Insira seu usuário: ")
        senha = input ("insira sua senha: ")
        confirme_senha = input ("Confirme sua senha: ")

        if senha != confirme_senha:
            print ("As senhas não são identicas. tente novamente")

        elif senha == confirme_senha:
            print ("Usuário cadastrado.")
            validar_usuario = open ("usuarios_cadastrados.txt", "a")
            validar_usuario.write ("\n")
            validar_usuario.write (usuario)
            validar_usuario.write ("\n")
            validar_usuario.write (senha)
            validar_usuario.close ()
            print("\naguarde um momento")
    else:

        print("\nVamos testar seu acesso")
        usuario = input("Por gentileza, informe seu usuario:\n>: ")
        senha = input("por gentileza, informe sua senha: 🔒🔑\n>: ")
        validar_usuario = open("usuarios_cadastrados.txt","r")
        for row in validar_usuario:
            lista_senha.append(row.strip())
            if usuario and senha in lista_senha:
                print("Acesso concedido")
                print ("\n")
                print ("\n")
                print ("\n")

                print ("***********\**********************/***********")
                print ("*********** Que comecem os jogos ***********")
                print ("*********** PEDRA - PAPEL - TESOURA ***********")
                print (f"\nVocê inicia com {vidas_do_jogador} vidas,"
                       f"\nSe você for derrotado, perde uma vida;"
                       f"\nSe você empatar, as vidas permanecem intactas;"
                       f"\nPara saber sua pontuação digite: score"
                       f"\nPara sair, digite: Sair"
                       f"\nBoa sorte!")

                while True:
                    import random
                    robot_choice = ("pedra", "papel", "tesoura")
                    robot = random.choice(robot_choice)

                    print ("\n***********\**********************/***********")
                    escolha = input("Para jogar digite: \nPedra🗿\nPapel📄\nTesoura✂\n>: ").lower()
                    #: Escolha Pedra
                    if escolha == "pedra" and robot == "papel":
                        print ("\n***********\**********************/***********\n")
                        print(f"O robô escolheu {robot} 📄")
                        print("Você perdeu esta rodada!")
                        vidas_do_jogador -= 1
                        contador_de_derrotas += 1
                        print (f"Agora você tem {vidas_do_jogador} vidas!")
                        print ("Use com sabedoria!")

                    if escolha == "pedra" and robot == "tesoura":
                        print ("\n***********\**********************/***********\n")
                        print(f"O robô escolheu {robot} ✂")
                        print("Você venceu esta rodada! ✨👀")
                        vidas_do_jogador += 1
                        contador_de_vitorias += 1
                        print (f"Agora você tem {vidas_do_jogador} vidas!")
                        print ("Muito bem!")

                        time.sleep(0.5)
                    #: Escolha Papel
                    if escolha == "papel" and robot == "pedra":
                        print ("\n***********\**********************/***********\n")
                        print (f"O robô escolheu {robot} 🗿")
                        print ("Você venceu esta rodada! ✨👀")
                        vidas_do_jogador += 1
                        contador_de_vitorias += 1
                        print (f"Agora você tem {vidas_do_jogador} vidas!")
                        print ("Que sorte em!!")
                        time.sleep(0.5)
                    if escolha == "papel" and robot == "tesoura":
                        print ("\n***********\**********************/***********\n")
                        print (f"O robô escolheu {robot} ✂")
                        print ("Você perdeu esta rodada!")
                        vidas_do_jogador -= 1
                        contador_de_derrotas += 1
                        print (f"Agora você tem {vidas_do_jogador} vidas!")
                        print ("Mais sorte na próxima!")
                        time.sleep(0.5)

                    #: Escolha Tesoura
                    if escolha == "tesoura" and robot == "papel":
                        print ("\n***********\**********************/***********\n")
                        print (f"O robô escolheu {robot} ")
                        print ("Você venceu esta rodada! ✨👀")
                        vidas_do_jogador += 1
                        contador_de_vitorias += 1
                        print (f"Agora você tem {vidas_do_jogador} vidas!")
                        print ("Você está indo bem!!")
                        time.sleep(0.5)
                    if escolha == "tesoura" and robot == "pedra":
                        print ("\n***********\**********************/***********\n")
                        print (f"O robô escolheu {robot} ")
                        print ("Você perdeu esta rodada!")
                        vidas_do_jogador -= 1
                        contador_de_derrotas += 1
                        print (f"Agora você tem {vidas_do_jogador} vidas!")
                        print ("Pedra esmaga igual o Hulk! mais sorte na próxima.")
                        time.sleep(0.5)

                    #: Escolhas iguais
                    if escolha == "pedra" and robot == "pedra":
                        print ("\n***********\**********************/***********\n")
                        print (f"O robô também escolheu {robot} ")
                        print ("E*M*P*A*T*E !")
                        contador_de_empates += 1
                        time.sleep(0.5)
                    if escolha == "papel" and robot == "papel":
                        print ("\n***********\**********************/***********\n")
                        print (f"O robô também escolheu {robot} ")
                        print ("E*M*P*A*T*E !")
                        contador_de_empates += 1
                        time.sleep(0.5)
                    if escolha == "tesoura" and robot == "tesoura":
                        print ("\n***********\**********************/***********\n")
                        print (f"O robô também escolheu {robot} ")
                        print ("E*M*P*A*T*E !")
                        contador_de_empates += 1
                        time.sleep(0.5)

                    # Sistema:
                    if escolha == "regras":
                        print ("\n***********\**********************/***********\n")
                        print ("\nPedra ganha da tesoura (amassando-a ou quebrando-a)."
                                "\nTesoura ganha do papel (cortando-o)."
                                "\nPapel ganha da pedra (embrulhando-a).")
                    if escolha == "vidas":
                        print ("\n***********\**********************/***********\n")
                        print (vidas_do_jogador)
                    if escolha == "score":
                        print ("\n***********\**********************/***********\n")
                        print (f"Você acumulou {contador_de_vitorias} vitórias.")
                        print (f"você tem {contador_de_empates} empates.")
                        print (f"você perdeu {contador_de_derrotas} vezes.")
                    if vidas_do_jogador == 0:
                        print ("\n***********\**********************/***********\n")
                        print ("Obrigado por participar.")
                        print ("Você não tem mais vidas.")
                        print (f"Você acumulou {contador_de_vitorias} vitórias.")
                        print (f"você tem {contador_de_empates} empates.")
                        print (f"você perdeu {contador_de_derrotas} vezes.")
                        exit()
                    if vidas_do_computador == 0:
                        print ("\n***********\**********************/***********\n")
                        print ("Obrigado por participar.")
                        print ("Você venceu e não tenho mais vidas.")
                        print (f"Você acumulou {contador_de_vitorias} vitórias.")
                        print (f"você tem {contador_de_empates} empates.")
                        print (f"você perdeu {contador_de_derrotas} vezes.")
                        break
                    if escolha == "sair":
                        print ("\n***********\**********************/***********\n")
                        print (f"Você acumulou {contador_de_vitorias} vitórias.")
                        print (f"você tem {contador_de_empates} empates.")
                        print (f"você perdeu {contador_de_derrotas} vezes.")
                        print ("Fim de jogo")
                        exit()
            else:
                print ("\n***********\**********************/***********\n")
                print("Seu usuário e senha estão incorretos, por gentileza solicite suporte.\n"
                      "envie email para: dmndcode@gmail.com")
                print("\nOu tente novamente!")