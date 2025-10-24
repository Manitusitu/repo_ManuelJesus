"""
Crea una función llamada dividir_numeros que reciba como entrada dos valores proporcionados por el usuario y realice una división entre ellos. La función debe:

Solicitar al usuario que introduzca dos números (usando la función input())
Convertir las entradas a números enteros
Realizar la división del primer número entre el segundo
Devolver el resultado de la división
La función debe manejar correctamente las siguientes excepciones:

Si el usuario introduce algo que no se puede convertir a un entero, mostrar el mensaje "Error: Debes introducir un número válido"
Si el usuario intenta dividir entre cero, mostrar el mensaje "Error: No es posible dividir entre cero"
Finalmente, independientemente de si la operación tuvo éxito o no, la función debe mostrar el mensaje "Operación finalizada".

"""

def dividir_numeros():
    
    try:

        # Solicitar al usuario que introduzca dos números
        numero1 = input("Escriba el primer numero: ")
        numero2 = input("Escriba el segundo numero: ")
        
        # Convertir las entradas a números enteros
        numero1entero = int(numero1)
        numero2entero = int(numero2)
        
        # Realizar la división del primer número entre el segundo
        division = numero1entero / numero2entero
        
        # Devolver el resultado de la división
        print(f"Esta es la division: {division}")
    
    except ZeroDivisionError:
        print (f"Error: No es posible dividir entre cero")
    
    except ValueError:
        print(f"Error: Debes introducir un número válido")
    
    finally:
        print(f"Operación finalizada")
        
    


# Llamada a la función
dividir_numeros()
