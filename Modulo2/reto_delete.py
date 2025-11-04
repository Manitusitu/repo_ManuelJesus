'''
Crea una aplicación FastAPI que permita eliminar libros de una biblioteca digital. Debes implementar un endpoint DELETE que elimine un libro específico por su ID.

Instrucciones paso a paso:

Importa FastAPI y HTTPException
Crea una instancia de FastAPI llamada app
Define una lista llamada libros con estos datos iniciales:


Implementa un endpoint DELETE en la ruta /libros/{libro_id} que:
Reciba libro_id como parámetro de tipo entero
Busque el libro en la lista por su ID
Si encuentra el libro, lo elimine de la lista y devuelva un mensaje de confirmación
Si no encuentra el libro, lance una HTTPException con código 404 y el mensaje "Libro no encontrado"
'''


from fastapi import FastAPI, HTTPException

app = FastAPI()

# Define aquí la lista de libros

libros = [
    {"id": 1, "titulo":"El Quijote", "autor":"Cervantes"},
    {"id": 2, "titulo":"Cien años de soledad", "autor":"García Marques"},
    {"id": 3, "titulo":"1984", "autor":"Orwell"}
]



# Implementa aquí el endpoint DELETE

@app.get("/libros")
def obtener_libros():
    return libros

@app.delete("/libros/{libro_id}")
def eliminarlibros(libro_id: int):
    for i, libro in enumerate(libros):
        if libro["id"] == libro_id:
            libro_eliminado = libros.pop(i)
            return {
                "mensaje": "Libro eliminado exitosa"
            }
    raise HTTPException(status_code=404, detail="404 - Libro no encontrado")

