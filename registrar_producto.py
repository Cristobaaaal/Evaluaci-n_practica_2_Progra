from conexion import Session
from modelos import Equipo


def insertar_equipo(nombre: str, tipo: str, stock_disponible: int, ):
    nombre = nombre.strip()

    if not nombre:
        raise ValueError("El nombre del equipo  es obligatorio.")
    if not tipo:
        raise ValueError("El tipo de equipo es obligatorio.")
    if stock_disponible < 0:
        raise ValueError("El stock disponible debe ser mayor que cero.")

    with Session.begin() as session:
        equipo = Equipo(nombre=nombre, tipo=tipo, stock_disponible=stock_disponible)
        session.add(equipo)


def registrar_equipo() -> None:
    nombre = input("Nombre del equipo: ")
    tipo = input("Tipo de equipo:")

    try:
        stock_disponible = int(input("Stock disponible: "))
    except ValueError:
        return print("El stock disponible debe ser un número entero.")
    try:
        insertar_equipo(nombre, tipo, stock_disponible)
    except ValueError as error:
        return print(error)

    print("Equipo registrado correctamente.")