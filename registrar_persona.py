from sqlite3 import SQLITE_CONSTRAINT_UNIQUE
from sqlalchemy.exc import IntegrityError
from conexion import Session
from modelos import Estudiante


def insertar_estudiante(nombre: str, correo: str):
    nombre = nombre.strip()
    correo = correo.strip()

    if not nombre:
        raise ValueError("El nombre es obligatorio.")
    if not correo:
        raise ValueError("El correo es obligatorio.")

    try:
        with Session.begin() as session:
            session.add(Estudiante(nombre=nombre, correo=correo))
    except IntegrityError as error:
        if getattr(error.orig, "sqlite_errorcode", None) != SQLITE_CONSTRAINT_UNIQUE:
            raise
        raise ValueError("Ya existe un estudiante con ese correo.") from error


def registrar_estudiante() -> None:
    nombre = input("Nombre del estudiante: ")
    correo = input("Correo del estudiante: ")

    try:
        insertar_estudiante(nombre, correo)
    except ValueError as error:
        return print(error)

    print("Estudiante registrado correctamente.")