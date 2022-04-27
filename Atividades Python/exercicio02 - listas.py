funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa']
turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
turno_noite = ['Pedro', 'Sophia', 'Bruno']
tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']

lista1 = set(tem_carro).intersection(turno_noite)
print(f'Funcionários que tem carro e trabalham a noite: \n{lista1}\n')

lista2 = set(tem_carro).intersection(turno_dia)
print(f' Funcionários que tem carro e trabalham durante o dia: \n{lista2}\n')

lista3 = set(funcionarios).difference(tem_carro)
print(f'Funcionários que não tem carro: \n{lista3}')