# Evaluaci-n_practica_2_Progra
Evaluación practica de Programación II (ICINF1109).
Cristóbal Dapellus

## Requisitos

- Python 3.10 o superior.
- SQLAlchemy 2.x.
- SQLite, incluido con Python.

## Instalación y ejecución en Windows

Abre PowerShell en la carpeta que contiene `main.py`. Crea el entorno virtual e instala SQLAlchemy:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install "SQLAlchemy>=2.0,<3.0"
python -c "import sqlalchemy; print(sqlalchemy.__version__)"
```

Luego inicia el programa:

```powershell
python main.py
```

Al iniciar, el programa crea las tablas si aún no existen. La base `prestamos.db` se guarda en la carpeta desde donde ejecutas el programa.

## Menú
1. Registrar equipo
2. Registrar estudiante
3. Consultar equipos.
4. Pedir préstamo. 
5. Registrar devolución. 
6. Salir.

Para comprobar la persistencia, sal con la opción `0`, abre el programa de nuevo y consulta las reservas.
