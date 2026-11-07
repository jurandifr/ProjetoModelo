import os
from dotenv import load_dotenv

load_dotenv()  # carrega variaveis ambiente

CREDENCIAIS = os.environ.get('CREDENCIAIS')

if __name__ == "__main__":
    # exemplo
    print(CREDENCIAIS)
