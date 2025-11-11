# app/dataset.py
from typing import Dict, List
from .models import Carreira

# Lista de competências avaliadas (use livremente no CLI)
COMPETENCIAS: List[str] = [
    "logica",
    "criatividade",
    "colaboracao",
    "adaptabilidade",
    "comunicacao",
    "pensamento_critico",
    "resolucao_problemas",
    "programacao",
    "dados",
    "design",
    "lideranca",
]

# Mapeia competência -> trilha/ideias de estudo (mostradas quando há gap)
TRILHAS_POR_COMPETENCIA: Dict[str, List[str]] = {
    "logica": ["Exercícios de lógica (HackerRank/LeetCode)", "Khan Academy – Lógica"],
    "criatividade": ["Desafios de ideação (Design Sprint)", "Mind mapping semanal"],
    "colaboracao": ["Scrum básico", "Pair programming em mini-projetos"],
    "adaptabilidade": ["Rotação de tarefas quinzenal", "Reflexões pós-sprint (retros)"],
    "comunicacao": ["Toastmasters/clubes de fala", "Escrita técnica curta semanal"],
    "pensamento_critico": ["Estudos de caso com 5 Porquês", "Mapas de argumento"],
    "resolucao_problemas": ["Ciclos PDCA/Kepner-Tregoe", "Katas diários (20 min)"],
    "programacao": ["Python essentials (docs + pequenos scripts)", "Projetos 100 dias de código"],
    "dados": ["Estatística básica + pandas", "SQL 101 + mini dashboards"],
    "design": ["Fundamentos de UX, heurísticas Nielsen", "Wireframes no Figma"],
    "lideranca": ["Delegação e feedback (SBI)", "Facilitação de reuniões"],
}

# Conjunto de carreiras com pesos por competência (0..1)
CARREIRAS: List[Carreira] = [
    Carreira(
        nome="Engenheiro(a) de Software",
        descricao="Constrói sistemas, APIs e apps com foco em qualidade e manutenção.",
        pesos_competencias={
            "logica": 0.9, "programacao": 1.0, "resolucao_problemas": 0.9,
            "colaboracao": 0.7, "comunicacao": 0.6, "adaptabilidade": 0.7,
            "pensamento_critico": 0.7, "dados": 0.4, "design": 0.3, "criatividade": 0.5,
            "lideranca": 0.3,
        },
        trilha_aprendizado=[
            "Python + Estruturas de Dados",
            "Boas práticas (PEP8, testes, logging)",
            "APIs REST/CLI + pequenos projetos",
        ],
    ),
    Carreira(
        nome="Cientista de Dados",
        descricao="Explora dados, modela e extrai insights para apoiar decisões.",
        pesos_competencias={
            "logica": 0.8, "dados": 1.0, "programacao": 0.8, "pensamento_critico": 0.9,
            "resolucao_problemas": 0.8, "comunicacao": 0.7, "colaboracao": 0.6,
            "adaptabilidade": 0.6, "design": 0.3, "criatividade": 0.6, "lideranca": 0.3,
        },
        trilha_aprendizado=[
            "Estatística básica → pandas/NumPy",
            "SQL prático + storytelling com dados",
            "Modelagem ML introdutória",
        ],
    ),
    Carreira(
        nome="UX Designer",
        descricao="Projeta experiências e interfaces centradas no usuário.",
        pesos_competencias={
            "design": 1.0, "criatividade": 0.9, "comunicacao": 0.8, "colaboracao": 0.8,
            "pensamento_critico": 0.7, "adaptabilidade": 0.7, "dados": 0.4,
            "resolucao_problemas": 0.7, "programacao": 0.3, "logica": 0.5, "lideranca": 0.3,
        },
        trilha_aprendizado=[
            "Heurísticas de usabilidade",
            "Pesquisa com usuários e protótipos",
            "Figma: wireframe → protótipo",
        ],
    ),
    Carreira(
        nome="DevOps/SRE",
        descricao="Automação de entrega, observabilidade e confiabilidade.",
        pesos_competencias={
            "programacao": 0.8, "resolucao_problemas": 0.9, "adaptabilidade": 0.9,
            "colaboracao": 0.8, "comunicacao": 0.6, "logica": 0.8, "dados": 0.5,
            "lideranca": 0.4, "pensamento_critico": 0.7, "design": 0.2, "criatividade": 0.5,
        },
        trilha_aprendizado=[
            "Automação com scripts (Python/CLI)",
            "Versionamento, CI/CD e monitoramento",
            "Infra como código (conceitos)",
        ],
    ),
    Carreira(
        nome="Analista de Produto",
        descricao="Conecta necessidades do usuário à estratégia do negócio.",
        pesos_competencias={
            "comunicacao": 0.9, "colaboracao": 0.9, "pensamento_critico": 0.8,
            "dados": 0.7, "adaptabilidade": 0.8, "lideranca": 0.6, "criatividade": 0.6,
            "resolucao_problemas": 0.7, "programacao": 0.2, "design": 0.5, "logica": 0.6,
        },
        trilha_aprendizado=[
            "Descoberta de produto (discovery)",
            "Métricas de produto (North Star, AARRR)",
            "Roadmaps e priorização",
        ],
    ),
]
