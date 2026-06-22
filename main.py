import crud
import auth
from db import inicializar_db
from colorama import init, Fore, Style

# Inicializar colorama para soporte de colores en consolas Windows y UNIX
init(autoreset=True)


def mostrar_menu_principal():
    print("\n╔════════════════════════════════════════════╗")
    print("║      🏆 SISTEMA DE GESTIÓN DE PRODUCTOS    ║")
    print("╠════════════════════════════════════════════╣")
    print("║  1. ➕ Crear producto                      ║")
    print("║  2. 🔍 Mostrar productos                   ║")
    print("║  3. ✏️  Actualizar producto                 ║")
    print("║  4. 🗑️  Eliminar producto                   ║")
    print("║  5. 📊 Reporte de stock                    ║")
    print("║  6. 🚪 Salir                               ║")
    print("╚════════════════════════════════════════════╝")

def mostrar_menu_productos():
    print("\n╔════════════════════════════════════════════╗")
    print("║             📦 MOSTRAR PRODUCTOS           ║")
    print("╠════════════════════════════════════════════╣")
    print("║  1. 🔢 Ver producto por código             ║")
    print("║  2. 🆔 Ver producto por ID                 ║")
    print("║  3. 🏷️ Ver productos por categoría          ║")
    print("║  4. 📜 Ver todos los productos             ║")
    print("║  5. 🔙 Volver al menú principal            ║")
    print("╚════════════════════════════════════════════╝")

def imprimir_producto(prod):
    print(f"\n📦 Producto: [{prod['codigo']}] {prod['nombre']}")
    print("---------------------------------------------")
    print(f"  🆔 ID:        {prod['id']}")
    print(f"  🏷️ Categoría: {prod['categoria']}")
    print(f"  🏭 Stock:     {prod['stock']} unidades")
    print(f"  💰 Precio:    ${prod['precio']:.2f}")
    if prod.get('descripcion'):
        print(f"  📝 Info:      {prod['descripcion']}")
    print("---------------------------------------------")

def imprimir_reporte_stock():
    resultados = crud.listar_productos()
    if not resultados:
        print(Fore.RED + "\n❌ No hay productos registrados para generar el reporte.")
        return

    print(Fore.CYAN + Style.BRIGHT + "\n╔══════════════════════════════════════════════════════════════════════════════════════╗")
    print(Fore.CYAN + Style.BRIGHT + "║                          📊 REPORTE DE CONTROL DE STOCK                              ║")
    print(Fore.CYAN + Style.BRIGHT + "╚══════════════════════════════════════════════════════════════════════════════════════╝")
    print(f"📦 Total de productos registrados: {Fore.WHITE + Style.BRIGHT}{len(resultados)}")
    print("Leyenda de alertas: " + Fore.RED + "■ Bajo (<5)" + Fore.RESET + "  " + Fore.YELLOW + "■ Moderado (<8)" + Fore.RESET + "  " + Fore.GREEN + "■ Óptimo (>=8)\n")

    # Cabecera de la Tabla
    print(Fore.BLUE + "┌" + "─"*6 + "┬" + "─"*12 + "┬" + "─"*22 + "┬" + "─"*17 + "┬" + "─"*9 + "┬" + "─"*12 + "┐")
    print(Fore.BLUE + "│" + Fore.CYAN + Style.BRIGHT + f" {'ID':<4} " +
          Fore.BLUE + "│" + Fore.CYAN + Style.BRIGHT + f" {'Código':<10} " +
          Fore.BLUE + "│" + Fore.CYAN + Style.BRIGHT + f" {'Nombre':<20} " +
          Fore.BLUE + "│" + Fore.CYAN + Style.BRIGHT + f" {'Categoría':<15} " +
          Fore.BLUE + "│" + Fore.CYAN + Style.BRIGHT + f" {'Stock':<7} " +
          Fore.BLUE + "│" + Fore.CYAN + Style.BRIGHT + f" {'Precio':<10} " +
          Fore.BLUE + "│")
    print(Fore.BLUE + "├" + "─"*6 + "┼" + "─"*12 + "┼" + "─"*22 + "┼" + "─"*17 + "┼" + "─"*9 + "┼" + "─"*12 + "┤")

    for prod in resultados:
        stock = prod['stock']
        if stock < 5:
            color = Fore.RED + Style.BRIGHT
        elif stock < 8:
            color = Fore.YELLOW + Style.BRIGHT
        else:
            color = Fore.GREEN + Style.BRIGHT
        
        # Truncar nombre o categoría si exceden el límite de columnas para mantener la grilla alineada
        nombre = prod['nombre'][:20]
        categoria = prod['categoria'][:15]
        
        id_str = f"{prod['id']:<4}"
        code_str = f"{prod['codigo']:<10}"
        name_str = f"{nombre:<20}"
        cat_str = f"{categoria:<15}"
        stock_str = f"{prod['stock']:<7}"
        price_str = f"${prod['precio']:.2f}"
        
        print(Fore.BLUE + "│" + color + f" {id_str} " +
              Fore.BLUE + "│" + color + f" {code_str} " +
              Fore.BLUE + "│" + color + f" {name_str} " +
              Fore.BLUE + "│" + color + f" {cat_str} " +
              Fore.BLUE + "│" + color + f" {stock_str} " +
              Fore.BLUE + "│" + color + f" {price_str:<10} " +
              Fore.BLUE + "│")
              
    print(Fore.BLUE + "└" + "─"*6 + "┴" + "─"*12 + "┴" + "─"*22 + "┴" + "─"*17 + "┴" + "─"*9 + "┴" + "─"*12 + "┘")
    print()

