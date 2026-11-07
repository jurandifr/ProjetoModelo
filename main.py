import os
from dotenv import load_dotenv
import config
from model.controller import ModelController
from control.controller import ControlController
from llm.controller import Drosophila

load_dotenv()  # carrega variaveis ambiente
CREDENCIAIS = os.environ.get('CREDENCIAIS')


def run():
    model = ModelController()
    dados = model.get()
    processado = ControlController.process(dados=dados)

    mosca = Drosophila()

    # exemplo
    print(f"Credenciais: {CREDENCIAIS}")
    print(f"DEBUG_MODE: {config.DEBUG_MODE}")
    print(f"DataFrame Shape: {dados.shape}")
    print(f"Saida do Processamento: {processado}")
    print(f"Mosca: {mosca.chat("food")}")


if __name__ == "__main__":
    run()
