import sys
from pathlib import Path
HOME = Path(__file__).resolve().parents[1]
sys.path.append(str(HOME))

DB_DUCKDB = f"duckdb:///{HOME / "model" / "database" / "db.duckdb"}"

# Só executa se executado como principal
if __name__ == "__main__":
    print(DB_DUCKDB)
