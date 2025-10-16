import sys


VALID_EMAIL = "user@gmail.com"
VALID_PASSWORD= "pass1234"

MAX_INTENTOS = 3
def login_1():
# bucle for para máximo 3 intentos fallidos de verificar email y contraseña
# leer por input el email y password
    for intento in range(1, MAX_INTENTOS + 1): # 1, 2, 3
        email = input("Introduce email: ").strip()
        password = input("Introduce password: ").strip()

        if email == VALID_EMAIL and password == VALID_PASSWORD:
            return True

        intentos_restantes = MAX_INTENTOS - intento # 3 - 1 = 2, 3 - 2 = 1, 3 - 3 = 0
        if intentos_restantes > 0:
            print(f"Credenciales incorrectas, te quedan {intentos_restantes} intentos")
        else:
            print("Has agotado todos los intentos, adiós.")
            sys.exit(1)

login_1()