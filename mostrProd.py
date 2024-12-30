import sqlite3 as sql

def mostrar_productos():
    conn = sql.connect("inventario.db")
    cursor = conn.cursor()
    instruccion = "SELECT * FROM productos"
    cursor.execute(instruccion)
    productos = cursor.fetchall()
    if not productos:
        print("No hay productos en el inventario")
        return
    else: 
     for producto in productos:
        print(f"Código: {producto[0]}")
        print(f"Nombre: {producto[1]}")
        print(f"Descripción: {producto[2]}")
        print(f"Cantidad: {producto[3]}")
        print(f"Precio: {producto[4]}")
        print(f"Categoría: {producto[5]}")
        print("-------------------------------")
    conn.commit()
    conn.close()

#mostrar_productos()
