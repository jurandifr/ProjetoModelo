# Pega o diretório onde ESTE arquivo de teste está atualmente
# Sobe um nível para a raiz do projeto e adiciona ao sys.path
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))


import main


def test_pytest():
    assert 1 == 1


def test_loadenv():
    assert main.CREDENCIAIS is not None
