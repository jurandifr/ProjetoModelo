import sqlalchemy as sa
from abc import ABC
import pandas as pd

# Ajuste do sys.path
import sys
from pathlib import Path
HOME = Path(__file__).resolve().parents[1]
sys.path.append(str(HOME))

# Imports internos
from model import conexoes


class ModelController(ABC):
    def __init__(self) -> None:
        super().__init__()
        self._db = sa.create_engine(conexoes.DB_DUCKDB)

    @staticmethod
    def sql(name: str) -> sa.TextClause:
        """_summary_

        Args:
            name (str): _description_

        Returns:
            sa.TextClause: _description_
        """
        query = (HOME / "model" / "sql" / f"{name}.sql").read_text(encoding="utf-8")
        return sa.text(query)

    def get(self) -> pd.DataFrame:
        """_summary_\n
        Retorna os dados que serão usados
        Returns:
            sa.Sequence | None: _description_
        """
        with self._db.connect() as cursor:
            res = cursor.execute(ModelController.sql("duck_db_show"))
            if res.returns_rows:
                return pd.DataFrame(res.fetchall())  # O cast é apenas para a tipagem não reclamar
            return pd.DataFrame()
