import libro as l
import random
import string

# Crear una lista vacía para almacenar los libros
libros = {}

# Añadir los diccionarios a la lista


def ejemplares_prestados():
   for cod, libro in libros.items():
        cantidad_prestados = libro["Prestados"]
        if cantidad_prestados > 0:
            print(f"Codigo: {cod}, Titulo: {libro['Titulo']}, Prestados: {cantidad_prestados}")
   else:
        print("No hay mas libros prestados.")
   return 

def registrar_nuevo_libro():
    nuevo_libro = l.nuevo_libro()
    #completar
    return None

def eliminar_ejemplar_libro():
    cod = input("Ingrese el codigo del libro: ")
    if cod in libros:
        cantidad_adquiridos = int(input("Ingrese la cantidad a eliminar: "))
        if cantidad_adquiridos <= libros[cod]["Cantidad"]:
            libros[cod]["Cantidad"] -= cantidad_adquiridos
            libros[cod]["Disponibles"] -= cantidad_adquiridos
            print(f"{cantidad_adquiridos} libros eliminados.")
        else:
            print("Cantidad invalida o mayor.")
    else:
        print("El codigo es invalido.")
    return 

def prestar_ejemplar_libro():
   cod = input("Ingrese el codigo del libro: ")
   if cod in libros:
        if libros[cod]["Disponibles"] > 0:
            print(f"Autor: {libros[cod]['Autor']}")
            print(f"Titulo: {libros[cod]['Titulo']}")
            print(f"Cantidad de ejemplares disponibles: {libros[cod]['Disponibles']}")
            confirmacion = input("¿Desea confirmar el prestamo? (S/N): ")
            if confirmacion.lower() == 's':
                libros[cod]["Disponibles"] -= 1
                libros[cod]["Prestados"] += 1
                print("Prestamo confirmado.")
            else:
                print("Prestamo cancelado.")
        else:
            print("No hay libros disponibles.")
   else:
        print("El codigo ingresado es invalido.")

   return 

def devolver_ejemplar_libro():
   cod = input("Ingrese el codigo del libro: ")
   if cod in libros and libros[cod]["Prestados"] > 0:
        confirmacion = input("¿Desea confirmar la devolución? (S/N): ")
        if confirmacion.lower() == 's':
            libros[cod]["Prestados"] -= 1
            print("Devolucion exitosa")
        else:
            print("Devolucion cancelada")
   else:
        print("El codigo del libro ingresado es invalido")
   return 

def nuevo_libro():
 autor = input("Ingrese el nombre del autor: ")
 titulo = input("Ingrese el nombre del libro: ")
 cantidad_adquiridos = int(input("Ingrese la cantidad de libros: "))
 characters = string.ascii_letters + string.digits
 cod = ''.join(random.choice(characters) for i in range(8))
 
 libros[cod] = {
        "Codigo": cod,
        "Cantidad": cantidad_adquiridos,
        "Prestados": 0,
        "Disponibles": cantidad_adquiridos,
        "Autor": autor,
        "Titulo": titulo
    }
 print(f"Libro registrado. Codigo: {cod}")
 return 