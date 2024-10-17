import os
import tkinter as tk
from tkinter import messagebox
correlativo = 1
tienda = {}
bodega = {}
clientes = {}
clientes_eliminados = {}

def agregarBodega(nombre_articulo, cantidad, precio, proveedor):
    global correlativo
    datos_articulo = {}

    # Comprobación de existencia en la bodega
    for articulo in bodega.values():
        if articulo['nombre'].lower() == nombre_articulo.lower():  
            raise ValueError(f"El artículo '{nombre_articulo}' ya existe en la bodega.")

    # Comprobación de existencia en la tienda
    for articulo in tienda.values():
        if articulo['nombre'].lower() == nombre_articulo.lower():
            raise ValueError(f"El artículo '{nombre_articulo}' ya existe en la tienda.")

    # Si pasa las verificaciones, agregarlo a la bodega
    datos_articulo['nombre'] = nombre_articulo
    datos_articulo['cantidad'] = cantidad
    datos_articulo['precio'] = precio
    datos_articulo['proveedor'] = proveedor

    bodega[correlativo] = datos_articulo
    correlativo += 1

def moverTienda(id_mover):
    if id_mover in bodega:
        tienda[id_mover] = bodega[id_mover]  
        del bodega[id_mover]  

        return f"El artículo '{tienda[id_mover]['nombre']}' ha sido movido a la tienda."
    else:
        raise ValueError("El ID ingresado no existe en la bodega.")


def mostrar_articulos():
    resultado = ""

    resultado += "\nArtículos en bodega:\n"
    if not bodega:
        resultado += "No hay artículos en la bodega.\n"
    else:
        for id_articulo, datos in bodega.items():
            resultado += f"ID: {id_articulo}, Nombre: {datos['nombre']}, Cantidad: {datos['cantidad']}, Precio: {datos['precio']}\n"

    resultado += "\nArtículos en tienda:\n"
    if not tienda:
        resultado += "No hay artículos en la tienda.\n"
    else:
        for id_articulo, datos in tienda.items():
            resultado += f"ID: {id_articulo}, Nombre: {datos['nombre']}, Cantidad: {datos['cantidad']}, Precio: {datos['precio']}\n"

    
def buscarArticulo(Id_buscar):
    resultado = ""

    if Id_buscar in bodega:
        resultado += f"Artículo encontrado en la bodega: ID {Id_buscar}, Nombre: {bodega[Id_buscar]['nombre']}, Cantidad: {bodega[Id_buscar]['cantidad']}, Precio: {bodega[Id_buscar]['precio']}\n"

    if Id_buscar in tienda:
        resultado += f"Artículo encontrado en la tienda: ID {Id_buscar}, Nombre: {tienda[Id_buscar]['nombre']}, Cantidad: {tienda[Id_buscar]['cantidad']}, Precio: {tienda[Id_buscar]['precio']}\n"

    if not resultado:
        resultado = "Artículo no encontrado en la bodega ni en la tienda."

    return resultado

def eliminarArticulo(id_eliminar):
    if not bodega and not tienda:
        return "No hay artículos para eliminar."

    if id_eliminar in bodega:
        datos = bodega.pop(id_eliminar)
        return f"Artículo '{datos['nombre']}' eliminado de la bodega."
    
    elif id_eliminar in tienda:
        datos = tienda.pop(id_eliminar)
        return f"Artículo '{datos['nombre']}' eliminado de la tienda."
    
    else:
        return "El ID ingresado no existe en la bodega ni en la tienda."

