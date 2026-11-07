# Readme.md

Arquivo de descrição da aplicação.
Deve funcionar como um "manual".

## Instruções
Executar o setup.py na primeira instalação


## What´s new / Realease
Descreve alterações feitas no projeto

2026-11-07 Versão 1.0 : Gerado o projeto

## Notas
Atualmente é mais moderno usar um arquivo pyproject.toml, no entanto nem todas as ferramentas leem as configurações escritas nele. Por esse motivo ainda usamos um jeito mais compativel.


# Arquivos

### Readme.md
Escrito em markdown, é um manual.

### requirements.txt
Lista as bibliotecas necessárias
Funciona com ´pip install -r requirements.txt´

### setup.py
Executado uma vez na instalação
Cria recursos apenas uma vez

### config.py
Guarda constantes que afetam o funcionamento

### main.py
Arquivo principal da aplicação

### .env
Arquivo do python-dotenv, carrega variaveis ambiente

### .flake8
Arquivo de configuração do linter de checagem de código

### .gitignore
Lista os arquivos que o git não deve copiar

### *.code-workspace
Guarda configurações do VsCode e pastas que estão abertas

### pytest.ini
Configuração para o PyTest reconhecer a pasta de tests

### /tests
Pasta de testes, essencial na metodolodia TDD, Desenvolvimento Orientado por Testes.

### /llm
O modelo MCV (model-control-view) não inclui lugares padonizados para IA, Machine Learning e Servers
Então uma boa pratica isolar a responsabilidade de carregar/conectar com o modelo

### /model
Onde ficam os controlers que gerenciam o recebimento e envio de dados

### /control
Onde fica a lógica e regra de negócios

### /view
Onde fica as interfaces com usuario
Podem ser:
* Widgets (Jupyter)
* Desktop (Tkinter / Pygubu)
* API/Html ( FastApi / Flask / Django)
* Eel (RAD)
* Gradio (RAD)
* Streamlit (Dashboard) 
* ... outros