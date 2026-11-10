from sqlalchemy import Boolean, CheckConstraint, ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Equipo(Base):
    __tablename__ = "equipos"
    __table_args__ = (
        CheckConstraint("stock_disponible >= 0", name="ck_stock_disponible"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    tipo: Mapped[str] = mapped_column(String(100), nullable=False)
    stock_disponible: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    prestamos: Mapped[list["Prestamo"]] = relationship(back_populates="equipo")


class Estudiante(Base):
    __tablename__ = "estudiantes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    correo: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    prestamos: Mapped[list["Prestamo"]] = relationship(back_populates="estudiante")


class Prestamo(Base):
    __tablename__ = "prestamos"
    __table_args__ = (
        CheckConstraint("cantidad > 0", name="ck_cantidad"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    estudiante_id: Mapped[int] = mapped_column(ForeignKey("estudiantes.id"), nullable=False)
    equipo_id: Mapped[int] = mapped_column(ForeignKey("equipos.id"), nullable=False)
    equipo: Mapped["Equipo"] = relationship(back_populates="prestamos")
    estudiante: Mapped["Estudiante"] = relationship(back_populates="prestamos")
    fecha: Mapped[str] = mapped_column(String(10), nullable=False)
    cantidad: Mapped[int] = mapped_column(Integer, nullable=False)
    estado: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)