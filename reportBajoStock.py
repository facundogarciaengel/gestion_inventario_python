import sqlite3 as sql

def reporte_bajo_stock():
    conn = sql.connect("inventario.db")
    cursor = conn.cursor()
    limite = int(input("Ingrese el límite de stock: "))
    instruccion = f"SELECT * FROM productos WHERE cantidad < {limite}"
    cursor.execute(instruccion)
    productos = cursor.fetchall()
    if not productos:
        print("No hay productos con stock bajo")
        return
    else:
        print("Productos con stock bajo:")
        for producto in productos:
            print(f"Código: {producto[0]}")
            print(f"Nombre: {producto[1]}")
            print(f"Cantidad: {producto[3]}")
            print("-------------------------------")

    conn.commit()
    conn.close()

#reporte_bajo_stock()