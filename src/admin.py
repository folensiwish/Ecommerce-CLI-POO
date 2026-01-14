from usuario import Usuario

class Admin(Usuario):

    def __init__(self, nombre_usuario, catalogo):
        super().__init__(nombre_usuario)
        self.catalogo = catalogo

    def listar_productos(self):
        return self.catalogo.listar_productos()

    def crear_producto(self, producto):
        self.catalogo.agregar_producto(producto)

    def actualizar_producto(self,id,nombre,categoria,precio):
        producto = self.catalogo.buscar_por_id(id)
        producto.nombre = nombre
        producto.categoria = categoria
        producto.precio= precio

    def eliminar_producto(self,id_prod):
        return self.catalogo.eliminar_producto(id_prod)

    def guardar_catalogo(self,nombre_archivo="catalogo.txt"):
        return self.catalogo.guardar_en_archivo(nombre_archivo)
    
