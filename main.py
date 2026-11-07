import os
from dotenv import load_dotenv
import config
from model.controller import ModelController

load_dotenv()  # carrega variaveis ambiente
CREDENCIAIS = os.environ.get('CREDENCIAIS')

model = ModelController()
dados = model.get()


if __name__ == "__main__":
    # exemplo
    print(CREDENCIAIS)
    print(config.DEBUG_MODE)
    print(dados)
