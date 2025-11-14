from fastapi import Depends, FastAPI, HTTPException, status
from pydantic import BaseModel, ConfigDict
from sqlalchemy import create_engine, Integer, String, Boolean, select
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column, Session


"""
VIDEOS
- title: string (obligatorio)
- channel: string (obligatorio)
- views: entero (opcional)
- has_subtitles: booleano (opcional)
"""

# CONFIGURACIÓN DE BASE DE DATOS
#crear motor de conexion con la base de datos
engine = create_engine(
    "sqlite:///Modulo2/videos.db",
    echo=True,
    connect_args={"check_same_thread":False}
)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=True,
    expire_on_commit=False
)
# MODELO DE BASE DE DATOS (SQLALCHEMY)

#clase base
class Base(DeclarativeBase):
    pass

#modelo de tabla videos
class Video(Base):
    __tablename__ = "videos"
    #id, clave primaria
    id:Mapped[int] = mapped_column(Integer,primary_key=True, autoincrement=True)
    #obligatorio 
    title:Mapped[str]=mapped_column(String,nullable=False)
    #obligatorio, 200 caracteres como minimo
    channel:Mapped[str] = mapped_column(String(200), nullable = False)
    #opcional
    views: Mapped[int | None] = mapped_column(Integer,nullable=True)
    #opcional
    has_subtitles: Mapped[bool | None] = mapped_column(Boolean,nullable=True)
    
# MODELOS PYDANTIC (SCHEMAS)

class VideoResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    title: str
    channel: str
    views: int | None
    has_subtitles: bool | None

class VideoCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    #Los que son opcionales ponemos el None = None
    title: str
    channel: str
    views: int | None = None
    has_subtitles: bool | None = None
    
class VideoUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    #En un Update(PUT) todo los campos son obligatorios
    #por eso hacemos esto
    title: str
    channel: str
    views: int | None
    has_subtitles: bool | None

class VideoPatch(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    #Como es un patch hay que ponerles None = None para
    #que todo sea opcional
    title: str | None = None
    channel: str | None = None
    views: int | None = None
    has_subtitles: bool | None = None

# INICIALIZACIÓN DE BASE DE DATOS
#crear las tablas de la base de datos
Base.metadata.create_all(engine)

# poblar tablas

def init_db():
    db = SessionLocal()
    try:
        existing_videos = db.execute(select(Video)).scalars().all()
        
        if existing_videos:
            return
        default_videos = [
            Video(title="Grajillas cantando", channel="La Grajilla",
            views=999999, has_subtitles=True),
            Video(title="Engaño a mi mujer y pasa esto", channel="JajaLolLmao",
            views=100000000, has_subtitles=False),
            Video(title="Goofy Aaaaaaah video", channel="Damn_Son",
            views=999999, has_subtitles=True)
            
        ]
        db.add_all(default_videos) # con esto lo añades todo
        db.commit() #hace la operacion
    finally:
        db.close()

init_db()
# DEPENDENCIA DE FASTPI
#metodo para dar sesion de base de datos al endpoint
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# APLICACIÓN FASTAPI
app = FastAPI(title="App de vídeos", version="3.1.4")

@app.get("/")
def home():
    return {"mensaje": "Gracias por pasarte por nuestra app de videos :) "}

# ENDPOINTS CRUD (Create, Read, Update, Delete)
"""
Create: Método POST (create)
Read: Método GET (find_all y find_by_id)
Update: Método PUT (update_full) y método PATCH (update_partial)
Delete: Método DELETE (delete)
"""
@app.get("/api/videos",response_model=list[VideoResponse])
def find_all(db: Session = Depends(get_db)):
    return db.execute(select(Video)).scalars().all()
