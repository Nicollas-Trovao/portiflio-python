import time
from typing import Generator


def get_coxinhas(*pedidos) -> list:
    print("Preparando toda a fornada de uma vez...")
    time.sleep(2)
    return [f"Coxinha de {pedido}" for pedido in pedidos]

def get_joelhos(*pedidos) -> Generator[any, any, any]:
    for pedido in pedidos:
        print(f"Preparando o joelho de {pedido}...")
        time.sleep(2)
        yield f"Joelho de {pedido}"

        
def main():
    print("Solicitando coxinhas...")
    coxinhas = get_coxinhas("frango", "carne", "queijo")
    for coxinha in coxinhas:
        print(coxinha)

    print("Solicitando joelhos...")
    joelhos = get_joelhos("frango", "carne", "queijo")
    for joelho in joelhos:
        print(joelho)