import datetime
import asyncio
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


async def gerar_dados(quantidade: int, dados: asyncio.Queue):
    print(f'Aguarde a geração de {quantidade :.2f} dados...')
    for idx in range(1, quantidade + 1):
        item = idx * idx
        await dados.put((item, datetime.datetime.now()))
        await asyncio.sleep(0)
    print(f'{quantidade :.2f} dados gerados com sucesso...')


async def processar_dados(quantidade: int, dados: asyncio.Queue):
    print(f'Aguarde o processamento de {quantidade :.2f} dados...')
    processados = 0
    while processados < quantidade:
        await dados.get()
        processados += 1
        await asyncio.sleep(0)
    print(f'Foram processados {processados :.2f} itens')


def main():
    total = 5_000
    dados = asyncio.Queue()

    print(f'Computando {total :.2f} dados...')

    el = asyncio.get_event_loop()

    tarefa1 = el.create_task(gerar_dados(total, dados))
    tarefa2 = el.create_task(processar_dados(total, dados))

    tarefas = asyncio.gather(tarefa1, tarefa2)
    el.run_until_complete(tarefas)


if __name__ == '__main__':
    main()