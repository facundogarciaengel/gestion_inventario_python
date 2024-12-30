import sqlite3 as sql

#Create the database
def crearDb(): 
    conn = sql.connect("inventario.db")
    conn.commit()
    conn.close()

#Create the table
def createTable():
    conn = sql.connect("inventario.db")
    cursor = conn.cursor()
    instruccion = f"CREATE TABLE IF NOT EXISTS productos (codigo INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT NOT NULL, descripcion TEXT NOT NULL, cantidad INTEGER NOT NULL, precio FLOAT NOT NULL, categoria TEXT NOT NULL)"
    cursor.execute(instruccion)
    conn.commit()  
    conn.close()


crearDb()
createTable()   

