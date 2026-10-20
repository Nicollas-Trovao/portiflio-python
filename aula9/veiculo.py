from dataclasses import dataclass

from pessoa import Pessoa
from marca import Marca

@dataclass(slots=True, frozen=True)
class veiculo:
    placa: str
    cor: str
    proprietario: Pessoa
    marca: Marca