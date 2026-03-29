inventario = []
def agregar_producto():
    nombre = input("ingresar nombre producto: ")
    precio = int(input("ingresar precio del producto: "))
    cantidad = float(input("ingresar cantidad: ")) 
    
    producto = {
        "nombre" : nombre,
        "precio" : precio,
        "cantidad" : cantidad
     }   
    inventario.append(producto)
   

def mostrar_inventario():
    if len(inventario) == 0:
        print(" El inventario está vacío.\n")
    else:
        print("\n Inventario:")
        for producto in inventario:
            print(f"Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")
        print()

def calcular_estadistica():
    if len(inventario)==0:
        print("no hay datos para calcular")
        return
    
total_valor = 0
total_cantidad = 0

for producto in inventario:
    total_valor += producto["precio"] * producto["cantidad"]
    total_cantidad += producto ["cantidad"]

    print(f" valor total del inventario: {total_valor}")
    print(f" valor cantidad del producto: {total_cantidad}")
    


 
