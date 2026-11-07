from abc import ABC
import pandas as pd


class ControlController(ABC):
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def process(dados: pd.DataFrame) -> pd.DataFrame | str:
        if len(dados):
            return dados
        return "Sem dados"
