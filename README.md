# Sistema de Gestión de Productos

Proyecto de consola en Python para gestionar un inventario de productos con operaciones CRUD y almacenamiento en JSON.

## Descripción

Esta aplicación permite mantener un catálogo de productos desde la terminal mediante un menú interactivo. Los usuarios pueden crear nuevos productos, consultar información, actualizar datos existentes y eliminar productos.

El sistema trabaja con un archivo local `productos.json`, por lo que los cambios se guardan entre ejecuciones.

## Estructura del proyecto

- `main.py`: punto de entrada principal del programa. Contiene los menús de interacción con el usuario y realiza las llamadas a las funciones del CRUD.
- `crud.py`: lógica de negocio para crear, leer, actualizar y eliminar productos. También valida códigos únicos, stock y precio.
- `datos.py`: lectura y escritura de datos en el archivo JSON. Convierte las claves del JSON entre `str` e `int` para trabajar internamente con IDs numéricos.
- `config.py`: configuración básica del proyecto, incluyendo la ruta absoluta de `productos.json`.
- `productos.json`: almacena los productos registrados en formato JSON.

## Modelo de datos

Cada producto se representa como un diccionario con los siguientes campos:

- `id` (int): identificador único generado automáticamente.
- `codigo` (str): código único de producto (por ejemplo, `LEC002`).
- `nombre` (str): nombre del producto.
- `categoria` (str): categoría del producto.
- `stock` (int): cantidad de unidades disponibles.
- `precio` (float): precio unitario del producto.
- `descripcion` (str): descripción breve del producto.

## Requisitos

- Python 3.x

## Instalación

1. Descargar o clonar el repositorio en tu equipo.
2. Abrir una terminal en la carpeta del proyecto.
3. Si utilizas un entorno virtual, créalo e instálalo (opcional):

```bash
python -m venv venv
venv\Scripts\activate
```

No hay dependencias externas; el proyecto usa únicamente la biblioteca estándar de Python.

## Uso

Ejecuta el siguiente comando desde la carpeta del proyecto:

```bash
python main.py
```

A continuación se desplegará el menú principal con las siguientes opciones:

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

## Ejemplos de flujo

1. Crear un producto

- Código: `LEC002`
- Nombre: `Leche entera`
- Categoría: `Lácteos`
- Stock: `20`
- Precio: `150.50`
- Descripción: `Leche fresca de 1 litro`

2. Consultar por categoría

- Buscar categoría: `Lácteos`

3. Actualizar un producto

- Ingresar ID del producto
- Dejar en blanco los campos que no se deseen cambiar

4. Eliminar un producto

- Ingresar ID del producto a eliminar

## Validaciones incluidas

- Código, nombre y categoría son obligatorios al crear un producto.
- El stock no puede ser negativo.
- El precio debe ser mayor que 0.
- El código debe ser único entre productos.
- Al actualizar, se permite dejar campos en blanco para mantener el valor anterior.
- Las búsquedas distinguen entre ID y código, y la búsqueda por categoría no distingue mayúsculas/minúsculas.

## Detalles técnicos

- `datos.py` maneja la persistencia en `productos.json`.
- `crud.py` valida entradas y administra la lógica CRUD.
- `config.py` define la ruta absoluta de `productos.json`, evitando problemas si el script se ejecuta desde otra carpeta.
- Las claves del JSON se guardan como cadenas, pero el sistema convierte esas claves a enteros al cargarlas.

## Producido

- Producido por Juan Manuel Pinto

