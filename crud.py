import sqlite3
from db import obtener_conexion

def validar_codigo_unico(codigo, id_actual=None):
    conn = obtener_conexion()
    cursor = conn.cursor()
    try:
        if id_actual is None:
            cursor.execute("SELECT COUNT(*) FROM productos WHERE codigo = ?", (codigo,))
        else:
            cursor.execute("SELECT COUNT(*) FROM productos WHERE codigo = ? AND id != ?", (codigo, id_actual))
        
        count = cursor.fetchone()[0]
        return count == 0
    except sqlite3.Error as e:
        print(f"❌ Error al validar código único: {e}")
        return False
    finally:
        conn.close()

def crear_producto(codigo, nombre, categoria, stock, precio, descripcion):
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

    conn = obtener_conexion()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            INSERT INTO productos (codigo, nombre, categoria, stock, precio, descripcion)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (codigo, nombre, categoria, stock, round(precio, 2), descripcion)
        )
        conn.commit()
        nuevo_id = cursor.lastrowid
        
        # Obtener el producto recién creado para retornarlo
        cursor.execute("SELECT * FROM productos WHERE id = ?", (nuevo_id,))
        producto = dict(cursor.fetchone())
        print(f"✅ Producto '{nombre}' (Código: {codigo}) creado con ID {nuevo_id}.")
        return producto
    except sqlite3.Error as e:
        print(f"❌ Error al crear producto: {e}")
        return None
    finally:
        conn.close()

def leer_producto_por_id(id_producto):
    conn = obtener_conexion()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM productos WHERE id = ?", (id_producto,))
        row = cursor.fetchone()
        if row:
            return dict(row)
        else:
            print(f"❌ Error: No existe producto con ID {id_producto}.")
            return None
    except sqlite3.Error as e:
        print(f"❌ Error al buscar producto por ID: {e}")
        return None
    finally:
        conn.close()

def leer_producto_por_codigo(codigo):
    conn = obtener_conexion()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM productos WHERE codigo = ?", (codigo,))
        row = cursor.fetchone()
        if row:
            return dict(row)
        else:
            print(f"❌ Error: No existe producto con código '{codigo}'.")
            return None
    except sqlite3.Error as e:
        print(f"❌ Error al buscar producto por código: {e}")
        return None
    finally:
        conn.close()

def actualizar_producto(id_producto, codigo=None, nombre=None, categoria=None, stock=None, precio=None, descripcion=None):
    # Verificar primero si el producto existe
    prod_actual = leer_producto_por_id(id_producto)
    if not prod_actual:
        return None

    conn = obtener_conexion()
    cursor = conn.cursor()
    try:
        fields = []
        values = []

        if codigo is not None:
            if not validar_codigo_unico(codigo, id_producto):
                print(f"❌ Error: El código '{codigo}' ya está en uso por otro producto.")
                return None
            fields.append("codigo = ?")
            values.append(codigo)

        if nombre is not None:
            fields.append("nombre = ?")
            values.append(nombre)

        if categoria is not None:
            fields.append("categoria = ?")
            values.append(categoria)

        if stock is not None:
            if stock < 0:
                print("❌ Error: El stock no puede ser negativo.")
                return None
            fields.append("stock = ?")
            values.append(stock)

        if precio is not None:
            if precio <= 0:
                print("❌ Error: El precio debe ser mayor que 0.")
                return None
            fields.append("precio = ?")
            values.append(round(precio, 2))

        if descripcion is not None:
            fields.append("descripcion = ?")
            values.append(descripcion)

        if not fields:
            # No hay campos para actualizar
            return prod_actual

        values.append(id_producto)
        query = f"UPDATE productos SET {', '.join(fields)} WHERE id = ?"
        cursor.execute(query, values)
        conn.commit()

        # Retornar el producto actualizado
        cursor.execute("SELECT * FROM productos WHERE id = ?", (id_producto,))
        prod_actualizado = dict(cursor.fetchone())
        print(f"✅ Producto ID {id_producto} actualizado correctamente.")
        return prod_actualizado
    except sqlite3.Error as e:
        print(f"❌ Error al actualizar producto: {e}")
        return None
    finally:
        conn.close()

def eliminar_producto(id_producto):
    conn = obtener_conexion()
    cursor = conn.cursor()
    try:
        # Primero buscar el nombre para el mensaje de éxito
        cursor.execute("SELECT nombre FROM productos WHERE id = ?", (id_producto,))
        row = cursor.fetchone()
        if not row:
            print(f"❌ Error: No existe producto con ID {id_producto}.")
            return False
        
        nombre = row['nombre']
        cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
        conn.commit()
        print(f"✅ Producto '{nombre}' (ID {id_producto}) eliminado.")
        return True
    except sqlite3.Error as e:
        print(f"❌ Error al eliminar producto: {e}")
        return False
    finally:
        conn.close()

def listar_productos():
    conn = obtener_conexion()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM productos")
        rows = cursor.fetchall()
        return [dict(r) for r in rows]
    except sqlite3.Error as e:
        print(f"❌ Error al listar productos: {e}")
        return []
    finally:
        conn.close()

def buscar_por_categoria(categoria):
    conn = obtener_conexion()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM productos WHERE LOWER(categoria) = LOWER(?)", (categoria,))
        rows = cursor.fetchall()
        return [dict(r) for r in rows]
    except sqlite3.Error as e:
        print(f"❌ Error al buscar por categoría: {e}")
        return []
    finally:
        conn.close()
