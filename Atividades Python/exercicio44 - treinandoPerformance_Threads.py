import threading
import multiprocessing
import datetime

lock = threading.RLock()


def main():
    quantidade_de_processamento = multiprocessing.cpu_count()
    print(f'Realizado o processamento com {quantidade_de_processamento} core(s)')

    hora_inicio = datetime.datetime.now()

    tarefas = [
        threading.Thread(target = tarefa01, ),
        threading.Thread(target = tarefa02, )
    ]

    [tarefa.start() for tarefa in tarefas]
    [tarefa.join() for tarefa in tarefas]

    tempo = datetime.datetime.now() - hora_inicio
    print(f"Etapa terminou em {tempo.total_seconds():.2f} segundos")


def tarefa01():
    with lock:
        a = 0
        while a < 50_000_000:
            #print(f'{a}')
            a += 1


def tarefa02():
    with lock:
        b = 0
        while b < 50_000_000:
            #print(f'{b}')
            b += 1


if __name__ == '__main__':
    main()
