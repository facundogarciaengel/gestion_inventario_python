import sqlite3 as sql


def actualizar_producto():
    conn = sql.connect("inventario.db")
    cursor = conn.cursor()
    codigo = int(input("Ingrese el código del producto a actualizar: "))
    #si no existe en el inventario de la base de datos el producto, se imprime un mensaje y se retorna
    cursor.execute(f"SELECT * FROM productos WHERE codigo = {codigo}")
    if cursor.fetchone() == None:
        print("El producto no existe en el inventario")
        return
    cantidad = int(input("Ingrese la nueva cantidad del producto: "))
    if cantidad < 0:
        print("La cantidad no puede ser negativa")
        return
    else:
        instruccion = f"UPDATE productos SET cantidad = {cantidad} WHERE codigo = {codigo}"
        cursor.execute(instruccion)
        conn.commit()
        conn.close()
        print("Producto actualizado correctamente")


#actualizar_producto(10)
