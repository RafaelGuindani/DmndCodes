import threading
import random
import time
from typing import List

lock = threading.RLock()

class Conta:

    def __init__(self, saldo = 0) -> None:
        self.saldo = saldo


def main():
    contas = criar_contas()

    with lock:
        total = sum(conta.saldo for conta in contas)

    print('Iniciando transferencias...')

    tarefas = [
        threading.Thread(target = servicos, args = (contas, total)),
        threading.Thread (target = servicos, args = (contas, total)),
        threading.Thread (target = servicos, args = (contas, total)),
        threading.Thread (target = servicos, args = (contas, total)),
        threading.Thread (target = servicos, args = (contas, total)),
        threading.Thread (target = servicos, args = (contas, total))
    ]

    [tarefa.start() for tarefa in tarefas]
    [tarefa.join() for tarefa in tarefas]

    print('Transferencias completas.')
    validaBanco(contas, total)


def servicos(contas, total):
    for _ in range(1, 10_000):
        conta1, conta2 = pegaDuasContas(contas)
        valor = random.randint(1, 100)
        transferir(conta1, conta2, valor)
        validaBanco(contas, total)


def criar_contas() -> List[Conta]:
    return [
        Conta (saldo = random.randint (5_000, 10_000)),
        Conta (saldo = random.randint (5_000, 10_000)),
        Conta (saldo = random.randint (5_000, 10_000)),
        Conta (saldo = random.randint (5_000, 10_000)),
        Conta (saldo = random.randint (5_000, 10_000)),
        Conta (saldo = random.randint (5_000, 10_000)),
    ]


def transferir(origem: Conta, destino: Conta, valor: int):
    if origem.saldo < valor:
        return

    with lock:
        origem.saldo -= valor
        time.sleep(0.001)
        destino.saldo += valor


def validaBanco(contas: List[Conta], total: int):
    with lock:
        atual = sum(conta.saldo for conta in contas)

    if atual != total:
        print(f'Erro: Balanço bancário inconsistente, BRL$ {atual:.2f} vs {total:.2f}', flush = True)
    else:
        print(f'Tudo certo: Balanço bancario consistente: BRL$ {total:.2f}', flush = True)


def pegaDuasContas(contas):
    conta1 = random.choice(contas)
    conta2 = random.choice(contas)

    while conta1 == conta2:
        conta2 = random.choice(contas)

    return conta1, conta2


if __name__ == '__main__':
    main()