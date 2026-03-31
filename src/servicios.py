#Agregamos los productos que va a tener nuestro inventario

def agregar_producto(inventario, nombre, precio, cantidad):
    inventario.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})

#Mostramos todos los productos que ingresamos en nuestra lista 
def mostrar_inventario(inventario):
    if not inventario:
        print("Inventario vacío")
        return
    for p in inventario:
        print(f"Nombre: {p['nombre']} | Precio: {p['precio']} | Cantidad: {p['cantidad']}")



#Buscar Producto por su nombre 
def buscar_producto(inventario, nombre):
    for p in inventario:
        if p['nombre'].lower() == nombre.lower():
            return p
    return None



#Actualizar un producto exis}tente
def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    producto = buscar_producto(inventario, nombre)
    if producto:
        if nuevo_precio is not None:
            producto['precio'] = nuevo_precio
        if nueva_cantidad is not None:
            producto['cantidad'] = nueva_cantidad
        print("Producto actualizado")
    else:
        print("Producto no encontrado")


#Eliminar un producto que ya existe 
def eliminar_producto(inventario, nombre):
    producto = buscar_producto(inventario, nombre)
    if producto:
        inventario.remove(producto)
        print("Producto eliminado")
    else:
        print("Producto no encontrado")

#Calculamos estadistica del inventario
def calcular_estadisticas(inventario):
    if not inventario:
        return {}

    unidades_totales = sum(p['cantidad'] for p in inventario)
    valor_total = sum(p['precio'] * p['cantidad'] for p in inventario)
    producto_mas_caro = max(inventario, key=lambda x: x['precio'])
    producto_mayor_stock = max(inventario, key=lambda x: x['cantidad'])

    return {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": producto_mas_caro,
        "producto_mayor_stock": producto_mayor_stock
    }
