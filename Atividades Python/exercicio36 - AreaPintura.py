import math

def areaPintura(altura, largura, cobertura):
    area = altura * largura
    quant_cobertura = math.ceil(area / cobertura)
    print(f'Voce vai precisar de {quant_cobertura} lata(s) de tinta(s)')


a = int(input("Altura da parede: "))
b = int(input("Largura da parede: "))
c = int(input("Quantidade de cobertura: "))

areaPintura(altura = a,largura = b,cobertura = c)