# Readme.md

Arquivo de descrição da aplicação.
Deve funcionar como um "manual".

## Instruções
Executar o setup.py na primeira instalação

## What´s new / Realease
Descreve alterações feitas no projeto

2026-11-06 Versão 1.0 : Gerado o projeto
2026-11-07 Versão 1.0.1 : Ampliada a estrutura de exemplos e postado no Github

## Notas
Atualmente é mais moderno usar um arquivo pyproject.toml, no entanto nem todas as ferramentas leem as configurações escritas nele. Por esse motivo ainda usamos um jeito mais compativel.

# Recomendações 

## Extensões VScode:

Vão te economizar tempo

 * autoDocstring
 * Better Comments
 * Flake8 (instale o pacote compativel com a extensão ´pip install flake8==7.3.0´ .)
 * Markdown All in One
 * Python Debugger (se qusier usar o recurso de parar o código em execução para analisar)
 * Black Formatter
 * Power Mode ( é só divertida)

## Bibliotecas Python  

Opcionais mas ajudam muito

* flake8
* pytests
* pygubu-designer (para usar as janelas do tkinter)

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

### __init__.py
Até o python 3.3 era obrigatório para reconhecer um módulo
Depois do 3.3 as pastas são importadas como namespaces
Fazendo o __init__.py ser mais voltado ao quando vocÊ quer controlar a importação ou inicializar coisas no módulo

### pytest.ini
Configuração para o PyTest reconhecer a pasta de tests

### /tests
Pasta de testes, essencial na metodolodia TDD, Desenvolvimento Orientado por Testes.

## O modelo MCV
A ideia de estruturar em pastas e separar as obrigações, cria classes genéricas que encapsulam variaveis e funções que serão acopladas apenas na estrutura final e chamadas pelo main.py

### /llm
O modelo MCV (model-control-view) não inclui lugares padonizados para IA, Machine Learning e Servers
Então uma boa pratica isolar a responsabilidade de carregar/conectar com o modelo

### /model
Onde ficam os controlers que gerenciam o recebimento e envio de dados

### /control
Onde fica a lógica e regras de negócios

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