from conexion import engine, Session
import modelos 
import crear_tablas
from registrar_producto import registrar_equipo
from registrar_persona import registrar_estudiante
from consultar_productos import consultar_equipos
from pedir_prestamo import pedir_prestamo
from cancelar_prestamo import pedir_cancelacion

def conexion():
    with engine.connect() as connection:
        print("Conexión exitosa a la base de datos.")
    conexion = engine.connect()
    return conexion

def mostrar_menu():
    print("======== Menú ========")
    print("1. Registrar equipo")
    print("2. Registrar estudiante")
    print("3. Consultar equipos")
    print("4. Pedir préstamo")
    print("5. Registrar devolución")
    print("6. Salir")
    print("======================")

def main():
    conexion()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_equipo()
        elif opcion == "2":
            registrar_estudiante()
        elif opcion == "3":
            consultar_equipos()
        elif opcion == "4":
            pedir_prestamo()
        elif opcion == "5":
            pedir_cancelacion()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
