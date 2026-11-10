from datetime import date
from sqlalchemy import update
from conexion import Session
from modelos import Equipo, Estudiante, Prestamo


def registrar_prestamo(equipo_id: int, estudiante_id: int, cantidad: int, fecha: str):
    fecha = fecha.strip()

    if cantidad <= 0:
        raise ValueError("La cantidad debe ser mayor que cero.")

    mensaje_fecha = "Ingresa una fecha válida en formato AAAA-MM-DD."
    try:
        fecha_validada = date.fromisoformat(fecha)
    except ValueError:
        raise ValueError(mensaje_fecha) from None

    if fecha_validada.isoformat() != fecha:
        raise ValueError(mensaje_fecha)

    with Session.begin() as session:
        if session.get(Estudiante, estudiante_id) is None:
            raise ValueError("No existe un estudiante con ese ID.")

        resultado = session.execute(
            update(Equipo)
            .where(Equipo.id == equipo_id, Equipo.stock_disponible >= cantidad)
            .values(stock_disponible=Equipo.stock_disponible - cantidad)
        )
        if resultado.rowcount == 0:
            if session.get(Equipo, equipo_id) is None:
                raise ValueError("No existe un equipo con ese ID.")
            raise ValueError("No hay stock suficiente para ese préstamo.")

        session.add(
            Prestamo(
                estudiante_id=estudiante_id,
                equipo_id=equipo_id,
                cantidad=cantidad,
                fecha=fecha,
            )
        )


def pedir_prestamo():
    try:
        estudiante_id = int(input("ID del estudiante: "))
    except ValueError:
        print("El ID del estudiante debe ser un número entero.")
        return

    try:
        equipo_id = int(input("ID del equipo: "))
    except ValueError:
        print("El ID del equipo debe ser un número entero.")
        return

    fecha = input("Fecha (AAAA-MM-DD): ")

    try:
        cantidad = int(input("Cantidad: "))
    except ValueError:
        print("La cantidad debe ser un número entero.")
        return

    try:
        registrar_prestamo(equipo_id, estudiante_id, cantidad, fecha)
    except ValueError as error:
        print(error)
        return

    print("Préstamo registrado correctamente.")