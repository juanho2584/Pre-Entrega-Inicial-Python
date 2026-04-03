# ==================== GESTIÓN DE PRODUCTOS  ====================
# Diccionario principal: cada producto tiene un id (numérico) y un código único (alfanumérico)
productos = {}
contador_id = 1  # Para asignar IDs automáticos

# ==================== FUNCIONES CRUD ===========================

def validar_codigo_unico(codigo, id_actual=None):
    """
    Verifica que el código no esté en uso por otro producto.
    Si id_actual se proporciona, ignora ese producto (útil para actualizaciones).
    """
    for prod in productos.values():
        if prod["codigo"] == codigo and (id_actual is None or prod["id"] != id_actual):
            return False
    return True

def crear_producto(codigo, nombre, categoria, stock, precio, descripcion):
    global contador_id
    # Validaciones básicas
    if not codigo or not nombre or not categoria:
        print("❌ Error: El código, nombre y categoría son obligatorios.")
        return None
    if stock < 0:
        print("❌ Error: El stock no puede ser negativo.")
        return None
    if precio <= 0:
        print("❌ Error: El precio debe ser mayor que 0.")
        return None
    if not validar_codigo_unico(codigo):
        print(f"❌ Error: El código '{codigo}' ya está en uso.")
        return None

    producto = {
        "id": contador_id,
        "codigo": codigo,
        "nombre": nombre,
        "categoria": categoria,
        "stock": stock,
        "precio": round(precio, 2),
        "descripcion": descripcion
    }
    productos[contador_id] = producto
    contador_id += 1
    print(f"✅ Producto '{nombre}' (Código: {codigo}) creado con ID {producto['id']}.")
    return producto

def leer_producto_por_id(id_producto):
    if id_producto in productos:
        return productos[id_producto]
    else:
        print(f"❌ Error: No existe producto con ID {id_producto}.")
        return None

def leer_producto_por_codigo(codigo):
    for prod in productos.values():
        if prod["codigo"] == codigo:
            return prod
    print(f"❌ Error: No existe producto con código '{codigo}'.")
    return None

def actualizar_producto(id_producto, codigo=None, nombre=None, categoria=None, stock=None, precio=None, descripcion=None):
    if id_producto not in productos:
        print(f"❌ Error: No existe producto con ID {id_producto}.")
        return None

    prod = productos[id_producto]
    if codigo is not None:
        if not validar_codigo_unico(codigo, id_producto):
            print(f"❌ Error: El código '{codigo}' ya está en uso por otro producto.")
            return None
        prod["codigo"] = codigo
    if nombre is not None:
        prod["nombre"] = nombre
    if categoria is not None:
        prod["categoria"] = categoria
    if stock is not None:
        if stock < 0:
            print("❌ Error: El stock no puede ser negativo.")
            return None
        prod["stock"] = stock
    if precio is not None:
        if precio <= 0:
            print("❌ Error: El precio debe ser mayor que 0.")
            return None
        prod["precio"] = round(precio, 2)
    if descripcion is not None:
        prod["descripcion"] = descripcion

    print(f"✅ Producto ID {id_producto} actualizado correctamente.")
    return prod

def eliminar_producto(id_producto):
    if id_producto in productos:
        nombre = productos[id_producto]["nombre"]
        del productos[id_producto]
        print(f"✅ Producto '{nombre}' (ID {id_producto}) eliminado.")
        return True
    else:
        print(f"❌ Error: No existe producto con ID {id_producto}.")
        return False

def listar_productos():
    if not productos:
        print("\n📦 No hay productos registrados.")
        return

    print("\n" + "=" * 55)
    print("LISTA DE PRODUCTOS")
    print("=" * 55)
    for prod in productos.values():
        print(f"ID: {prod['id']} | Código: {prod['codigo']}")
        print(f"  Nombre: {prod['nombre']}")
        print(f"  Categoría: {prod['categoria']}")
        print(f"  Stock: {prod['stock']} unidades")
        print(f"  Precio: ${prod['precio']:.2f}")
        print(f"  Descripción: {prod['descripcion']}")
        print("-" * 45)

def buscar_por_categoria(categoria):
    resultados = [p for p in productos.values() if p["categoria"].lower() == categoria.lower()]
    if resultados:
        print(f"\n🔍 Productos en categoría '{categoria}':")
        for prod in resultados:
            print(f"  ID {prod['id']} - {prod['nombre']} (Código: {prod['codigo']}) | Stock: {prod['stock']} | ${prod['precio']:.2f}")
    else:
        print(f"❌ No se encontraron productos en la categoría '{categoria}'.")
    return resultados

# ==================== PRECARGA DE 10 PRODUCTOS CON DICCIONARIOS ====================

