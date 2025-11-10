"""
Crea una clase CuentaBancaria que implemente el concepto de encapsulación. La clase debe tener los siguientes atributos privados: _titular (string) y _saldo (float). Implementa propiedades para acceder y modificar estos atributos de forma controlada:

La propiedad titular debe permitir obtener el valor pero no modificarlo (solo lectura).
La propiedad saldo debe permitir obtener el valor y modificarlo, pero con la restricción de que no se pueda establecer un saldo negativo (debe lanzar un ValueError con el mensaje "El saldo no puede ser negativo").
Añade un método depositar(cantidad) que incremente el saldo solo si la cantidad es positiva, devolviendo True si la operación fue exitosa o False en caso contrario.
Añade un método retirar(cantidad) que disminuya el saldo solo si hay suficiente dinero, devolviendo True si la operación fue exitosa o False en caso contrario.
La clase debe inicializarse con un titular y un saldo inicial (que por defecto será 0).
"""

print("=== PROGRAMA: SISTEMA DE CUENTA BANCARIA ===\n")


class CuentaBancaria:
    """
    Implementa una cuenta bancaria encapsulada con propiedades
    y métodos para gestionar el saldo.
    """
    
    def __init__(self, titular, saldo_inicial=0.0):
        """
        Inicializa la cuenta bancaria.
        
        Args:
            titular (str): El nombre del titular de la cuenta.
            saldo_inicial (float, optional): El saldo inicial. Defaults to 0.0.
        """
        self._titular = titular # Atributo privado
        
        # Validamos el saldo inicial usando la lógica de la propiedad
        # (Aunque podríamos asignar a _saldo, es buena práctica 
        # usar la propiedad si ya tiene lógica de validación).
        self.saldo = saldo_inicial

    # --- Propiedad titular (Solo lectura) ---
    
    @property
    def titular(self):
        """
        Obtiene el nombre del titular de la cuenta (solo lectura).
        """
        return self._titular
    
    # No definimos @titular.setter para hacerlo de solo lectura

    # --- Propiedad saldo (Lectura y Escritura controlada) ---
    
    @property
    def saldo(self):
        """
        Obtiene el saldo actual de la cuenta.
        """
        return self._saldo

    @saldo.setter
    def saldo(self, nuevo_saldo):
        """
        Establece un nuevo saldo, validando que no sea negativo.
        """
        if nuevo_saldo < 0:
            raise ValueError("El saldo no puede ser negativo")
        
        self._saldo = float(nuevo_saldo) # Aseguramos que sea float

    # --- Métodos de la cuenta ---

    def depositar(self, cantidad):
        """
        Añade una cantidad al saldo si esta es positiva.
        
        Args:
            cantidad (float): La cantidad a depositar.
            
        Returns:
            bool: True si el depósito fue exitoso, False si no.
        """
        if cantidad > 0:
            self._saldo += cantidad # Usamos _saldo para evitar el setter
            # (self.saldo += cantidad también funcionaría)
            return True
        else:
            return False

    def retirar(self, cantidad):
        """
        Resta una cantidad al saldo si es positiva y hay fondos suficientes.
        
        Args:
            cantidad (float): La cantidad a retirar.
            
        Returns:
            bool: True si el retiro fue exitoso, False si no.
        """
        if cantidad > 0 and self._saldo >= cantidad:
            self._saldo -= cantidad
            return True
        else:
            # Falla si la cantidad es negativa o si no hay fondos
            return False

    def __str__(self):
        """Representación en string de la cuenta."""
        return f"Cuenta de {self.titular} | Saldo: {self.saldo:.2f}€"
        

# === PRUEBAS DE LA CLASE ===
print("=== CREANDO CUENTA BANCARIA ===")
# Crear una cuenta bancaria
# Escribe aquí tu código
cuenta = CuentaBancaria("Jose Luis", 0)

print(f"Titular: {cuenta.titular}")
print(f"Saldo inicial: ${cuenta.saldo}")

print("\n=== PROBANDO DEPÓSITOS ===")
# Probar depósito válido
# Escribe aquí tu código
cuenta.depositar(50)

# Probar depósito inválido
# Escribe aquí tu código
cuenta.depositar(-2)

print(f"Saldo después de operaciones: ${cuenta.saldo}")

print("\n=== PROBANDO RETIROS ===")
# Probar retiro válido
# Escribe aquí tu código
cuenta.retirar(20)

# Probar retiro que excede el saldo
# Escribe aquí tu código
cuenta.retirar(9999)

print(f"Saldo final: ${cuenta.saldo}")

print("\n=== PROBANDO VALIDACIONES ===")
# Intentar establecer un saldo negativo
#try:
    
    # Escribe aquí tu código para probar saldo negativo
    
#except ValueError as e:
#    print(f"Error capturado: {e}")