print("=== PROGRAMA: GESTIÓN DE CALIFICACIONES ===\n")

# Estructura inicial del diccionario
estudiantes = {
    "Ana": [8, 9, 7],
    "Carlos": [6, 8, 9],
    "Elena": [9, 9, 8]
}

print("=== DICCIONARIO INICIAL ===")
print("Estudiantes y sus calificaciones:")
for nombre, calificaciones in estudiantes.items():
    print(f"{nombre}: {calificaciones}")

print("\n=== OPERACIÓN 1: AÑADIR NUEVO ESTUDIANTE ===")
# 1. Añade un nuevo estudiante con sus calificaciones al diccionario
# Escribe aquí tu código
estudiantes["Marcos"] = [5, 8, 7]
print("Diccionario actualizado:")
for nombre, calificaciones in estudiantes.items():
    print(f"{nombre}: {calificaciones}")

print("\n=== OPERACIÓN 2: CALCULAR PROMEDIOS ===")
# 2. Calcula y muestra el promedio de calificaciones de cada estudiante
# Escribe aquí tu código
for nombre, calificaciones in estudiantes.items():
    total = sum(calificaciones)
    
    nota_media = total/3
    
    print(nota_media)
    


print("\n=== OPERACIÓN 3: ENCONTRAR MEJOR ESTUDIANTE ===")
# 3. Identifica y muestra el nombre del estudiante con el promedio más alto
# Escribe aquí tu código
mayor_nota_media  = 0
nombre_mejor_estudiante = " "
for nombre, calificaciones in estudiantes.items():
    total = sum(calificaciones)
    
    nota_media = total/3
    
    if nota_media > mayor_nota_media:
        mayor_nota_media = nota_media
        nombre_mejor_estudiante = nombre
    

print(nombre_mejor_estudiante,mayor_nota_media)



