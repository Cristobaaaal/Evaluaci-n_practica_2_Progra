from sqlalchemy import select
from conexion import Session
from modelos import Equipo


def consultar_equipos():
    with Session() as session:
        equipos = session.scalars(select(Equipo)).all()

        if not equipos:
            return print("No hay equipos registrados.")

        for equipo in equipos:
            print(f"ID: {equipo.id} | {equipo.nombre} | {equipo.tipo} | {equipo.stock_disponible}")