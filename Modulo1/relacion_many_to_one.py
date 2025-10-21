print("=== EJERCICIO: RELACIÓN HABITACIONES-HOTEL ===\n")

# 1. Crear la clase Hotel con los atributos: id, nombre, direccion, estrellas
class Hotel:
    def __init__(self, id, nombre, direccion, estrellas):
        # Escribe aquí tu código
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.estrellas = estrellas

# 2. Crear la clase Habitacion con los atributos: id, numero, tipo, precio, hotel
class Habitacion:
    def __init__(self, id, numero, tipo, precio, hotel):
        # Escribe aquí tu código
        self.id = id
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.hotel = hotel

print("=== CREANDO OBJETOS ===")

# 3. Crear un hotel con id: 1, nombre: Hotel Carbonero, dirección: Plaza Parus Mayor 123, estrellas: 4
hotel1 = Hotel(1,"Hotel Carbonero", "Plaza Parus Mayor 123", 4)


# 4. Crear tres habitaciones:
# - id: 1, número: 101, tipo: Individual, precio: 80, hotel: Hotel Carbonero
habitacion1 = Habitacion(1, 101, "Individual", 80, "Hotel Carbonero")
habitacion2 = Habitacion(2, 102, "Doble", 120, "Hotel Carbonero")
habitacion3 = Habitacion(3, 103, "Suite", 200, "Hotel Carbonero")


print("=== VERIFICANDO RELACIÓN ===")

# 5. Imprimir información del hotel y sus habitaciones
# Hay que mostrar:
# - Nombre del hotel y sus estrellas
print(f"El hotel {hotel1.nombre} tiene {hotel1.estrellas} estrellas")

print("\n=== RESULTADO FINAL ===")
# 7. Mostrar un mensaje confirmando la relación many-to-one
print(f"La habitación {habitacion1.numero}, la habitacion {habitacion2.numero} y la {habitacion3.numero} pertenece al hotel: {hotel1.nombre}")

