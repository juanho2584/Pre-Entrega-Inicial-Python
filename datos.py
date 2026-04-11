import json
import os
from config import FILE_PATH

def cargar_datos():
    """Lee el diccionario de productos desde el archivo JSON."""
    if not os.path.exists(FILE_PATH):
        # Si el archivo no existe, retorna diccionario vacío
        return {}
    
    try:
        with open(FILE_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            # JSON guarda las claves como strings, hay que convertirlas nuevamente a enteros
            return {int(k): v for k, v in data.items()}
    except json.JSONDecodeError:
        # En caso de estar vacío o dañado el JSON
        return {}

def guardar_datos(productos):
    """Guarda el diccionario de productos en el archivo JSON."""
    try:
        with open(FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump(productos, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"❌ Error crítico al intentar guardar el archivo JSON: {e}")
