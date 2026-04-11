import os

# Ruta absoluta al archivo JSON (para evitar problemas desde donde se ejecute)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, 'productos.json')
