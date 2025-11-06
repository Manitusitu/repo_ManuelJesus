print("=== PROGRAMA: ANÁLISIS DE ESTUDIANTES POR ASIGNATURA ===\n")

# Definir los tres conjuntos de estudiantes
# 1. Conjunto de estudiantes que cursan matemáticas (5 estudiantes)
# Escribe aquí tu código
estudiantes_matematicas = {"Lucas", "Mateo", "Maria","Manuel", "Juan"}

# 2. Conjunto de estudiantes que cursan física (5 estudiantes)
# Escribe aquí tu código
estudiantes_fisica = {"Lucas", "Sueyo", "Marta","Manolo", "Jose"}


# 3. Conjunto de estudiantes que cursan programación (5 estudiantes)
# Escribe aquí tu código

estudiantes_programacion = {"Lucas", "Mateo", "Marta","Manolo", "Diego"}


print("=== CONJUNTOS INICIALES ===")
print(f"Estudiantes de Matemáticas: {estudiantes_matematicas}")
print(f"Estudiantes de Física: {estudiantes_fisica}")
print(f"Estudiantes de Programación: {estudiantes_programacion}")

print("\n=== ANÁLISIS DE INTERSECCIONES Y DIFERENCIAS ===")

# 1. Los estudiantes que cursan las tres asignaturas
# Escribe aquí tu código usando operadores de conjuntos

tres_asignaturas = estudiantes_matematicas.intersection(estudiantes_fisica,estudiantes_programacion)

print(f"Estudiantes que cursan las tres asignaturas: {tres_asignaturas}")

# 2. Los estudiantes que cursan matemáticas y física, pero no programación
# Escribe aquí tu código usando operadores de conjuntos

mat_fis_no_prog = estudiantes_matematicas.intersection(estudiantes_fisica) - estudiantes_programacion

print(f"Estudiantes que cursan matemáticas y física, pero no programación: {mat_fis_no_prog}")

# 3. Los estudiantes que solo cursan una asignatura
# Escribe aquí tu código para cada asignatura individualmente


solo_una_asignatura = estudiantes_matematicas.symmetric_difference(estudiantes_fisica) - estudiantes_programacion

# Unir los tres conjuntos de estudiantes que solo cursan una asignatura
# Escribe aquí tu código


print(f"Estudiantes que solo cursan una asignatura: {solo_una_asignatura}")

# 4. Todos los estudiantes únicos (el conjunto total)
# Escribe aquí tu código usando operadores de conjuntos
todos_estudiantes = estudiantes_matematicas.union(estudiantes_fisica,estudiantes_programacion)

print(f"Total de estudiantes únicos: {todos_estudiantes}")
print(f"Número total de estudiantes: {len(todos_estudiantes)}")