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


#GET- Obtener un video
@app.get("/api/videos/{id}",response_model=VideoResponse)
def find_by_id(id:int, db: Session = Depends(get_db)):
    video = db.execute(select(Video).where(Video.id == id)).scalar_one_or_none()
    
    if not video:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="No se ha encontrado el video con id {id}"
        )
        
    return video

#POST - Crear un nuevo video

@app.post("/api/videos", response_model=VideoResponse,status_code=status.HTTP_201_CREATED)
def create(video_dto: VideoCreate, db:Session = Depends(get_db)):
    if not video_dto.title.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El titulo del video no puede estar vacio"
        
    )
    
    if not video_dto.channel.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El canal no puede estar vacio"
        )
    
   
    if video_dto.views is not None and video_dto.views < 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,                    
            detail="Las visualizaciones no pueden ser menores que 0")
        
    # crear objeto video
    
    video = Video(
        title = video_dto.title.strip(),
        channel = video_dto.channel.strip(),
        views = video_dto.views,
        has_subtitles = video_dto.has_subtitles
    )
    
    db.add(video)
    db.commit()
    db.refresh(video)
    return video


#PUT -actualizar COMPLETAMENTE una cancion
@app.put("/api/videos/{id}", response_model=VideoResponse)
def actualizacion_completa(id: int, video_dto: VideoUpdate, db: Session = Depends(get_db)):
    #busca video por id
    
    video = db.execute(
        select(Video).where(Video.id == id)).scalar_one_or_none()
    #si no existe devuelve 404
    
    if not video:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No se ha encontrado el video con el id {id}"
        )
    #validaciones igual que en el create
    
    if not video_dto.title.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El titulo del video no puede estar vacio"
        
    )
    
    if not video_dto.channel.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El canal no puede estar vacio"
        )
    
   
    if video_dto.views is not None and video_dto.views < 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,                    
            detail="Las visualizaciones no pueden ser menores que 0")
        
    # ponemos los datos actualizados
    
    video.title= video_dto.title.strip()
    video.channel = video_dto.channel.strip()
    video.views = video_dto.views
    video.has_subtitles = video_dto.has_subtitles
    
    
    db.commit()
    db.refresh(video)
    return video


#PATCH - actualizar PARCIALMENTE un video





#DELETE -eliminar un video
@app.delete("/api/videos/{id}",status_code=status.HTTP_204_NO_CONTENT)
def borrrar_por_id(id:int, db: Session=Depends(get_db)):
    #busca por id
    video = db.execute(
        select(Video).where(Video.id==id)
    ).scalar_one_or_none()
    
    #si no existe, devuelve 404
    if not video:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No se ha encontrado el video con el id {id}"
        )
    
    #elimina el video
    db.delete(video)
    db.commit()
    return None

        