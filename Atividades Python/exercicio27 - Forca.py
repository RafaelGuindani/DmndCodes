import random

lista_palavras = ["dakota", "garfield", "milk"]
palavra_escolhida = random.choice(lista_palavras)
print(palavra_escolhida)

mostrar = []
contador_de_palavras = len(palavra_escolhida)

for _ in range(contador_de_palavras):
    mostrar += "_"

fim_de_jogo = False
while not fim_de_jogo:

    escolha_uma_letra = input("Escolha uma letra:\n>: ").lower()

    for posicao in range(contador_de_palavras):
        letra = palavra_escolhida[posicao]

        if letra == escolha_uma_letra:
            mostrar[posicao] = letra

    print(mostrar)

    if "_" not in mostrar:
        fim_de_jogo = True
        print("Você Venceu")
