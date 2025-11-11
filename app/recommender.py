# app/recommender.py
from typing import Dict, List, Tuple
from .models import Perfil, Carreira

ScoreItem = Tuple[Carreira, float, List[Tuple[str, float]]]  # (carreira, score0..1, gaps)

def _score(perfil_norm: Dict[str, float], carreira: Carreira) -> Tuple[float, List[Tuple[str, float]]]:
    """
    Score ponderado: sum(user*weight)/sum(weight).
    Também retorna gaps: competências com alta importância e nota baixa.
    """
    num, den = 0.0, 0.0
    gaps: List[Tuple[str, float]] = []
    for comp, w in carreira.pesos_competencias.items():
        u = perfil_norm.get(comp, 0.0)
        num += u * w
        den += w
        # gap alto quando w é grande e u é baixo
        if w >= 0.6 and u < 0.7:
            gaps.append((comp, round((0.7 - u) * w, 3)))
    return (num / den if den else 0.0, sorted(gaps, key=lambda x: x[1], reverse=True))

def ranquear_carreiras(perfil: Perfil, carreiras: List[Carreira], top_n: int = 3) -> List[ScoreItem]:
    p = perfil.normalizado()
    avaliados: List[ScoreItem] = []
    for c in carreiras:
        s, gaps = _score(p, c)
        avaliados.append((c, round(s, 3), gaps))
    return sorted(avaliados, key=lambda x: x[1], reverse=True)[:max(1, top_n)]

def trilhas_recomendadas(gaps: List[Tuple[str, float]], trilhas_por_competencia: Dict[str, List[str]], k: int = 3) -> List[str]:
    # Pega até k competências com maiores gaps e monta uma trilha combinada
    sugestoes: List[str] = []
    for comp, _ in gaps[:k]:
        for passo in trilhas_por_competencia.get(comp, [])[:1]:  # 1 passo por competência para ficar objetivo
            sugestoes.append(f"[{comp}] {passo}")
    return sugestoes
