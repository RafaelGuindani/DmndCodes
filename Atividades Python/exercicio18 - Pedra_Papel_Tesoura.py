import time

#: Config game \\\
contador_de_vitorias = 0
contador_de_empates = 0
contador_de_derrotas = 0
vidas_do_computador = 7
vidas_do_jogador = 5
lista_senha = []

#: Config Aparencia \\\
vermelho = '\033[1;31m'
verde = '\033[1;32m'
amarelo = '\033[1;93m'
magenta = '\033[1;35m'
cyan = '\033[1;36m'
cinza_claro = '	\033[1;37m'
inverte = '\033[;7m'
fechacor = '\033[m'

print(f"{verde}Bem vindo(a) ao joguinho de pedra, papel, tesoura.{fechacor}")

while True:
    print("Antes de iniciarmos, me ajude com algumas informações:")
    print(f"Para encerrar digite: {vermelho}Exit{fechacor}")
    acesso = input(f"voce já tem acesso?\n{verde}Sim\n{vermelho}Nao{fechacor}\n>: ").lower()[0]

    #: Sair ///
    if acesso == "e":
        exit()

    #: Se não tiver acesso ///
    if acesso == "n":

        print(f"{amarelo}Vamos criar o seu acesso:{fechacor}")

        #:Criação de usuário e senha ///
        usuario = input ("Insira seu usuário: ").lower()
        print(usuario)
        senha = input ("insira sua senha: ").lower()
        print(senha)
        confirme_senha = input (f"{amarelo}Confirme sua senha: {fechacor}").lower()
        print(confirme_senha)
        if senha != confirme_senha:
            print (f"{vermelho}As senhas não são identicas. tente novamente{fechacor}")

        if senha == confirme_senha:
                print (f"{verde}Usuário cadastrado.{fechacor}")
                validar_usuario = open ("usuarios_cadastrados.txt", "a")
                validar_usuario.write ("\n")
                validar_usuario.write (usuario.lower())
                validar_usuario.write ("\n")
                validar_usuario.write (senha.lower())
                validar_usuario.close ()
                print (f"\n{amarelo}aguarde um momento{fechacor}")
                time.sleep (0.5)

    if acesso == "s":

        print (f"\n{amarelo}Vamos testar seu acesso{fechacor}")
        usuario = input (f"Por gentileza, informe seu {verde}usuario{fechacor}:\n>: ").lower ()
        senha = input (f"por gentileza, informe sua {verde}senha{verde}: 🔒🔑\n>: ").lower ()
        time.sleep (0.5)

        validar_usuario = open ("usuarios_cadastrados.txt", "r")

        for row in validar_usuario:

            lista_senha.append (row.strip ())
            if usuario and senha in lista_senha:

                print (f"{verde}Acesso concedido{fechacor}")
                time.sleep (0.5)
                print ("\n")

                print ("***********\**********************/***********")
                print (f"{amarelo}*********** {vermelho}Que comecem os jogos{fechacor}{amarelo} ***********{fechacor}")
                print (f"{amarelo}*********** {magenta}PEDRA - {verde}PAPEL - {vermelho}TESOURA ***********{fechacor}")
                print (f"\nVocê inicia com {vidas_do_jogador} vidas,"
                       f"\nSe você for derrotado, perde {vermelho}uma vida{fechacor};"
                       f"\nSe você empatar, as vidas permanecem intactas;"
                       f"\nPara saber sua pontuação digite: {verde}score{fechacor};"
                       f"\nPara sair, digite: {vermelho}Sair{fechacor};"
                       f"\nPara regras, digite: {magenta}Regras{fechacor};"
                       f"\n{inverte}Boa sorte!{fechacor}")

                while True:

                    import random

                    robot_choice = ("pedra", "papel", "tesoura")
                    robot = random.choice (robot_choice)

                    print ("\n***********\**********************/***********")
                    escolha = input (f"Para jogar digite: \n{verde}Pedra\n{cyan}Papel\n{magenta}Tesoura\n>:"
                                     f" {fechacor}").lower ()
                    #: Escolha Pedra
                    if escolha == "pedra" and robot == "papel":
                        print ("\n***********\**********************/***********\n")
                        print (f"O robô escolheu {cinza_claro}{robot} 📄{fechacor}")
                        print(f"{cyan}Papel ganha da pedra (embrulhando-a){fechacor}")
                        print ("Você perdeu esta rodada!")
                        vidas_do_jogador -= 1
                        contador_de_derrotas += 1
                        print (f"Agora você tem {vermelho}{vidas_do_jogador} vidas!{fechacor}")
                        print ("Use com sabedoria!")

                    if escolha == "pedra" and robot == "tesoura":
                        print ("\n***********\**********************/***********\n")
                        print (f"O robô escolheu {cinza_claro}{robot} ✂{fechacor}")
                        print(f"{cyan}Pedra ganha da tesoura (amassando-a ou quebrando-a){fechacor}")
                        print ("Você venceu esta rodada! ✨👀")
                        vidas_do_jogador += 1
                        contador_de_vitorias += 1
                        print (f"Agora você tem {verde}{vidas_do_jogador} vidas!{fechacor}")
                        print ("Muito bem!")

                        time.sleep (0.5)
                    #: Escolha Papel
                    if escolha == "papel" and robot == "pedra":
                        print ("\n***********\**********************/***********\n")
                        print (f"O robô escolheu {cinza_claro}{robot} 🗿{fechacor}")
                        print(f"{cyan}Papel ganha da pedra (embrulhando-a){fechacor}")
                        print ("Você venceu esta rodada! ✨👀")
                        vidas_do_jogador += 1
                        contador_de_vitorias += 1
                        print (f"Agora você tem {verde}{vidas_do_jogador} vidas!{fechacor}")
                        print ("Que sorte em!!")
                        time.sleep (0.5)
                    if escolha == "papel" and robot == "tesoura":
                        print ("\n***********\**********************/***********\n")
                        print (f"O robô escolheu {cinza_claro}{robot} ✂{fechacor}")
                        print ("Você perdeu esta rodada!")
                        vidas_do_jogador -= 1
                        contador_de_derrotas += 1
                        print (f"Agora você tem {vermelho}{vidas_do_jogador} vidas!{fechacor}")
                        print ("Mais sorte na próxima!")
                        time.sleep (0.5)

                    #: Escolha Tesoura
                    if escolha == "tesoura" and robot == "papel":
                        print ("\n***********\**********************/***********\n")
                        print (f"O robô escolheu {cinza_claro}{robot} 📄 {fechacor}")
                        print (f"{cyan}Tesoura ganha do papel (cortando-o){fechacor}")
                        print ("Você venceu esta rodada! ✨👀")
                        vidas_do_jogador += 1
                        contador_de_vitorias += 1
                        print (f"Agora você tem {verde}{vidas_do_jogador} vidas!{fechacor}")
                        print ("Você está indo bem!!")
                        time.sleep (0.5)
                    if escolha == "tesoura" and robot == "pedra":
                        print ("\n***********\**********************/***********\n")
                        print (f"O robô escolheu {cinza_claro}{robot} 🗿{fechacor}")
                        print ("Você perdeu esta rodada!")
                        vidas_do_jogador -= 1
                        contador_de_derrotas += 1
                        print (f"Agora você tem {vermelho}{vidas_do_jogador} vidas!{fechacor}")
                        print ("Pedra esmaga igual o Hulk! mais sorte na próxima.")
                        time.sleep (0.5)

                    #: Escolhas iguais
                    if escolha == "pedra" and robot == "pedra":
                        print ("\n***********\**********************/***********\n")
                        print (f"O robô também escolheu {robot} ")
                        print (f"{amarelo}E*M*P*A*T*E !{fechacor}")
                        contador_de_empates += 1
                        time.sleep (0.5)
                    if escolha == "papel" and robot == "papel":
                        print ("\n***********\**********************/***********\n")
                        print (f"O robô também escolheu {robot} ")
                        print (f"{amarelo}E*M*P*A*T*E !{fechacor}")
                        contador_de_empates += 1
                        time.sleep (0.5)
                    if escolha == "tesoura" and robot == "tesoura":
                        print ("\n***********\**********************/***********\n")
                        print (f"O robô também escolheu {robot} ")
                        print (f"{amarelo}E*M*P*A*T*E !{fechacor}")
                        contador_de_empates += 1
                        time.sleep (0.5)

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
                        exit ()
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
                        exit ()
    else:
        print ("\n***********\**********************/***********\n")
        print ("Seu usuário e senha estão incorretos, por gentileza solicite suporte.\n"
               "envie email para: dmndcode@gmail.com")
        print ("\nOu tente novamente!")
        exit ()
