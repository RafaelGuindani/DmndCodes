import threading
import multiprocessing
import datetime
import math


def main():

    qtd_cores = multiprocessing.cpu_count()
    print(f'Realizado o processamento matemático com {qtd_cores} core(s).')

    inicio = datetime.datetime.now ()

    threads = []
    for n in range(1, qtd_cores + 1):
        ini = 50_000_000 * (n - 1) / qtd_cores
        fim = 50_000_000 * n / qtd_cores
        print(f'Core {n} processando de {ini} até {fim}')

        threads.append(
            threading.Thread(
                target = computar,
                kwargs = {'start': ini, 'fim': fim},
                daemon = True
            )
        )
    [th.start() for th in threads]
    [th.join() for th in threads]

    tempo = datetime.datetime.now() - inicio
    print(f"Esta etapa terminou em {tempo.total_seconds ():.2f} segundos")


def computar(fim, start=1):
    pos = start
    fator = 1000 * 1000
    while pos < fim:
        pos += 1
        math.sqrt ((pos - fator) * (pos - fator))


if __name__ == '__main__':
    main ()
