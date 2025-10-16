print("=== PROGRAMA: GENERADOR DE PATRÓN TRIANGULAR ===\n")

# Solicitar al usuario la altura del triángulo
altura = input("Escriba la altura: ")


# Convertir la entrada a número entero
altura_triangulo_entero = int(altura)

print(f"\nGenerando patrón triangular de altura {altura}:")
print("-" * 30)

# Generar el patrón usando bucles for anidados
# Bucle externo: para cada fila (desde 1 hasta la altura)
for i in range(1, altura_triangulo_entero+1):
    print()
    for k in range(1,i+1):
        print(k, end=" ")


    # Bucle interno: para cada número en la fila actual (desde 1 hasta el número de fila)
    # Escribe aquí tu código para el bucle interno


        # Imprimir cada número seguido de un espacio (sin salto de línea)
        # Escribe aquí tu código para imprimir el número


    # Después de completar una fila, hacer un salto de línea
    # Escribe aquí tu código para el salto de línea


print("-" * 30)
print("Patrón completado!")