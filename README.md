# Sistema de Gestión de Productos (con SQLite)

Proyecto de consola en Python para gestionar un inventario de productos con operaciones CRUD y almacenamiento en una base de datos relacional local SQLite.

## Descripción

Esta aplicación permite mantener un catálogo de productos desde la terminal mediante un menú interactivo. Cuenta con un sistema de autenticación de usuarios y permite crear, consultar, actualizar y eliminar productos.

El sistema trabaja con una base de datos local SQLite (`inventario.db`), asegurando la integridad referencial, consistencia de datos y persistencia entre ejecuciones.

## Estructura del proyecto

- `main.py`: punto de entrada principal del programa. Gestiona la inicialización de la base de datos, inicio de sesión, menús de interacción y las funciones del CRUD.
- `auth.py`: lógica de autenticación de usuarios. Administra el registro, inicio de sesión y límites de intentos para acceder al sistema interactuando directamente con la base de datos.
- `crud.py`: lógica de negocio para crear, leer, actualizar y eliminar productos. Ejecuta consultas parametrizadas en SQLite y valida stock, precio y códigos únicos.
- `db.py`: inicialización del esquema de base de datos relacional y funciones helper para la conexión.
- `config.py`: configuración básica del proyecto, definiendo la ruta absoluta de la base de datos `inventario.db`.
- `inventario.db`: base de datos SQLite autogenerada al iniciar la aplicación.

## Modelo de datos (Base de Datos)

### Tabla `usuarios`
- `username` (TEXT, Primary Key): identificador único del usuario (mínimo 3 caracteres).
- `password` (TEXT): contraseña del usuario (mínimo 4 caracteres).

### Tabla `productos`
- `id` (INTEGER, Primary Key Autoincrement): identificador único generado automáticamente.
- `codigo` (TEXT, Unique): código único de producto (por ejemplo, `LEC002`).
- `nombre` (TEXT): nombre del producto.
- `categoria` (TEXT): categoría del producto.
- `stock` (INTEGER): cantidad de unidades disponibles (no puede ser negativo).
- `precio` (REAL): precio unitario del producto (debe ser mayor que 0).
- `descripcion` (TEXT): descripción breve del producto.

## Requisitos

- Python 3.7 o superior

## Instalación

1. Descargar o clonar el repositorio en tu equipo.
2. Abrir una terminal en la carpeta del proyecto.
3. Si utilizas un entorno virtual, créalo e instálalo (opcional):

```bash
python -m venv venv
venv\Scripts\activate
```

No hay dependencias externas adicionales; el proyecto usa únicamente `sqlite3`, el cual viene integrado en la biblioteca estándar de Python.

## Uso

Para asegurar la correcta visualización de emojis y formato de caracteres especiales en la terminal (especialmente en Windows), ejecuta el siguiente comando:

```bash
python -X utf8 main.py
```

Al iniciar, el sistema te presentará el menú de control de acceso:
1. Iniciar sesión
2. Registrarse
3. Salir del sistema

Si es la primera vez que se ejecuta, debes registrar un usuario en la opción 2 y luego iniciar sesión (cuenta con una seguridad de máximo 3 intentos fallidos consecutivos).

Una vez autenticado exitosamente, se desplegará el menú principal de productos con las siguientes opciones:

1. Crear producto
2. Mostrar productos
3. Actualizar producto
4. Eliminar producto
5. Salir

### Submenú de visualización

Dentro de "Mostrar productos" se puede elegir:
- Ver producto por código
- Ver producto por ID
- Ver productos por categoría
- Ver todos los productos

## Validaciones incluidas

- Validación de usuario (mín. 3 caracteres) y contraseña (mín. 4 caracteres) al registrarse.
- Bloqueo por seguridad después de 3 intentos de inicio de sesión fallidos.
- Código, nombre y categoría son obligatorios al crear un producto.
- El stock no puede ser negativo.
- El precio debe ser mayor que 0.
- El código del producto debe ser único.
- Al actualizar, se permite dejar campos en blanco para mantener el valor anterior.
- Las búsquedas por categoría no distinguen entre mayúsculas y minúsculas.

## Producido

- Producido por Juan Manuel Pinto
