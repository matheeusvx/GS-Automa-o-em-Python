# app/cli.py
from typing import Dict
from .models import Perfil
from .dataset import COMPETENCIAS, CARREIRAS, TRILHAS_POR_COMPETENCIA
from .recommender import ranquear_carreiras, trilhas_recomendadas

def _entrada_int(msg: str, minimo: int = 0, maximo: int = 10) -> int:
    while True:
        try:
            v = int(input(msg).strip())
            if minimo <= v <= maximo:
                return v
            print(f"Digite um inteiro entre {minimo} e {maximo}.")
        except ValueError:
            print("Valor inválido. Tente novamente.")

def _coletar_perfil() -> Perfil:
    print("\n== Cadastro de Perfil ==")
    nome = input("Seu nome: ").strip() or "Anonimo"
    print("Avalie suas competências de 0 a 10 (seja honesto!):")
    comps: Dict[str, int] = {}
    for c in COMPETENCIAS:
        comps[c] = _entrada_int(f"  {c}: ")
    return Perfil(nome=nome, competencias=comps)

def run():
    perfil: Perfil | None = None
    while True:
        print("\n--- Future Skills Lab (CLI) ---")
        print("1) Cadastrar/editar meu perfil")
        print("2) Analisar perfil (Top 3 Carreiras + Trilhas)")
        print("3) Listar carreiras disponíveis")
        print("0) Sair")
        op = input("Opção: ").strip()

        if op == "0":
            print("Até logo!")
            break

        elif op == "1":
            perfil = _coletar_perfil()
            print(f"✔ Perfil salvo: {perfil.nome}")

        elif op == "2":
            if not perfil:
                print("Cadastre um perfil primeiro (opção 1).")
                continue
            print(f"\n== Recomendações para: {perfil.nome} ==")
            ranking = ranquear_carreiras(perfil, CARREIRAS, top_n=3)
            for i, (carreira, score, gaps) in enumerate(ranking, start=1):
                print(f"\n{i}) {carreira.nome}  |  aderência: {int(score*100)}%")
                print(f"   {carreira.descricao}")
                trilha = trilhas_recomendadas(gaps, TRILHAS_POR_COMPETENCIA, k=3)
                if trilha:
                    print("   → Trilhas sugeridas:")
                    for passo in trilha:
                        print(f"      - {passo}")
                else:
                    print("   → Você já está bem alinhado(a) a esta carreira! Continue aprofundando.")
                if carreira.trilha_aprendizado:
                    print("   → Roteiro-base da carreira:")
                    for passo in carreira.trilha_aprendizado:
                        print(f"      - {passo}")

        elif op == "3":
            print("\n== Carreiras mapeadas ==")
            for c in CARREIRAS:
                print(f"- {c.nome}")
        else:
            print("Opção inválida.")
