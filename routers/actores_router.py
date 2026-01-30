"""
Router REST API para gestión de actores
"""
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from data.database import database
from data.actor_repository import ActorRepository
from domain.model.Actor import Actor
from utils.dependencies import require_auth, require_auth_admin

# Crear el router
router = APIRouter(prefix="/api/actores", tags=["actores"])


# Modelo Pydantic para recibir datos
class ActorCreate(BaseModel):
    nombre: str


class ActorResponse(BaseModel):
    id: int
    nombre: str


@router.get("", response_model=list[ActorResponse])
async def listar_actores(usuario: dict = Depends(require_auth)):
    """
    Obtener lista de todos los actores
    Requiere autenticación
    """
    actor_repo = ActorRepository()
    actores = actor_repo.get_all(database)
    
    return [{"id": actor.id, "nombre": actor.nombre} for actor in actores]


@router.get("/{actor_id}", response_model=ActorResponse)
async def obtener_actor(actor_id: int, usuario: dict = Depends(require_auth)):
    """
    Obtener un actor por ID
    Requiere autenticación
    """
    actor_repo = ActorRepository()
    actor = actor_repo.get_by_id(database, actor_id)
    
    if not actor:
        raise HTTPException(status_code=404, detail="Actor no encontrado")
    
    return {"id": actor.id, "nombre": actor.nombre}


@router.post("", response_model=ActorResponse, status_code=201)
async def crear_actor(
    actor_data: ActorCreate,
    usuario: dict = Depends(require_auth_admin)
):
    """
    Crear un nuevo actor
    Requiere rol de administrador
    """
    actor_repo = ActorRepository()
    actor = Actor(0, actor_data.nombre)
    actor_repo.insertar_actor(database, actor)
    
    # Obtener el actor recién creado para devolver su ID
    actores = actor_repo.get_all(database)
    nuevo_actor = actores[-1]  # El último insertado
    
    return {"id": nuevo_actor.id, "nombre": nuevo_actor.nombre}


@router.put("/{actor_id}", response_model=ActorResponse)
async def actualizar_actor(
    actor_id: int,
    actor_data: ActorCreate,
    usuario: dict = Depends(require_auth_admin)
):
    """
    Actualizar un actor
    Requiere rol de administrador
    """
    actor_repo = ActorRepository()
    
    # Verificar que existe
    actor = actor_repo.get_by_id(database, actor_id)
    if not actor:
        raise HTTPException(status_code=404, detail="Actor no encontrado")
    
    actor_repo.actualizar_actor(database, actor_id, actor_data.nombre)
    
    return {"id": actor_id, "nombre": actor_data.nombre}


@router.delete("/{actor_id}", status_code=204)
async def eliminar_actor(
    actor_id: int,
    usuario: dict = Depends(require_auth_admin)
):
    """
    Eliminar un actor
    Requiere rol de administrador
    """
    actor_repo = ActorRepository()
    
    # Verificar que existe
    actor = actor_repo.get_by_id(database, actor_id)
    if not actor:
        raise HTTPException(status_code=404, detail="Actor no encontrado")
    
    actor_repo.borrar_actor(database, actor_id)
    return None
