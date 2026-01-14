class ProductoNoEncontradoError(Exception):
    def __init__(self, id_producto):
        self.id_producto = id_producto

    def __str__(self):
        return f"No existe un producto con ID {self.id_producto}"
