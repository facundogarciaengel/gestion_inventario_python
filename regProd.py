#Para registrar productos en la tabla productos debemos importar sqlite3 y 
#crear una función que inserte los datos en la tabla productos.
import sqlite3 as sql

def registrar_producto():
    conn = sql.connect("inventario.db")
    cursor = conn.cursor()
    nombre = input("Ingrese el nombre del producto: ")
    descripcion = input("Ingrese la descripción del producto: ")
    cantidad = int(input("Ingrese la cantidad del producto: "))
    precio = float(input("Ingrese el precio del producto: "))
    categoria = input("Ingrese la categoría del producto: ")
    instruccion = f"INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria) VALUES ('{nombre}', '{descripcion}', {cantidad}, {precio}, '{categoria}')"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()
    print("Producto registrado con éxito")

#registrar_producto()
