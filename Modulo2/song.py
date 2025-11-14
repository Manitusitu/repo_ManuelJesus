from fastapi import Depends, FastAPI, HTTPException, status
from pydantic import BaseModel, ConfigDict
from sqlalchemy import create_engine, Integer, String, Boolean, select
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column, Session

#configurar base de datos


#crear motor de conexión a base de datos
engine = create_engine(
    "sqlite:///Modulo2/cancioncitas.db",
    echo=True,
    connect_args={"check_same_thread": False}
)

#crear fábrica de sesiones de bases de datos

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=True,
    expire_on_commit=False
)

#modelo base de datos (sqlalchemy)

#clase base para modelos sqlalchemy
class Base(DeclarativeBase):
    pass

# modelo de la tabla song (se crea un solo modelo,
# que sera una tabla en nuestra
# base de datos)

class Song(Base):
  __tablename__ = "songs" # nombre de la tabla en bd
  
  #clave primaria
  id: Mapped[int]  = mapped_column(Integer, primary_key=True, autoincrement=True)
  #requerido, maximo 200 caracteres(al poner nullable en false
  #lo hacemos un campo obligatorio)
  title: Mapped[str] = mapped_column(String(200),nullable=False)
  #requerido, maximo 200 caracteres
  artist: Mapped[str] = mapped_column(String(200), nullable=False)
  #opcional(Por ser opcional ponemos el [])
  duration_seconds: Mapped[int | None] = mapped_column(Integer,nullable=True)
  #opcional
  explicit: Mapped [bool | None] = mapped_column(Boolean, nullable=True)


#modelos pydantic (schemas)
#modelos que validan los datos que llegan y salen de la API

#schema para TODAS las respuestas de la API
#lo usamos en GET, POST, PUT, PATCH
class SongResponse(BaseModel):
    
    model_config = ConfigDict(from_attributes=True) #Traduce los atributos de SQLAlchemy para Pydantic
    id: int
    title:str
    artist: str
    duration_seconds: int | None
    explicit: bool | None
    
#schema para CREAR una cancion (POST)
#no incluimos id porque se genera automaticamente
class SongCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    title: str
    artist: str
    duration_seconds: int | None = None
    explicit: bool | None = None

# schema para Actualizacion completa (PUT)
# todos los campos se tienen que enviar
class SongUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    title: str
    artist: str
    duration_seconds: int | None
    explicit: bool | None
    
#schema para actualizacion parcial (PATCH)
#solo se envian los campos que quieres actualizar
class SongPatch(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    title: str | None = None
    artist: str | None = None
    duration_seconds: int | None = None
    explicit: bool | None = None


#inicializacion base de datos

#crear todas las tablas
Base.metadata.create_all(engine)

#metodo inicializar con canciones por defecto

def init_db():
    """
    Inicializa con canciones por defecto, las creara solo si
    no existen en la base de datos
    """
    db = SessionLocal()
    try:
        existing_song = db.execute(select(Song)).scalars().all()
        
        if existing_song:
            return
        default_songs = [
            Song(title="Mamma Mia", artist="ABBA", duration_seconds=300, explicit=False),
            Song(title="Viva la vida", artist="Cold Play", duration_seconds=314, explicit=False),
            Song(title="Billie Jean", artist="Michael Jackson", duration_seconds=294, explicit=False),
            Song(title="Smells Like Teen Spirit", artist="Nirvana", duration_seconds=301, explicit=True),
            Song(title="Paranoid Android", artist="Radiohead", duration_seconds=386, explicit=True)
        ]
        #agregar las canciones
        db.add_all(default_songs)
        db.commit()
    finally:
        db.close()

#inicializa la base de datos con canciones por defecto
init_db()


#dependencia de fastapi


def get_db():
    db = SessionLocal()
    try:
        yield db #entrega la sesion al endpoint
    finally:
        db.close()

#aplicacion fastapi

#crea la instancia de la aplicacion FastAPI
app = FastAPI(title="Cancioncitas",version="1.0.0")


# endpoint raiz
@app.get("/")
def home():
    return {"mensaje: Bienvenido a la app Cancioncitas"}

#ENDPOINTS CRUD

#GET-Obtener todas las canciones
@app.get("/api/songs",response_model=list[SongResponse])
def find_all(db: Session = Depends(get_db)):
    #db.execute(): ejecuta la consulta
    #select(Song): crea consulta SELECT * FROM Song
    #.scarlars(): extrae los objetos Song
    #.all(): obtiene los resultados como lista
    return db.execute(select(Song)).scalars().all()

#GET- Obtener una cancion por id

@app.get("api/songs/{id}",response_model=SongResponse)
def find_by_id(id:int, db: Session =Depends(get_db)):
    song = db.execute(
        select(Song).where(Song.id == id)
    ).scalar_one_or_none()
    
    if not song:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,detail=f"No se ha encontrado la canción con id {id}"
            
        )
    return song

