from sys_path import HOME  # noqa: F401
import main


def test_pytest():
    assert 1 == 1


def test_loadenv():
    assert main.CREDENCIAIS is not None