def submenu_mostrar():
    while True:
        mostrar_menu_productos()
        opcion = input("\n👉 Elige una opción (1-5): ").strip()

        if opcion == "1":
            print("\n--- 🔢 VER PRODUCTO POR CÓDIGO ---")
            codigo = input("Código del producto: ").strip()
            prod = crud.leer_producto_por_codigo(codigo)
            if prod:
                imprimir_producto(prod)
        elif opcion == "2":
            print("\n--- 🆔 VER PRODUCTO POR ID ---")
            try:
                id_prod = int(input("ID del producto: "))
            except ValueError:
                print("❌ Error: El ID debe ser un número entero.")
                continue
            prod = crud.leer_producto_por_id(id_prod)
            if prod:
                imprimir_producto(prod)
        elif opcion == "3":
            print("\n--- 🏷️ VER PRODUCTOS POR CATEGORÍA ---")
            categoria = input("Categoría a buscar: ").strip()
            resultados = crud.buscar_por_categoria(categoria)
            if resultados:
                print(f"\n🔍 Se encontraron {len(resultados)} productos en la categoría '{categoria}':")
                for prod in resultados:
                    imprimir_producto(prod)
            else:
                print(f"❌ No se encontraron productos en la categoría '{categoria}'.")
        elif opcion == "4":
            print("\n--- 📜 VER TODOS LOS PRODUCTOS ---")
            resultados = crud.listar_productos()
            if resultados:
                print(f"\n📦 Total de productos registrados: {len(resultados)}")
                for prod in resultados:
                    imprimir_producto(prod)
            else:
                print("\n📦 No hay productos registrados.")
        elif opcion == "5":
            break
        else:
            print("❌ Opción no válida. Intenta de nuevo.")

def main():
    inicializar_db()
    if not auth.menu_login():
        return
        
    while True:
        mostrar_menu_principal()
        opcion = input("\n👉 Elige una opción (1-6): ").strip()

        if opcion == "1":
            print("\n--- ➕ CREAR NUEVO PRODUCTO ---")
            codigo = input("Código único (ej: LEC002): ").strip()
            nombre = input("Nombre: ").strip()
            categoria = input("Categoría: ").strip()
            try:
                stock = int(input("Stock (unidades): "))
                precio = float(input("Precio ($): "))
            except ValueError:
                print("❌ Error: Stock y precio deben ser numéricos.")
                continue
            descripcion = input("Descripción breve: ").strip()
            crud.crear_producto(codigo, nombre, categoria, stock, precio, descripcion)

        elif opcion == "2":
            submenu_mostrar()

        elif opcion == "3":
            print("\n--- ✏️ ACTUALIZAR PRODUCTO ---")
            try:
                id_prod = int(input("ID del producto a actualizar: "))
            except ValueError:
                print("❌ Error: ID inválido.")
                continue
            
            prod_actual = crud.leer_producto_por_id(id_prod)
            if not prod_actual:
                continue

            print("Deje en blanco los campos que NO desee modificar (presione Enter).")
            codigo = input(f"Nuevo código ({prod_actual['codigo']}): ").strip() or None
            nombre = input(f"Nuevo nombre ({prod_actual['nombre']}): ").strip() or None
            categoria = input(f"Nueva categoría ({prod_actual['categoria']}): ").strip() or None
            
            stock_input = input(f"Nuevo stock ({prod_actual['stock']}): ").strip()
            stock = int(stock_input) if stock_input else None
            
            precio_input = input(f"Nuevo precio (${prod_actual['precio']:.2f}): ").strip()
            precio = float(precio_input) if precio_input else None
            
            descripcion = input(f"Nueva descripción ({prod_actual.get('descripcion', '')}): ").strip() or None

            crud.actualizar_producto(id_prod, codigo, nombre, categoria, stock, precio, descripcion)

        elif opcion == "4":
            print("\n--- 🗑️ ELIMINAR PRODUCTO ---")
            try:
                id_prod = int(input("ID del producto a eliminar: "))
            except ValueError:
                print("❌ Error: ID inválido.")
                continue
            crud.eliminar_producto(id_prod)

        elif opcion == "5":
            imprimir_reporte_stock()

        elif opcion == "6":
            print("\n👋 ¡Gracias por utilizar el Sistema de Gestión de Productos!")
            break

        else:
            print("❌ Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
