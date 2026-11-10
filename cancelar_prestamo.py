from sqlalchemy import delete, update
from conexion import Session
from modelos import Equipo, Prestamo


def cancelar_prestamo(id_prestamo: int):
    with Session.begin() as session:
        prestamo = session.execute(
            delete(Prestamo)
            .where(Prestamo.id == id_prestamo)
            .returning(Prestamo.equipo_id, Prestamo.cantidad)
        ).one_or_none()

        if prestamo is None:
            raise ValueError("No existe un préstamo con ese ID.")

        session.execute(
            update(Equipo)
            .where(Equipo.id == prestamo.equipo_id)
            .values(stock_disponible=Equipo.stock_disponible + prestamo.cantidad)
        )


def pedir_cancelacion() -> None:
    try:
        id_prestamo = int(input("ID del préstamo: "))
    except ValueError:
        print("El ID del préstamo debe ser un número entero.")
        return

    try:
        cancelar_prestamo(id_prestamo)
    except ValueError as error:
        print(error)
        return

    print("Préstamo cancelado. El equipo vuelve a estar disponible.")