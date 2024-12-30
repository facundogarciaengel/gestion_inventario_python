 */
# Proyecto: Sistema de Gestión de Inventarios

## Descripción General
Este proyecto es un sistema de gestión de inventarios que permite a los usuarios administrar productos.
 El sistema incluye funcionalidades para agregar, editar, eliminar y visualizar elementos del inventario junto con un reporte de bajo stock. Además, cuenta con un menú principal
que facilita la navegación entre las diferentes secciones del sistema.

## Archivos y Funcionalidades

#### Función: agregar_producto
Agrega un nuevo producto al inventario. Solicita al usuario ingresar los detalles del producto, como nombre, categoría, cantidad y precio.

#### Función: editar_producto
Permite editar la información de un producto existente en el inventario. El usuario puede actualizar los detalles del producto.

#### Función: eliminar_producto
Elimina un producto del inventario basado en su identificador único.

#### Función: listar_productos
Muestra una lista de todos los productos en el inventario, incluyendo sus detalles.

### Función: busca_producto
Permite buscar y mostrar los detalles de un producto específico por su código. 

### Función: reporte_bajo_stock
Permite mostrar los productos que estan por debajo del limite de stock que querramos analizar. Nos pide ingresar un limite de stock
para buscar cuales estan por debajo de ese valor. 

### menu_principal.py
#### Función: mostrar_menu_principal
Muestra el menú principal del sistema de gestión de inventarios. Permite al usuario navegar entre las diferentes funcionalidades del sistema.
 El menú principal ofrece opciones para agregar, editar, eliminar, modificar, generar reportes y listar elementos.
