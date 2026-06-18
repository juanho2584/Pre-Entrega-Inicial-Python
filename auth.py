import sqlite3
from db import obtener_conexion

def validar_credenciales(username, password):
    if len(username) < 3:
        print("❌ Error: El usuario debe tener al menos 3 caracteres.")
        return False
    if len(password) < 4:
        print("❌ Error: La contraseña debe tener al menos 4 caracteres.")
        return False
    return True

def registrar_usuario():
    print("\n--- 📝 REGISTRO DE USUARIO ---")
    username = input("Ingresa un nuevo nombre de usuario: ").strip()
    
    conn = obtener_conexion()
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT username FROM usuarios WHERE username = ?", (username,))
        if cursor.fetchone():
            print("❌ Error: El usuario ya existe. Intenta con otro.")
            return False
        
        password = input("Ingresa una contraseña: ").strip()
        
        if not validar_credenciales(username, password):
            return False
        
        cursor.execute("INSERT INTO usuarios (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        print("✅ ¡Usuario registrado exitosamente! Ahora puedes iniciar sesión.")
        return True
    except sqlite3.Error as e:
        print(f"❌ Error al registrar usuario: {e}")
        return False
    finally:
        conn.close()

def iniciar_sesion():
    print("\n--- 🔐 INICIAR SESIÓN ---")
    
    conn = obtener_conexion()
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT COUNT(*) FROM usuarios")
        cantidad_usuarios = cursor.fetchone()[0]
        
        if cantidad_usuarios == 0:
            print("⚠️ No hay usuarios registrados en el sistema. Por favor, regístrate primero.")
            return False
            
        intentos_fallidos = 0
        while intentos_fallidos < 3:
            username = input("Usuario: ").strip()
            password = input("Contraseña: ").strip()
            
            cursor.execute("SELECT password FROM usuarios WHERE username = ?", (username,))
            row = cursor.fetchone()
            
            if row and row['password'] == password:
                print(f"\n✅ ¡Bienvenido/a, {username}!")
                return True
            else:
                intentos_fallidos += 1
                if intentos_fallidos >= 3:
                    print("\n❌ Has superado el límite de 3 intentos fallidos. Saliendo del sistema...")
                    return "LOCKED"
                else:
                    print(f"❌ Error: Usuario o contraseña incorrectos.")
                    print(f"⚠️ Te quedan {3 - intentos_fallidos} intento(s).\n")
    except sqlite3.Error as e:
        print(f"❌ Error en la base de datos: {e}")
        return False
    finally:
        conn.close()

def menu_login():
    while True:
        print("\n╔════════════════════════════════════════════╗")
        print("║             🔐 CONTROL DE ACCESO           ║")
        print("╠════════════════════════════════════════════╣")
        print("║  1. Iniciar sesión                         ║")
        print("║  2. Registrarse                            ║")
        print("║  3. Salir del sistema                      ║")
        print("╚════════════════════════════════════════════╝")
        
        opcion = input("\n👉 Elige una opción (1-3): ").strip()
        
        if opcion == "1":
            resultado = iniciar_sesion()
            if resultado == True:
                return True
            elif resultado == "LOCKED":
                return False
        elif opcion == "2":
            registrar_usuario()
        elif opcion == "3":
            print("\n👋 ¡Hasta pronto!")
            return False
        else:
            print("❌ Opción no válida. Intenta de nuevo.")
