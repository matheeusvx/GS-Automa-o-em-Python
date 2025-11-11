# app/models.py
from dataclasses import dataclass, field
from typing import Dict, List

@dataclass
class Perfil:
    nome: str
    competencias: Dict[str, int]  # 0..10

    def normalizado(self) -> Dict[str, float]:
        # Converte 0..10 para 0..1
        return {k: max(0, min(10, v)) / 10.0 for k, v in self.competencias.items()}

@dataclass
class Carreira:
    nome: str
    descricao: str
    # Pesos 0..1 por competência (importância relativa)
    pesos_competencias: Dict[str, float]
    trilha_aprendizado: List[str] = field(default_factory=list)
