# Como os testes são executados a partir da pasta "tests", não perdem o vinculo do imports
# Ajuste do sys.path
import sys
from pathlib import Path
HOME = Path(__file__).resolve().parents[1]
sys.path.append(str(HOME))
