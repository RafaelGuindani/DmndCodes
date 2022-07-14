import multiprocessing
from concurrent.futures.process import  ProcessPoolExecutor
import datetime


def main():
    quantidade_de_processamento = multiprocessing.cpu_count()
    hora_inicio = datetime.datetime.now()
    tempo = datetime.datetime.now() - hora_inicio

    with ProcessPoolExecutor(max_workers = quantidade_de_processamento) as executor:
        executor.submit(tarefa01())
        executor.submit(tarefa02())

    print(f'\nRealizado o processamento com {quantidade_de_processamento} core(s)')
    print(f"Etapa terminou em {tempo.total_seconds():.2f} segundos")


def tarefa01():
    a = 0
    while a < 50_000_000:
        #print(f'{a}')
        a += 1


def tarefa02():
    b = 0
    while b < 50_000_000:
        #print(f'{b}')
        b += 1


if __name__ == '__main__':
    main()
