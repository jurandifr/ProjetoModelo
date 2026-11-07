import sys
from pathlib import Path
# sys.path.append(str(Path(__file__).resolve().parents[1]))  # A partir da pasta superior
sys.path.append(str(Path.cwd()))  # A partir da pasta de execução

from model import conexoes


def test_duckdb():
    assert conexoes.DB_DUCKDB is not None
