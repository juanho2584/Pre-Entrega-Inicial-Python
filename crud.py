from datos import cargar_datos, guardar_datos

def obtener_siguiente_id():
    productos = cargar_datos()
    if not productos:
        return 1
    return max(productos.keys()) + 1

def validar_codigo_unico(codigo, id_actual=None):
    productos = cargar_datos()
    for prod in productos.values():
        if prod["codigo"] == codigo and (id_actual is None or prod["id"] != id_actual):
            return False
    return True

def crear_producto(codigo, nombre, categoria, stock, precio, descripcion):
    productos = cargar_datos()
    
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

    nuevo_id = obtener_siguiente_id()
    producto = {
        "id": nuevo_id,
        "codigo": codigo,
        "nombre": nombre,
        "categoria": categoria,
        "stock": stock,
        "precio": round(precio, 2),
        "descripcion": descripcion
    }
    productos[nuevo_id] = producto
    guardar_datos(productos)
    print(f"✅ Producto '{nombre}' (Código: {codigo}) creado con ID {nuevo_id}.")
    return producto

def leer_producto_por_id(id_producto):
    productos = cargar_datos()
    if id_producto in productos:
        return productos[id_producto]
    else:
        print(f"❌ Error: No existe producto con ID {id_producto}.")
        return None

def leer_producto_por_codigo(codigo):
    productos = cargar_datos()
    for prod in productos.values():
        if prod["codigo"] == codigo:
            return prod
    print(f"❌ Error: No existe producto con código '{codigo}'.")
    return None

def actualizar_producto(id_producto, codigo=None, nombre=None, categoria=None, stock=None, precio=None, descripcion=None):
    productos = cargar_datos()
    
    if id_producto not in productos:
        # Ya hay un error manejado por main o lo mostramos aca si no venia validado
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

    guardar_datos(productos)
    print(f"✅ Producto ID {id_producto} actualizado correctamente.")
    return prod

def eliminar_producto(id_producto):
    productos = cargar_datos()
    if id_producto in productos:
        nombre = productos[id_producto]["nombre"]
        del productos[id_producto]
        guardar_datos(productos)
        print(f"✅ Producto '{nombre}' (ID {id_producto}) eliminado.")
        return True
    else:
        print(f"❌ Error: No existe producto con ID {id_producto}.")
        return False

def listar_productos():
    productos = cargar_datos()
    return list(productos.values())

def buscar_por_categoria(categoria):
    productos = cargar_datos()
    return [p for p in productos.values() if p["categoria"].lower() == categoria.lower()]
