"""
Executado apenas uma vez, na instalação da aplicação.
"""

import subprocess

subprocess.call("pip install -r requirements.txt", shell=True)
