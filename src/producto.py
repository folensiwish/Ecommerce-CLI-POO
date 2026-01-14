class Producto:

    def __init__(self, id, nombre, categoria, precio):
        self._id = id
        self._nombre = nombre
        self._categoria = categoria
        self._precio = precio
    
    @property
    def id(self):
        return self._id
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def categoria(self):
        return self._categoria
    
    @property
    def precio(self):
        return self._precio
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre
    
    @categoria.setter
    def categoria(self, nueva_categoria):
        self._categoria = nueva_categoria
    
    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self._precio = nuevo_precio
        else:
            raise ValueError("El precio debe ser mayor a 0")
        
    def __str__(self):
        return f'{self.id} | {self.nombre} | {self.categoria} | ${self.precio}'
