from pathlib import Path
import sys

# Pega o diretório onde ESTE arquivo de teste está atualmente
current_dir = Path(__file__).resolve().parent

# Sobe um nível para a raiz do projeto e adiciona ao sys.path
root_dir = current_dir.parent
sys.path.append(str(root_dir))

import main  # noqa: E402

def test_pytest():
    assert 1 == 2

def test_loadenv():
    assert main.CREDENCIAIS is not None