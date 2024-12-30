import sqlite3 as sql

def eliminar_producto():
    conn = sql.connect("inventario.db")
    cursor = conn.cursor()
    codigo = int(input("Ingrese el código del producto a eliminar: "))
    instruccion = f"SELECT * FROM productos WHERE codigo = {codigo}"
    cursor.execute(instruccion)
    producto = cursor.fetchone()
    if producto == None:
        print("El producto no existe en el inventario")
        return
    else: 
        instruccion = f"DELETE FROM productos WHERE codigo = {codigo}"
        cursor.execute(instruccion)
        conn.commit()
        conn.close()
        print("Producto eliminado correctamente")
    
#eliminar_producto()