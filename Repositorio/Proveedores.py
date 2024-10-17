import os   
import tkinter as tk
from tkinter import messagebox
correlativo = 1
proveedores = {}

def agregarProveedor(nombre_proveedor, apellido_proveedor, direccion_proveedor, Dpi_proveedor, Nit_proveedor, telefono_proveedor):
    global correlativo
    datos_proveedor = {}
    for persona in proveedores.values():
        if persona['Dpi'].lower() == Dpi_proveedor.lower():  
            messagebox.showerror("Error", f"El Proveedor con DPI '{Dpi_proveedor}' ya existe")
            return
    datos_proveedor['Dpi'] = Dpi_proveedor
    datos_proveedor['nombre'] = nombre_proveedor
    datos_proveedor['apellido'] = apellido_proveedor
    datos_proveedor['Nit'] = Nit_proveedor
    datos_proveedor['direccion'] = direccion_proveedor
    datos_proveedor['telefono'] = telefono_proveedor

    proveedores[correlativo] = datos_proveedor
    correlativo += 1

def mostrar_proveedores():
    resultado = ""
    resultado += "\nProveedores:\n"
    if not proveedores:
        return "No hay Proveedores.\n"
    
    else: 
        for id_proveedor, datos in proveedores.items():
            resultado+= (f"ID: {id_proveedor}, Nombre: {datos['nombre']}, Apellido: {datos['apellido']}, Nit: {datos['Nit']}, Direccion: {datos['direccion']}, Telefono: {datos['telefono']}\n")
            return resultado
        

def eliminar_proveedor(id_eliminar):
    if id_eliminar in proveedores:
        datos = proveedores.pop(id_eliminar)
        return f"El proveedor con ID {id_eliminar} ha sido eliminado."
    else:
        raise ValueError("El ID ingresado no existe en la lista de proveedores.")
    
def buscar_proveedor(id_buscar):
    if id_buscar in proveedores:
        datos = proveedores[id_buscar]  
        return f"nombre: {datos['nombre']}, apellido: {datos['apellido']}, Nit: {datos['Nit']}, Direccion: {datos['direccion']}, Telefono: {datos['telefono']}"
    else:
        raise ValueError("El ID ingresado no se encuentra existente en la lista de proveedores.")
    7