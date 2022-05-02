primeiro_nome = input("insira o seu nome:\n>: ")
segundo_nome = input("Insira o nome da pessoa que tem interesse:\n>: ")

combinar_nomes = primeiro_nome + segundo_nome

letras_minusculas_nomes = combinar_nomes.lower()

t = letras_minusculas_nomes.count("t")
r = letras_minusculas_nomes.count("r")
u = letras_minusculas_nomes.count("u")
e = letras_minusculas_nomes.count("e")

true = t + r + u + e

l = letras_minusculas_nomes.count("l")
o = letras_minusculas_nomes.count("o")
v = letras_minusculas_nomes.count("v")
e = letras_minusculas_nomes.count("e")

love = l + o + v + e

score_do_amor = int(str(true) + str(love))

print(f'{score_do_amor}%')

if (score_do_amor < 10) or (score_do_amor > 90):
    print(f'O resultado é {score_do_amor}%, vocês vão ficar juntos igual chocolate e leite condensado.')

elif (score_do_amor >= 40) and (score_do_amor <= 50):
    print(f'O resultado é {score_do_amor}%, vocês ficarão juntos.')

else:
    print (f'O resultado é {score_do_amor}%')
