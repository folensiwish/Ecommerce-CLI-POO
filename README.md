Ecommerce CLI - Programación Orientada a Objetos (POO)
Este proyecto es un sistema de gestión de ventas por consola desarrollado en Python. Ha sido diseñado bajo el paradigma de Programación Orientada a Objetos (POO) para simular un flujo real de comercio electrónico, permitiendo la gestión de productos de tecnología y la realización de compras automatizadas.

🚀 Características Principales
El sistema se divide en dos módulos principales según el rol del usuario:

1. Módulo Administrador (Gestión de Inventario)
Permite realizar el mantenimiento completo del catálogo de productos:

CRUD de Productos: Crear, leer, actualizar y eliminar artículos del inventario.

Persistencia de Datos: Exportación del catálogo actual a un archivo plano (catalogo.txt) para respaldo de información.

2. Módulo Cliente (Experiencia de Compra)
Enfocado en la interacción del usuario final con el catálogo:

Navegación y Búsqueda: Visualización completa del catálogo o búsqueda específica por ID.

Gestión de Carrito: Añadir productos especificando cantidades, con cálculo automático de subtotales y total general.

Finalización de Compra: Generación de una orden de compra detallada con fecha y hora, exportada automáticamente a ordenes.txt.

🛠️ Tecnologías y Conceptos de Programación Aplicados
Para lograr un sistema robusto y escalable, se utilizaron las siguientes técnicas de POO:

Herencia Simple: Se utilizó una clase base Usuario de la cual heredan Admin y Cliente, compartiendo atributos comunes pero especializando sus comportamientos.

Composición y Colaboración:

La clase Catalogo contiene y gestiona una colección de objetos Producto.

La clase Carrito se compone de objetos ItemCarrito para manejar la relación entre productos y cantidades.

Encapsulamiento: Uso de decoradores @property y @setter en la clase Producto para proteger la integridad de los datos (ej: impedir precios negativos).

Manejo de Excepciones Personalizadas: Implementación de la clase ProductoNoEncontradoError para gestionar errores específicos de búsqueda de forma controlada.

Manejo de Archivos (I/O): Lectura y escritura de archivos .txt para la persistencia de órdenes y catálogos.

📁 Estructura del Proyecto
El código está modularizado para facilitar su mantenimiento:

tienda.py: Punto de entrada de la aplicación y lógica de menús.

producto.py: Definición del modelo de datos para los artículos.

usuario.py, admin.py, cliente.py: Lógica de roles y permisos.

catalogo.py: Motor de gestión del inventario.

carrito.py: Lógica de cálculo y almacenamiento temporal de compras.

error.py: Definición de excepciones personalizadas.

💻 Cómo ejecutar el programa
Requisitos: Tener instalado Python 

Preparación: Asegúrate de que todos los archivos .py se encuentren en el mismo directorio.

Ejecución: Abre tu terminal y ubícate en la carpeta del proyecto, luego ejecuta:

python tienda.py

Uso:

Selecciona el perfil (1 para Admin, 2 para Cliente).

Sigue las instrucciones del menú interactivo para navegar por las funciones.
