import csv

#Guardamos el archivo en csv
def guardar_csv(inventario, ruta, incluir_header=True):
    if not inventario:
        print("Inventario vacío, no se guardó")
        return

    try:
        with open(ruta, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            if incluir_header:
                writer.writerow(["nombre", "precio", "cantidad"])
            for p in inventario:
                writer.writerow([p['nombre'], p['precio'], p['cantidad']])
        print(f"Inventario guardado en: {ruta}")
    except Exception as e:
        print(f"Error al guardar: {e}")


#Cargamos nuestro inventario desde un archivo cvs
def cargar_csv(ruta):
    inventario = []
    errores = 0

    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)

            if header != ["nombre", "precio", "cantidad"]:
                print("Encabezado inválido")
                return []

            for fila in reader:
                try:
                    if len(fila) != 3:
                        raise ValueError("Columnas incorrectas")

                    nombre = fila[0]
                    precio = float(fila[1])
                    cantidad = int(fila[2])

                    if precio < 0 or cantidad < 0:
                        raise ValueError("Valores negativos")

                    inventario.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
                except:
                    errores += 1

        print(f"Carga completa. Errores: {errores}")
        return inventario

    except FileNotFoundError:
        print("Archivo no encontrado")
    except Exception as e:
        print(f"Error: {e}")

    return []