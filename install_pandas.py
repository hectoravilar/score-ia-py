import subprocess
import sys

# Instala pandas no Python atual
subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas"])
print("Pandas instalado com sucesso!")