def precargar_productos():
    # Ahora definimos los productos como una lista de diccionarios, no de tuplas
    datos = [
        {"codigo": "LEC001", "nombre": "Leche Entera", "categoria": "Lácteos", "stock": 50, "precio": 1.25, "descripcion": "Leche entera pasteurizada, 1 litro"},
        {"codigo": "PAN001", "nombre": "Pan Integral", "categoria": "Panadería", "stock": 30, "precio": 0.85, "descripcion": "Pan integral artesanal, 500 gramos"},
        {"codigo": "FRU001", "nombre": "Manzanas Rojas", "categoria": "Frutas", "stock": 25, "precio": 2.50, "descripcion": "Manzanas rojas frescas, 1 kg"},
        {"codigo": "GRA001", "nombre": "Arroz Largo", "categoria": "Granos", "stock": 100, "precio": 1.10, "descripcion": "Arroz blanco de grano largo, 1 kg"},
        {"codigo": "CAR001", "nombre": "Pechuga de Pollo", "categoria": "Carnes", "stock": 15, "precio": 4.50, "descripcion": "Pechuga de pollo sin hueso, 1 kg"},
        {"codigo": "LAC002", "nombre": "Yogur Natural", "categoria": "Lácteos", "stock": 40, "precio": 0.95, "descripcion": "Yogur natural sin azúcar, 1 litro"},
        {"codigo": "VER001", "nombre": "Tomates", "categoria": "Verduras", "stock": 20, "precio": 1.80, "descripcion": "Tomates perita, 1 kg"},
        {"codigo": "BEB001", "nombre": "Café Molido", "categoria": "Bebidas", "stock": 35, "precio": 3.20, "descripcion": "Café tostado molido, 500 gramos"},
        {"codigo": "SNK001", "nombre": "Galletas de Avena", "categoria": "Snacks", "stock": 45, "precio": 1.50, "descripcion": "Galletas integrales de avena, 200 gramos"},
        {"codigo": "LIM001", "nombre": "Detergente Líquido", "categoria": "Limpieza", "stock": 60, "precio": 2.80, "descripcion": "Detergente para ropa, 1 litro"}
    ]
    for prod in datos:
        crear_producto(prod["codigo"], prod["nombre"], prod["categoria"], prod["stock"], prod["precio"], prod["descripcion"])

# ==================== MENÚ PRINCIPAL ====================

def mostrar_menu():
    print("\n" + "=" * 40)
    print("   SISTEMA DE GESTIÓN DE PRODUCTOS")
    print("=" * 40)
    print("1. Crear producto")
    print("2. Leer producto por ID")
    print("3. Leer producto por código")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Listar todos los productos")
    print("7. Buscar por categoría")
    print("8. Salir")
    print("=" * 40)

def main():
    precargar_productos()  # Cargamos los 10 productos de ejemplo
    while True:
        mostrar_menu()
        opcion = input("\nElige una opción (1-8): ").strip()

        if opcion == "1":
            print("\n--- CREAR NUEVO PRODUCTO ---")
            codigo = input("Código único (ej: LEC002): ").strip()
            nombre = input("Nombre: ").strip()
            categoria = input("Categoría: ").strip()
            try:
                stock = int(input("Stock: "))
                precio = float(input("Precio: "))
            except ValueError:
                print("❌ Error: Stock y precio deben ser números.")
                continue
            descripcion = input("Descripción breve: ").strip()
            crear_producto(codigo, nombre, categoria, stock, precio, descripcion)

        elif opcion == "2":
            print("\n--- LEER PRODUCTO POR ID ---")
            try:
                id_prod = int(input("ID del producto: "))
            except ValueError:
                print("❌ Error: El ID debe ser un número entero.")
                continue
            prod = leer_producto_por_id(id_prod)
            if prod:
                print("\nDatos del producto:")
                print(f"  ID: {prod['id']}")
                print(f"  Código: {prod['codigo']}")
                print(f"  Nombre: {prod['nombre']}")
                print(f"  Categoría: {prod['categoria']}")
                print(f"  Stock: {prod['stock']}")
                print(f"  Precio: ${prod['precio']:.2f}")
                print(f"  Descripción: {prod['descripcion']}")

        elif opcion == "3":
            print("\n--- LEER PRODUCTO POR CÓDIGO ---")
            codigo = input("Código del producto: ").strip()
            prod = leer_producto_por_codigo(codigo)
            if prod:
                print("\nDatos del producto:")
                print(f"  ID: {prod['id']}")
                print(f"  Código: {prod['codigo']}")
                print(f"  Nombre: {prod['nombre']}")
                print(f"  Categoría: {prod['categoria']}")
                print(f"  Stock: {prod['stock']}")
                print(f"  Precio: ${prod['precio']:.2f}")
                print(f"  Descripción: {prod['descripcion']}")

        elif opcion == "4":
            print("\n--- ACTUALIZAR PRODUCTO ---")
            try:
                id_prod = int(input("ID del producto a actualizar: "))
            except ValueError:
                print("❌ Error: ID inválido.")
                continue
            if id_prod not in productos:
                print(f"❌ Error: No existe producto con ID {id_prod}.")
                continue
            print("Deja en blanco los campos que no quieras modificar.")
            codigo = input("Nuevo código (Enter para omitir): ").strip() or None
            nombre = input("Nuevo nombre (Enter para omitir): ").strip() or None
            categoria = input("Nueva categoría (Enter para omitir): ").strip() or None
            stock_input = input("Nuevo stock (Enter para omitir): ").strip()
            stock = int(stock_input) if stock_input else None
            precio_input = input("Nuevo precio (Enter para omitir): ").strip()
            precio = float(precio_input) if precio_input else None
            descripcion = input("Nueva descripción (Enter para omitir): ").strip() or None

            actualizar_producto(id_prod, codigo, nombre, categoria, stock, precio, descripcion)

        elif opcion == "5":
            print("\n--- ELIMINAR PRODUCTO ---")
            try:
                id_prod = int(input("ID del producto a eliminar: "))
            except ValueError:
                print("❌ Error: ID inválido.")
                continue
            eliminar_producto(id_prod)

        elif opcion == "6":
            listar_productos()

        elif opcion == "7":
            print("\n--- BUSCAR POR CATEGORÍA ---")
            categoria = input("Categoría a buscar: ").strip()
            buscar_por_categoria(categoria)

        elif opcion == "8":
            print("\n👋 ¡Hasta luego!")
            break

        else:
            print("❌ Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()