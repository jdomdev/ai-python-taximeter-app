import sys
import os

# Obtener la ruta absoluta del directorio raíz del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Agregar 'src' al PYTHONPATH
SRC_DIR = os.path.join(BASE_DIR, "src")
sys.path.insert(0, SRC_DIR)  # insert(0, ...) asegura que se use antes que otras rutas


