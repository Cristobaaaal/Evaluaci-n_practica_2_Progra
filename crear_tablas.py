from conexion import engine
from modelos import Base

Base.metadata.create_all(engine)
print("Tablas Listas")