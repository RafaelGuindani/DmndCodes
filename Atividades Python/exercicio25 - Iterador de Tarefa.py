with open('25 - dados.txt', 'r') as fp:
    for line in iter(fp.readline, ''):
        print(line)
