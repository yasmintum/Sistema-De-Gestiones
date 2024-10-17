import os 
import tkinter as tk
from tkinter import messagebox
correlativo = 1 
clientes = {}
clientes_eliminados = {}

def agregarCliente(nombre_Cliente, Apellido_Cliente, Nit_Cliente, Dpi_Cliente, telefono_Cliente):
    global correlativo
    datos_Clientes = {}
    for persona in clientes.values():
        if persona['Dpi'].lower() == Dpi_Cliente.lower():  
            messagebox.showerror("Error", f"El Cliente con DPI '{Dpi_Cliente}' ya existe")
            return
        
    datos_Clientes['Dpi'] = Dpi_Cliente
    datos_Clientes['nombre'] = nombre_Cliente
    datos_Clientes['apellido'] = Apellido_Cliente
    datos_Clientes['Nit'] = Nit_Cliente
    datos_Clientes['telefono'] = telefono_Cliente

    clientes[correlativo] = datos_Clientes
    correlativo += 1

def mostrar_clientes():
    resultado = ""
    resultado += "\nClientes:\n"
    if not clientes:
        return "No hay Clientes.\n"

    else:
        for id_cliente, datos in clientes.items():
            resultado += (f"ID: {id_cliente}, Nombre: {datos['nombre']}, Apellido: {datos['apellido']}, Nit: {datos['Nit']}, Telefono: {datos['telefono']}\n")
        return resultado

def eliminar_cliente(id_cliente):
    if id_cliente in clientes:
        clientes_eliminados[id_cliente] = clientes.pop(id_cliente)
        return f"El cliente con ID {id_cliente} ha sido eliminado."
    else:
        raise ValueError("El ID ingresado no existe en la lista de clientes.")

def Historial_clientes_eliminados():
    resultado = ""
    resultado += "\nClientes eliminados:\n"
    if not clientes_eliminados:
        return "No hay clientes eliminados.\n"
    else:
        for id_cliente, datos in clientes_eliminados.items():
            resultado += f"ID: {id_cliente}, Nombre: {datos['nombre']}, Apellido: {datos['apellido']}, Nit: {datos['Nit']}, Telefono: {datos['telefono']}\n"
    return resultado

def buscar_cliente(id_cliente):
    if id_cliente in clientes:
        datos = clientes[id_cliente]
        return f"Nombre: {datos['nombre']}, Apellido: {datos['apellido']}, Nit: {datos['Nit']}, Telefono: {datos['telefono']}"
    else:
        raise ValueError("El ID ingresado no existe en la lista de clientes.")