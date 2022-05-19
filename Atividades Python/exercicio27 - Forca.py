from random import Random


import random

fim_de_partida = False
tentativas_do_usuario = 3
lista_de_palavras = ["Dakota", "Garfield", "Milk", "Ruby"]
palavra_selecionada = random.choice(lista_de_palavras).lower()
quantas_letras_tem = len(palavra_selecionada)


demonstrativo = []

for _ in range(quantas_letras_tem):
    demonstrativo += "_"

while not fim_de_partida:
    uma_letra = input("Informe uma letra:\n>: ").lower()

    for posicao in range(quantas_letras_tem):
        letra = palavra_selecionada[posicao]

        if letra == uma_letra:
            demonstrativo[posicao] = letra

    if uma_letra not in palavra_selecionada:
        tentativas_do_usuario -= 1
        print(f"Voce perdeu uma tentativa, agora tem {tentativas_do_usuario} tentativa(s)")

        if tentativas_do_usuario == 0:

            print("Fim de jogo")
            print("Você Perdeu")

            fim_de_partida = True
            print(f"A palavra era: {palavra_selecionada}")

    print(f"{' '.join(demonstrativo)}")

    if "_" not in demonstrativo:
        fim_de_partida = True
        print("Você Venceu")
