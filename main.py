from src.validacion_de_datos import *

#MENU PRINCIPAL



print("Proyecto de inventario de productos")
print("1. Agregar producto")
print("2. Mostrar inventario")
print("3. Calcular estadistica")
print("4. Salir")

opcion = (input("Seleccione una opcion: "))


if opcion == "1":  
    agregar_producto()
    print("Producto agregado correctamente")

elif opcion == "2":
    mostrar_inventario()

elif opcion == "3":
    calcular_estadistica()

elif opcion == "4":
    print("Saliendo del programa")

else:
    print("x Opcion invalida, intente nuevamente ")

