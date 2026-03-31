from src.servicios import *
from src.archivos import *



#MENU DEL PROGRAMA 
def menu():
   print("Proyecto de inventario de productos ")
   print("1. Agregar productos ")
   print("2. Mostrar productos ")
   print("3. Buscar productos ")
   print("4. Actualizar productos ")
   print("5. Eliminar productos ")
   print("6. Estadisticas del productos ")
   print("7. Guardar csv ")
   print("8. Cargar csv ")
   print("9. Salir del programa ")


def main():
    inventario = []

    while True:
        menu()
        opcion = input("Seleccione opción: ")

        if opcion == '1':
            nombre = input("ingresar nombre producto: ")
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad: "))
            agregar_producto(inventario, nombre, precio, cantidad)

        elif opcion == '2':
            mostrar_inventario(inventario)

        elif opcion == '3':
            nombre = input("Nombre a buscar: ")
            print(buscar_producto(inventario, nombre))

        elif opcion == '4':
            nombre = input("Nombre: ")
            precio = input("Nuevo precio (enter para omitir): ")
            cantidad = input("Nueva cantidad (enter para omitir): ")

            actualizar_producto(
                inventario,
                nombre,
                float(precio) if precio else None,
                int(cantidad) if cantidad else None
            )

        elif opcion == '5':
            nombre = input("Nombre: ")
            eliminar_producto(inventario, nombre)

        elif opcion == '6':
            stats = calcular_estadisticas(inventario)
            print(stats)

        elif opcion == '7':
            ruta = input("Ruta archivo: ")
            guardar_csv(inventario, ruta)

        elif opcion == '8':
            ruta = input("Ruta archivo: ")
            nuevo = cargar_csv(ruta)

            if nuevo:
                decision = input("¿Sobrescribir inventario? (S/N): ")
                if decision.lower() == 's':
                    inventario = nuevo
                else:
                    inventario.extend(nuevo)

        elif opcion == '9':
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()