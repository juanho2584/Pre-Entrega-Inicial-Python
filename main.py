import crud

def mostrar_menu_principal():
    print("\n╔════════════════════════════════════════════╗")
    print("║      🏆 SISTEMA DE GESTIÓN DE PRODUCTOS    ║")
    print("╠════════════════════════════════════════════╣")
    print("║  1. ➕ Crear producto                      ║")
    print("║  2. 🔍 Mostrar productos                   ║")
    print("║  3. ✏️  Actualizar producto                 ║")
    print("║  4. 🗑️  Eliminar producto                   ║")
    print("║  5. 🚪 Salir                               ║")
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
    while True:
        mostrar_menu_principal()
        opcion = input("\n👉 Elige una opción (1-5): ").strip()

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
            print("\n👋 ¡Gracias por utilizar el Sistema de Gestión de Productos!")
            break

        else:
            print("❌ Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
