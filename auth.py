import json
import os

ARCHIVO_USUARIOS = 'usuarios.json'

def cargar_usuarios():
    if not os.path.exists(ARCHIVO_USUARIOS):
        return {}
    try:
        with open(ARCHIVO_USUARIOS, 'r', encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError:
        return {}

def guardar_usuarios(usuarios):
    with open(ARCHIVO_USUARIOS, 'w', encoding='utf-8') as file:
        json.dump(usuarios, file, indent=4)

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
    usuarios = cargar_usuarios()
    
    username = input("Ingresa un nuevo nombre de usuario: ").strip()
    if username in usuarios:
        print("❌ Error: El usuario ya existe. Intenta con otro.")
        return False
    
    password = input("Ingresa una contraseña: ").strip()
    
    if not validar_credenciales(username, password):
        return False
    
    usuarios[username] = password
    guardar_usuarios(usuarios)
    print("✅ ¡Usuario registrado exitosamente! Ahora puedes iniciar sesión.")
    return True

def iniciar_sesion():
    print("\n--- 🔐 INICIAR SESIÓN ---")
    usuarios = cargar_usuarios()
    
    if not usuarios:
        print("⚠️ No hay usuarios registrados en el sistema. Por favor, regístrate primero.")
        return False
        
    intentos_fallidos = 0
    while intentos_fallidos < 3:
        username = input("Usuario: ").strip()
        password = input("Contraseña: ").strip()
        
        if username in usuarios and usuarios[username] == password:
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
