print("=== EJERCICIO: RELACIÓN CARPETA-ARCHIVOS ===\n")

# 1. Crear la clase Carpeta con los atributos: id, nombre, fecha_creacion
# El atributo 'archivos' debe inicializarse como una lista vacía
class Carpeta:
    def __init__(self, id, nombre, fecha_creacion):
        self.id = id
        self.nombre = nombre
        self.fecha_creacion = fecha_creacion
        self.archivos = []

# 2. Crear la clase Archivo con los atributos: id, nombre, extension, tamaño, carpeta_id
class Archivo:
    def __init__(self, id, nombre, extension, tamaño, carpeta_id):
        self.id = id
        self.nombre = nombre
        self.extension = extension
        self.tamaño = tamaño
        self.carpeta_id = carpeta_id

print("=== CREANDO OBJETOS ===")

# 3. Crear una carpeta con id: 1, nombre: Proyecto Aviberico, fecha de creación: 2025-01-15
carpeta1 = Carpeta(1,"Proyecto Aviberico","2025-01-15")

# 4. Crear tres archivos:
archivo1 = Archivo(1,"main","py",1024,1)
archivo2 = Archivo(2,"config","json",512,1)
archivo3 = Archivo(3,"readme","md",256,1)


print("=== ESTABLECIENDO RELACIÓN ===")

# 5. Agregar los archivos a la carpeta (relación one-to-many)
carpeta1.archivos.append(archivo1)
carpeta1.archivos.append(archivo2)
carpeta1.archivos.append(archivo3)



print("=== VERIFICANDO RELACIÓN ===")

# 6. Imprimir información de la carpeta y sus archivos
# Hay que mostrar:
# - Nombre de la carpeta
print(f"Nombre de la carpeta: {carpeta1.nombre}")
# - Número total de archivos
print(f"El numero de archivos es de: {len(carpeta1.archivos)}")
print(f"Fecha de creacion: {carpeta1.fecha_creacion}")
# - Lista de archivos con sus detalles
for archivo in carpeta1.archivos:
    print(f"- {archivo.nombre}.{archivo.extension} | {archivo.tamaño} bytes")

print("\n=== RESULTADO FINAL ===")
# 7. Mostrar un mensaje confirmando la relación one-to-many
print(f"La carpeta {carpeta1.nombre} tiene {len(carpeta1.archivos)} archivos")