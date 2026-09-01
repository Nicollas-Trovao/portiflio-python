from collections import deque
from collections import Counter
from collections import defaultdict

class temporizador:
    hora: int = 60
    minuto: int
    segundo: int
    dq = deque([minuto, segundo])

class palavras:
    palavras = Counter(['a', 'b', 'c', 'd', 'e'])

class dicionario:
    dicionario = defaultdict(list)
    dicionario['a'].append('b')
    dicionario['a'].append('c')
    dicionario['b'].append('d')
    dicionario['b'].append('e')

def __init__(self, dq: deque, hora: int = 60):
    self.hora = hora
    self.minuto = dq[0]
    self.segundo = dq[1]

    print(dicionario.dicionario)



