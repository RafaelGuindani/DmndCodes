import threading
import datetime
import time

def main():
    start = datetime.datetime.now ()

    threads = [
        threading.Thread(target = contar, args = ('elefante', 10)),
        threading.Thread (target = contar, args = ('Buraco', 2)),
        threading.Thread (target = contar, args = ('Moeda', 28)),
        threading.Thread (target = contar, args = ('Pato', 12))
        ]

    [th.start() for th in threads]

    [th.join() for th in threads]
    performance = datetime.datetime.now () - start
    print (f"a tarefa foi concluida em {performance.total_seconds ():.2f} segundos")

def contar(o_que, numero):
    for n in range(1, numero+1):
        print(f'{n} {o_que}(s)...')
        time.sleep(0.3)

if __name__ == '__main__':
    main()