# POST - crear una nueva canción
@app.post("/api/songs", response_model=SongResponse, status_code=status.HTTP_201_CREATED)
def create(song_dto: SongCreate, db: Session = Depends(get_db)):
    if not song_dto.title.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El título de la canción no puede estar vacío"
        )
    
    if not song_dto.artist.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El artista de la canción no puede estar vacío"
        )
    
    if song_dto.duration_seconds is not None and song_dto.duration_seconds < 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="La duración debe ser un número positivo"
        )
    
    # crea objeto Song con datos validados
    song = Song(
        title=song_dto.title.strip(),
        artist=song_dto.artist.strip(),
        duration_seconds=song_dto.duration_seconds,
        explicit=song_dto.explicit
    )
    
    db.add(song) # agrega el objeto a la sesión
    db.commit() # confirma la creación en base de datos
    db.refresh(song) # refresca el objeto para obtener el id generado
    return song # retorna la canción creada


#PUT - actualizar COMPLETAMENTE una cancion
@app.put("/api/songs/{id}", response_model=SongResponse)
def update_full(id:int, song_dto: SongUpdate,db:Session = Depends(get_db)):
    #busca cancion por id
    
    song = db.execute(
        select(Song).where(Song.id == id)
    ).scalar_one_or_none()

    #si no existe, devuelve 404
    
    if not song:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No se ha encontrado la cancion con id {id}"
        )
    
    # validaciones (igual que en POST)
    if not song_dto.title.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El titulo de la cancion no puede estar vacio"
            )
    
    if not song_dto.artist.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El artista de la cancion no puede estar vacio"
        )
    
    if not song_dto.duration_seconds is not None and song_dto.duration_seconds < 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="La cancion debe tener un numero positivo"
        )
        
    song.title = song_dto.title.strip()
    song.artist = song_dto.artist.strip()
    song.duration_seconds = song_dto.duration_seconds
    song.explicit = song_dto.explicit
    
    db.commit() #confirma los cambios
    db.refresh(song) # refresca el objeto de la base de datos
    return song

#PATCH - actualizar PARCIALMENTE una cancion
@app.patch("/api/songs/{id}",response_model=SongResponse)
def update_parcial(id:int, song_dto: SongPatch,db:Session = Depends(get_db)):
    #busca cancion por id
    
    song = db.execute(
        select(Song).where(Song.id == id)
    ).scalar_one_or_none()

    #si no existe, devuelve 404
    
    if not song:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No se ha encontrado la cancion con id {id}"
        )
    
    #actualiza solo los campos que se han enviado (no son none)
    if song_dto.title is not None:
        if not song_dto.title.strip():
            raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El titulo de la cancion no puede estar vacio"

            )
    
        song.title = song_dto.title.strip()

                
    if song_dto.artist is not None:
        if not song_dto.artist.strip():
            raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El artista de la cancion no puede estar vacio"
            )
        song.artist = song_dto.artist.strip()
            
    if song_dto.duration_seconds is not None:
        if not song_dto.duration_seconds < 0:
            raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="La duracion de la cancion debe ser positivo"
            )
        
        song.duration_seconds = song_dto.duration_seconds
    
    if song_dto.explicit is not None:
        song.explicit = song_dto.explicit
    
    
    db.commit() #confirma los cambios
    db.refresh(song) # refresca el objeto de la base de datos
    return song


#DELETE -eliminar una cancion
@app.delete("/api/songs/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id:int, db: Session=Depends(get_db)):
    #busca la canción por ud
    song = db.execute(
        select(Song).where(Song.id==id)
    ).scalar_one_or_none()
    
    #si no existe, devuelve 404
    if not song:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No se ha encontrado la canción con id {id}"
        )
    
    # elimina la canción de base de datos
    db.delete(song) # marca el objeto para eliminación
    db.commit() # confirma la eliminación en base de datos
    return None
        

        
        
        