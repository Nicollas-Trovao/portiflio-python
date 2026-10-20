from dataclasses import dataclass, field
from datetime import date
from typing import List, Optional

@dataclass
class Pessoa:
    cpf: str
    nome: str
    nascimento: date
    cidadania: Optional[str] = None

    _multas: List[float] = field(default_factory=list, init=False, repr=False)
