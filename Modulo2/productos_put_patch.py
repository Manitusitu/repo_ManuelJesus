'''
Crea una API con FastAPI que gestione productos de una tienda. Debes implementar dos endpoints: uno PUT para actualización completa y otro PATCH para actualización parcial de productos.

Implementa lo siguiente:

Define un modelo Producto con los campos: nombre (str), precio (float) y stock (int)
Define un modelo ProductoPatch para actualizaciones parciales con todos los campos opcionales
Crea una lista inicial con al menos 2 productos de ejemplo
Implementa un endpoint PUT en /productos/{producto_id} que reemplace completamente un producto
Implementa un endpoint PATCH en /productos/{producto_id} que actualice solo los campos proporcionados
Ambos endpoints deben:

Recibir el ID del producto en la URL
Validar que el producto existe (devolver error 404 si no existe)
Devolver el producto actualizado
Para el endpoint PATCH, usa model_dump(exclude_unset=True) para obtener solo los campos enviados.
'''

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Define aquí tus modelos Pydantic

class Producto(BaseModel):
    nombre: str
    precio: float
    stock: int

class ProductoPatch(BaseModel):
    nombre: Optional[str] = None
    precio: Optional[float] = None
    stock: Optional[int]


# Define aquí tu lista de productos inicial

lista_productos = [
    {"id": 1, "nombre": "Lavadora", "precio": 50.99, "stock": 13},
    {"id": 2, "nombre": "Microondas", "precio": 31.99, "stock": 45}
]

@app.get("/productos")
def obtener_productos():
    return lista_productos
# Implementa aquí el endpoint PUT
@app.put("/productos/{productos_id}")
def reemplazar_producto(producto_id:int, producto: Producto):
    
    for i, product in enumerate(lista_productos):
        if product["id"] == producto_id:
            lista_productos[i] = {
                "id" : producto_id,
                "nombre": producto.nombre,
                "precio": producto.precio,
                "stock": producto.stock
            }
            return lista_productos[i]
        
    raise HTTPException (status_code=404, detail="404- Producto no encontrado")
# Implementa aquí el endpoint PATCH

@app.patch("/productos/{producto_id}")
def reemplazar_producto_parcialmente(producto_id:int, producto_patch:ProductoPatch):
    producto_index = None
    
    for i, product in enumerate(lista_productos):
        if product["id"] == producto_id:
            producto_index = i
    
    if producto_index is None:
        raise HTTPException (status_code=404, detail="404- Producto no encontrado")

    datos_actualizacion = producto_patch.model_dump(exclude_unset=True)

    for campo, valor in datos_actualizacion.items():
        lista_productos[producto_index] [campo] = valor
    
    return {
        "mensaje" : "Producto cambiado correctamente",
        "producto" : lista_productos[producto_index]
    }
