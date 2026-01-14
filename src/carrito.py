class ItemCarrito:
    
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad
    
    def subtotal(self):
        return self.producto.precio * self.cantidad
    
    def __str__(self):
        return f'Producto: {self.producto.nombre} | Cantidad: {self.cantidad} | Precio: ${self.producto.precio} | Subtotal: ${self.subtotal()}'


class Carrito:
   
    def __init__(self):
        self.items = []
        
    def agregar_item(self, producto, cantidad):
        if cantidad <= 0:
            raise ValueError('La cantidad debe ser mayor a 0')
        item = ItemCarrito(producto, cantidad)
        self.items.append(item)
    
    def listar_items(self):
        return self.items
  
    def calcular_total(self):
        total = 0
        for item in self.items:
            total += item.subtotal()
        return total
        
    def vaciar(self):
        self.items.clear()
        print('\n¡Los productos han salido eliminados del carrito!')
    
    
    def __str__(self):
        if len(self.items) == 0:
            return f"El carrito está vacío"

        resultado = "\n-- Carrito de compras --\n"
        for item in self.items:
            resultado += f"{item}\n"
        resultado += f"\nTotal a pagar: ${self.calcular_total()}"
        return resultado
