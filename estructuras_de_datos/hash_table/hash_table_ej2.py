""" Ejercicio 2 de la serie de Hash Table: Sistema de inventario """

class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, id_producto, nombre, cantidad, precio):
        """ Agrega o actualiza un producto """

        if id_producto in self.productos:  # Actualizar el stock y el precio
            self.productos[id_producto]["cantidad"] += cantidad
            self.productos[id_producto]["precio"] = precio
            return
        
        # Si no esta, agregarlo

        self.productos[id_producto] = {
            "nombre": nombre,
            "cantidad": cantidad,
            "precio": precio
        }

    
    def vender_producto(self, id_producto, cantidad): 
        """Reduce la cantidad si hay suficiente stock"""

        if id_producto not in self.productos:
            print(f"El producto con ID {id_producto} no existe en el almacen. ")
            return
        
        if cantidad > self.productos[id_producto]["cantidad"]:
            print(f'No hay suficientes cantidad del producto con ID {id_producto} ({self.productos[id_producto]["nombre"]}). Solo quedan {self.productos[id_producto]["cantidad"]} ejemplares.')
            return
        
        self.productos[id_producto]["cantidad"] -= cantidad

    
    def buscar_por_nombre(self, nombre): 
        """Busca productos que contengan el nombre (búsqueda parcial)"""

        productos_encontrados = []

        for producto in self.productos.values():
            if nombre in producto["nombre"]:
                productos_encontrados.append(producto)

        if not productos_encontrados:
            print(f"No hay ningun producto que contenga {nombre} en su nombre.")
            return

        return productos_encontrados

    def productos_bajo_stock(self, minimo=5): 
        """Devuelve productos con stock menor al mínimo""" 

        if not self.productos:
            print("No hay productos en el almacen.")
            return

        productos_casi_agotados = []

        for producto in self.productos.values():
            if producto["cantidad"] <= minimo:
                productos_casi_agotados.append(producto)

        if not productos_casi_agotados:
            print(f"Todos los productos tienen cantidades superiores a {minimo}.")
            return

        return productos_casi_agotados
    

inv = Inventario() 
inv.agregar_producto(1, "Laptop", 10, 999.99) 
inv.agregar_producto(2, "Mouse", 50, 19.99) 
inv.vender_producto(1, 3) # Ahora hay 7 laptops 
print(inv.productos_bajo_stock(10)) # [Laptop: 7]
