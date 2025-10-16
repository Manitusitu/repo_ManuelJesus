# Solicitar la edad al usuario
edad = input("Dime cual es tu edad: ")
# Convertir la entrada a entero
edad_entero = int(edad)
# Evaluar la edad usando if-elif-else
if edad_entero < 13:
    print("Eres un niño")
elif edad_entero >= 13 and edad_entero <= 17:
    print("Eres un adolescente")
elif edad_entero >= 18 and edad_entero <= 64:
    print("Eres un adulto")
else:
    print("Eres un adulto mayor")
    
# Mostrar el mensaje correspondiente