import sqlite3
import os
from config import DB_PATH

def obtener_conexion():
    """Retorna una conexión activa a la base de datos SQLite."""
    conn = sqlite3.connect(DB_PATH)
    # Permite acceder a las columnas por nombre como si fuera un diccionario
    conn.row_factory = sqlite3.Row
    return conn

def inicializar_db():
    """Crea las tablas de usuarios y productos si no existen en la base de datos."""
    conn = obtener_conexion()
    cursor = conn.cursor()
    
    try:
        # Habilitar claves foráneas
        cursor.execute("PRAGMA foreign_keys = ON;")
        
        # Tabla de usuarios
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                username TEXT PRIMARY KEY NOT NULL,
                password TEXT NOT NULL
            );
        """)
        
        # Tabla de productos
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                codigo TEXT UNIQUE NOT NULL,
                nombre TEXT NOT NULL,
                categoria TEXT NOT NULL,
                stock INTEGER NOT NULL DEFAULT 0,
                precio REAL NOT NULL,
                descripcion TEXT
            );
        """)
        
        conn.commit()
    except sqlite3.Error as e:
        print(f"❌ Error al inicializar la base de datos: {e}")
    finally:
        conn.close()
