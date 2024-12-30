from regProd import registrar_producto
from mostrProd import mostrar_productos
from buscProd import buscar_producto
from actProd import actualizar_producto
from elimProd import eliminar_producto
from reportBajoStock import reporte_bajo_stock
from colorama import init, Fore, Back, Style
import sqlite3 as sql
init(autoreset=True) # Reset the color after each print

contador = 0
def menu_principal():
    while True:
        print(Style.BRIGHT + Fore.BLUE + Back.WHITE + "\nMenú de Gestion de Personas".center(40, " ")) 
        print(Style.BRIGHT + Fore.CYAN + "1. Registrar producto")
        print(Style.BRIGHT + Fore.CYAN + "2. Mostrar productos")
        print(Style.BRIGHT + Fore.CYAN + "3. Buscar producto")
        print(Style.BRIGHT + Fore.CYAN + "4. Actualizar producto")
        print(Style.BRIGHT + Fore.CYAN + "5. Eliminar producto")
        print(Style.BRIGHT + Fore.CYAN + "6. Reporte de productos bajo stock")
        print(Style.BRIGHT + Fore.RED + "7. Salir")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            actualizar_producto()
        elif opcion == "5":
            eliminar_producto()
        elif opcion == "6":
            reporte_bajo_stock()
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")
if __name__ == "__main__":
    menu_principal()
    