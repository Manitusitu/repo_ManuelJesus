from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from sqlalchemy import String, Integer,Float, Boolean, create_engine


app = FastAPI()

#modelo Pydantic

class Producto(BaseModel):
    nombre: str
    precio: float
    stock: int
    disponible: bool


#configuracion bases de datos
DATABASE_URL = "sqlite:///./productos_prueba.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
    
)
# base declarativa
class Base(DeclarativeBase):
    pass

#modelo ORM SqlAlchemy (tabla)

class ProductoORM(Base):
    __tablename__ = "productos"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String,nullable=False)
    precio: Mapped[float] = mapped_column(Float, nullable=False)
    stock: Mapped[int] = mapped_column(Integer, nullable=False)
    disponible: Mapped[bool] = mapped_column(Boolean, nullable=False)
    
#asi creamos las tablas
Base.metadata.create_all(bind=engine)

#crear sesión
db = SessionLocal()

try:
    productos_existentes = db.query(ProductoORM).first()
    productos = [
            ProductoORM(id=1, nombre="Leche", precio=1.99, stock=30, disponible=True),
            ProductoORM(id=2, nombre="Queso", precio=5.99, stock=15, disponible=True),
            ProductoORM(id=3, nombre="Yogur", precio=2.99, stock=25, disponible=False)
        ]
    db.add_all(productos)
    db.commit()
    

finally:
    db.close()