from sys_path import HOME  # noqa: F401
from model import conexoes


def test_duckdb():
    assert conexoes.DB_DUCKDB is not None
