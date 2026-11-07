"""
Executado apenas uma vez, na instalação da aplicação.
"""

import subprocess

subprocess.call("pip install -r requirements.txt", shell=True)
subprocess.call(""" curl -L --create-dirs --output-dir control/llm -O \
    "https://huggingface.co/mondk/fly-brain/resolve/main/fly-behavior-classifier.Q4_K_M.gguf" 
""", shell=True)