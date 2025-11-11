# app/__init__.py
"""
Future Skills Lab (pacote app)
"""

from .models import Perfil, Carreira
from .dataset import COMPETENCIAS, CARREIRAS, TRILHAS_POR_COMPETENCIA
from .recommender import ranquear_carreiras, trilhas_recomendadas
from .cli import run as run_cli

__all__ = [
    "Perfil", "Carreira",
    "COMPETENCIAS", "CARREIRAS", "TRILHAS_POR_COMPETENCIA",
    "ranquear_carreiras", "trilhas_recomendadas",
    "run_cli",
]

__version__ = "0.1.0"
