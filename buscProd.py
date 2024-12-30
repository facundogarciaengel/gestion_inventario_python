import sqlite3 as sql

def buscar_producto():
    conn = sql.connect("inventario.db")
    cursor = conn.cursor()
    codigo = int(input("Ingrese el código del producto a buscar: "))
    instruccion = f"SELECT * FROM productos WHERE codigo = {codigo}"
    cursor.execute(instruccion)
    producto = cursor.fetchone()
    if producto == None:
        print("El producto no existe en el inventario")
        return
    else:
        print(f"Código: {producto[0]}")
        print(f"Nombre: {producto[1]}")
        print(f"Descripción: {producto[2]}")
        print(f"Cantidad: {producto[3]}")
        print(f"Precio: {producto[4]}")
        print(f"Categoría: {producto[5]}")

    conn.commit()
    conn.close()

#buscar_producto()