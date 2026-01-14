from usuario import Usuario
from carrito import Carrito
from datetime import datetime

class Cliente(Usuario):

    def __init__(self, nombre_usuario,catalogo):
        super().__init__(nombre_usuario)
        self.carrito = Carrito()
        self.catalogo = catalogo
    
    
    def ver_catalogo(self):
        return self.catalogo.listar_productos()

    def buscar_productos(self,id):
        return self.catalogo.buscar_por_id(id)

    def agregar_productos_carrito(self,id_prod,cantidad):
        producto = self.catalogo.buscar_por_id(id_prod)
        self.carrito.agregar_item(producto,cantidad)
        print(f'{producto.nombre} agregado al carrito exitosamente')

    def ver_carrito(self):
        return self.carrito.listar_items()
    
    def confirmar_compra(self):
        try:
            with open("ordenes.txt",'a') as archivo:
                fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                archivo.write(f'Orden de compra - {fecha}\n')
                archivo.write(f'Cliente: {self.nombre_usuario}\n')

                for item in self.carrito.listar_items():
                    archivo.write(f'{item}\n')

                total = self.carrito.calcular_total()
                archivo.write(f'Total: ${total}\n')

            total = self.carrito.calcular_total()

            self.carrito.vaciar()

            return total
        except Exception as error:
            print(f'Error al guarda la orden: {error}')