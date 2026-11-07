from sys_path import HOME  # noqa: F401
from control.llm.controller import Drosophila


def test_drosophila():
    mosca = Drosophila()
    assert mosca.chat("food") == "land_on_food"
