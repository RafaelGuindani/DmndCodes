import random

# Defina os nomes separados por virgula [ Rafael, Andressa, Emanuelly, Rafaella ] ///
anfitriao = input('Insira os nomes, separados por virgulas\n')

# Separe os nomes pelo seu delimitador ///
delimitador = anfitriao.split(",")

# Conte quantos nomes tem na lista ///
contador_de_nomes = len(delimitador)

# Escolha aleatória do nome ///
escolha_aleatoria = random.randint(0, contador_de_nomes - 1)
quem_paga_hoje = delimitador[escolha_aleatoria]
print(f'Hoje quem paga a conta é {quem_paga_hoje}')
