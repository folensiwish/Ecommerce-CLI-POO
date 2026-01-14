from producto import Producto
from catalogo import Catalogo
from admin import Admin
from cliente import Cliente
from error import ProductoNoEncontradoError


list_productos = [
    Producto(1, "Mouse Razor x86", "Tecnologia", 85000),
    Producto(2, "Parlante mlab xt", "Tecnologia", 73000),
    Producto(3, "Teclado redragon", "Tecnologia", 20000),
    Producto(4, "Audifonos JBL 204", "Tecnologia", 35000),
    Producto(5, "Pantalla HP m24", "Tecnologia", 125000),
]


usuario = int(input('1) Admin \n2) Cliente\nIngrese una opcion: '))
if usuario == 2:
    nombre_cliente = input('Ingrese su nombre: ')
else:
    nombre_cliente = 'Cliente'

catalogo = Catalogo(list_productos)
admin = Admin("Administrador",catalogo)
cli = Cliente(nombre_cliente,catalogo)


def menu_principal():
    while True:
        
        if usuario == 1:
            try:
                menu = int(input(f'\nBienvenido/a a tu Ecommerce\n\nMenu\n\n1) Listar productos\n2) Crear producto nuevo\n3) Actualizar producto\n4) Eliminar producto\n5) Guardar catálogo en archivo\n0) Salir\n\nIngrese una opcion: '))
                if menu == 1:
                    print('-- Lista de productos --')
                    print('ID | Nombre producto | Categoria | Precio')
                    print('-'*40)
                    for i in admin.listar_productos():
                        print(i)

                elif menu == 2:
                    print('-- Crear un producto --')
                    id = int(input('Ingrese el id del nuevo producto: '))
                    nombre = input('Ingrese el nombre del producto nuevo: ')
                    categoria = input('Ingrese la categoria del producto nuevo: ')
                    precio = int(input('Ingrese el precio del producto nuevo: '))
                    prod = Producto(id,nombre,categoria,precio)
                    admin.crear_producto(prod)

                elif menu ==3:

                    print('-- Actualizar un producto --')
                    id_producto = int(input('ID producto: '))
                    nombre_nuevo = input('Nuevo nombre producto: ')
                    categoria_nueva = input('Nueva categoria producto: ')
                    precio_nuevo = int(input('Nuevo precio: '))
                    admin.actualizar_producto(id_producto,nombre_nuevo,categoria_nueva,precio_nuevo)

                elif menu ==4:

                    print('-- Eliminar producto --')
                    try:
                        id_prod = int(input('Ingresa el ID del producto a eliminar: '))
                        if admin.eliminar_producto(id_prod) == id_prod:
                            print(f'\nID: {id_prod} fue eliminado del catalogo')
                    except ProductoNoEncontradoError as error:
                        print(f'\n{error}')
        
                elif menu ==5:

                    admin.catalogo.guardar_en_archivo()

                elif menu == 0:
                    print("¡Sesion Cerrada!")
                    break 
                else:
                    print("Opción no válida.")
            except ValueError:
                print('Debes ingresar un numero valido')
#--------------------------------------------------------------CLIENTE-------------------------------------------------------------       
        elif usuario == 2:
            try:            
                menu = int(input(f'\nBienvenido/a a tu Ecommerce\n\nMenu\n\n1) Ver catálogo de productos\n2) Buscar productos\n3) Agregar producto al carrito\n4) Ver carrito y total\n5) Confirmar compra\n0) Salir\n\nIngrese una opcion: '))

                if menu == 1:
                    print('-- Lista de productos --')
                    print('ID | Nombre producto | Categoria | Precio')
                    print('-'*40)
                    for i in cli.ver_catalogo():
                        print(i)

                elif menu ==2:
                    print('-- Buscar producto --')
                    try:
                        prod_id = int(input('ID del producto que quieres encontrar: '))
                        print('\n-- Producto encontrado --')
                        print('ID | Nombre producto | Categoria | Precio')
                        print('-'*40)
                        print(cli.buscar_productos(prod_id))
                    except ProductoNoEncontradoError as error:
                        print(f'\n{error}')
                    except ValueError:
                        print('Debes ingresar un numero entero mayor a 0')

                elif menu ==3:
                    print('-- Agregar productos al carrito --')
                    try:
                        producto_id = int(input('ID del producto para añadir al carrito: '))
                        cantidad = int(input('Ingrese la cantidad del producto: '))
                        cli.agregar_productos_carrito(producto_id,cantidad)
                    except ValueError:
                        print('Debes ingresar un numero y que sea mayor a 0')

                elif menu==4:
                    print(cli.carrito)

                elif menu== 5:
                    if len(cli.carrito.items) == 0:
                        print('Carrito vacio, no se puede confimar la compra')
                    else:
                        confirmar= input('¿Confirmar la compra? si/no: ') 
                        if confirmar.lower() == 'si':
                            total = cli.confirmar_compra()
                            print('¡Compra confirmada!')
                            print(f'Total a pagar: ${total}')
                            print('La orden a sido registrada en ordenes.txt')
                        else:
                            print('Compra cancelada')

                elif menu == 0:
                    print("¡Gracias por tu visita, vuelva pronto!")
                    break 
                else:
                    print("Opción no válida.")

            except ValueError:
                print('Debes ingresar un numero valido')

menu_principal()      