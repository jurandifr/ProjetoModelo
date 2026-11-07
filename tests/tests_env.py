# Ajuste do sys.path
import sys
from pathlib import Path
HOME = Path(__file__).resolve().parents[1]
sys.path.append(str(HOME))

# Imports internos
import main


def test_pytest():
    assert 1 == 1


def test_loadenv():
    assert main.CREDENCIAIS is not None
