print("=== PROGRAMA: JERARQUÍA DE PRODUCTOS ===\n")

# Clase base Producto
class Producto:
    def __init__(self, nombre, precio, stock):
        # Inicializar atributos básicos
        # Escribe aquí tu código
        self.nombre = nombre
        self.precio = precio
        self.stock = stock        
    
    def mostrar_info(self):
        # Devolver información básica del producto
        # Escribe aquí tu código
        return f"El producto con nombre {self.nombre} cuesta {self.precio} euros y hay {self.stock} unidades"
        
    
    def hay_stock(self):
        # Verificar si hay unidades disponibles
        # Escribe aquí tu código
        if self.stock > 0:
            return f"Hay stock"
            
        else:
            return f"No hay stock"
             
        

# Clase Alimento que hereda de Producto
class Alimento(Producto):
    def __init__(self, nombre, precio, stock, fecha_caducidad):
        # Llamar al constructor de la clase padre
        Producto.__init__(self,nombre, precio, stock) #Si pongo el super.__init__ no hace falta traer el self
        # Inicializar atributo específico de Alimento
        self.fecha_caducidad = fecha_caducidad

        
    
    def mostrar_info(self):
        # Sobreescribir el método para incluir fecha de caducidad
        # Escribe aquí tu código (puedes usar super() o reimplementar)
        return f"El producto con nombre {self.nombre} cuesta {self.precio} euros y hay {self.stock} unidades y tiene como fecha de caducidad {self.fecha_caducidad}"

        
        


# Clase Electronico que hereda de Producto
class Electronico(Producto):
    def __init__(self, nombre, precio, stock, garantia):
        # Llamar al constructor de la clase padre
        # Escribe aquí tu código
        Producto.__init__(self,nombre, precio, stock)

        
        # Inicializar atributo específico de Electronico
        # Escribe aquí tu código
        self.garantia = garantia
        
    
    def mostrar_info(self):
        # Sobreescribir el método para incluir información de garantía
        # Escribe aquí tu código (puedes usar super() o reimplementar)
        return f"El producto con nombre {self.nombre} cuesta {self.precio} euros y hay {self.stock} unidades y tiene como garantia {self.garantia} años"

        


# === CREACIÓN Y PRUEBA DE INSTANCIAS ===
print("=== CREANDO PRODUCTOS ===")

# Crear una instancia de Producto genérico
# Escribe aquí tu código
producto1 = Producto("Usb 30GB",24,20)
# Crear una instancia de Alimento
# Escribe aquí tu código
alimento1 = Alimento("Yogur",1,35,"20-12-2025")

# Crear una instancia de Electronico
# Escribe aquí tu código
electronico1 = Electronico("Lavadora",60, 0,10)




print("\n=== INFORMACIÓN DE PRODUCTOS ===")

# Mostrar información del producto genérico
# Escribe aquí tu código
print(producto1.mostrar_info())

# Mostrar información del alimento
# Escribe aquí tu código
print(alimento1.mostrar_info())

# Mostrar información del electrónico
# Escribe aquí tu código
print(electronico1.mostrar_info())

print("\n=== VERIFICANDO STOCK ===")

# Verificar stock de cada producto
# Escribe aquí tu código

print(f"Del producto {producto1.nombre} {producto1.hay_stock()}")
print(f"Del producto {alimento1.nombre} {alimento1.hay_stock()}")
print(f"Del producto {electronico1.nombre} {electronico1.hay_stock()}")
