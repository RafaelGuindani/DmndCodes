import time
import colorama

from threading import Thread
from queue import Queue


def geradorDeDados(queue):
    for i in range(1, 11):
        print(colorama.Fore.GREEN + f'Dados {i} gerado.', flush = True)
        time.sleep(2)
        queue.put(i)


def consumidorDeDados(queue):
    while queue.qsize() > 0:
        valor = queue.get()
        print(colorama.Fore.RED + f'Dados {valor + 2} processado', flush = True)
        time.sleep(0.5)
        queue.task_done()


if __name__ == '__main__':
    print(colorama.Fore.WHITE + 'Sistema iniciado', flush = True)
    queue = Queue()
    th1 = Thread(target = geradorDeDados, args = (queue,))
    th2 = Thread(target = consumidorDeDados, args = (queue,))

    th1.start()
    th1.join()

    th2.start()
    th2.join()
