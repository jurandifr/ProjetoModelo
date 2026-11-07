import os
from dotenv import load_dotenv
import config
from model.controller import ModelController
from control.controller import ControlController

load_dotenv()  # carrega variaveis ambiente
CREDENCIAIS = os.environ.get('CREDENCIAIS')


def run():
    model = ModelController()
    dados = model.get()
    processado = ControlController.process(dados=dados)

    # exemplo
    print(CREDENCIAIS)
    print(config.DEBUG_MODE)
    print(dados)
    print(processado)


if __name__ == "__main__":
    run()
