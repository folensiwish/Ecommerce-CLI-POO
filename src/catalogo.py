from error import ProductoNoEncontradoError

class Catalogo:
    def __init__(self,producto=[]):
        self.productos = producto
        
    def listar_productos(self):
        return self.productos
    
    def agregar_producto(self, producto):
        self.productos.append(producto)

    def buscar_por_id(self, id):
        for i in self.productos:
            if i.id == id:
                return i
        raise ProductoNoEncontradoError(id)

    def eliminar_producto(self,id_prod):
        for i in self.productos:
            if i.id == id_prod:
                self.productos.remove(i)
                return True
        raise ProductoNoEncontradoError(id_prod)
    
    def guardar_en_archivo(self, nombre_archivo="catalogo.txt"):
        try:
            with open(nombre_archivo, 'w') as archivo:
                for prod in self.productos:
                    guardar = f'{prod.id},{prod.nombre},{prod.categoria},{prod.precio}\n'
                    archivo.write(guardar)
                print('El catalogo fue guardado en el archivo exitosamente')
        except Exception as error:
            print(f'Error al guardar el archivo: {error}')
