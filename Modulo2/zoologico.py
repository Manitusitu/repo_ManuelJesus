"""
Crea una aplicación FastAPI con tres endpoints GET específicos:

1. Endpoint /animales: Devuelve una respuesta JSON con una lista de 4 animales. Cada animal debe ser un string con el nombre del animal.

2. Endpoint /zoologico: Devuelve información básica sobre el zoológico en formato JSON, incluyendo el nombre del zoológico, la cantidad total de animales, si está abierto, y el horario de atención.

3. Endpoint /estadisticas: Devuelve estadísticas del zoológico en formato JSON con datos anidados, incluyendo:

Información general del zoológico (nombre y ubicación)
Datos de animales (total de especies y animales más populares)
Estado operacional (abierto/cerrado y empleados presentes)
Para empezar:

Importa FastAPI
Crea la instancia de la aplicación
Define cada endpoint usando el decorador pertinente seguido de la función correspondiente
Cada función debe devolver un diccionario de Python (FastAPI lo convertirá automáticamente a JSON)
Usa nombres descriptivos para las funciones y claves JSON
Incluye datos anidados en el endpoint de estadísticas
"""

from fastapi import FastAPI

# Crear la instancia de la aplicación

app = FastAPI()

# Escribe aquí tu código para los endpoints GET

@app.get("/animales")
def obtener_animales():
    return {"animales": ["León", "Tortuga", "Ornitorrinco","Huron"]}


@app.get("/zoologico")
def obtener_datos_zoologico():
    return {"nombre": "Zoologico Wilson", "cantidad total de animales": 150, "abierto": True, "horario de atencion": "12:30 - 14:30"}

@app.get("/estadisticas")
def obtener_estadisticas():
    return {
        "Informacion General": {
            "nombre": "Zoologico Wilson",
            "ubicacion" : "Sevilla"
        },
        "Datos de animales": {
            "total de especies": 60,
            "animales mas populares" : ["Leon","Tigre", "Elefante","Marsupilami"]
        },
        "Estado operacional": {
            "abierto/cerrado": "abierto",
            "empleados presentes": 30
        }   
    }
    