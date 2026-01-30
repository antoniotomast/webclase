from typing import Annotated
from fastapi import APIRouter, Request, Form, Depends, HTTPException
from pydantic import BaseModel
from data.database import database
from data.usuario_repository import UsuarioRepository
from utils.session import crear_sesion, destruir_sesion, obtener_usuario_actual

# Crear el router
router = APIRouter(prefix="/api/auth", tags=["autenticacion"])


# Modelos Pydantic
class LoginResponse(BaseModel):
    user: dict
    message: str


class ErrorResponse(BaseModel):
    detail: str


@router.get("/me")
async def obtener_usuario_autenticado(request: Request):
    """Obtiene el usuario actual autenticado"""
    usuario = obtener_usuario_actual(request)
    
    if not usuario:
        raise HTTPException(status_code=401, detail="No autenticado")
    
    return usuario


@router.post("/login", response_model=LoginResponse)
async def do_login(
    request: Request,
    username: Annotated[str, Form()],
    password: Annotated[str, Form()]
):
    """Procesa el login y devuelve JSON"""
    usuario_repo = UsuarioRepository()
    
    # Buscar el usuario
    usuario = usuario_repo.get_by_username(database, username)
    
    if not usuario:
        raise HTTPException(status_code=401, detail="Usuario o contraseña incorrectos")
    
    # Verificar la contraseña
    if not usuario_repo.verificar_password(password, usuario.password_hash):
        raise HTTPException(status_code=401, detail="Usuario o contraseña incorrectos")
    
    # Debug: verificar tipos antes de crear sesión
    print(f"DEBUG - user_id type: {type(usuario.id)}, value: {usuario.id}")
    print(f"DEBUG - username type: {type(usuario.username)}, value: {usuario.username}")
    print(f"DEBUG - role type: {type(usuario.role)}, value: {usuario.role}")
    
    # Crear sesión
    crear_sesion(request, usuario.id, usuario.username, usuario.role)
    
    # Debug: ver qué hay en la sesión antes de retornar
    print(f"DEBUG - Sesión después de crear: {dict(request.session)}")
    for key, value in request.session.items():
        print(f"  {key}: {value} (type: {type(value).__name__})")
    
    return {
        "user": {
            "id": usuario.id,
            "username": usuario.username,
            "email": usuario.email,
            "role": usuario.role
        },
        "message": "Login exitoso"
    }


@router.post("/registro", response_model=LoginResponse)
async def do_registro(
    request: Request,
    username: Annotated[str, Form()],
    password: Annotated[str, Form()],
    password_confirm: Annotated[str, Form()],
    email: Annotated[str, Form()] = None
):
    """Procesa el registro de usuario y devuelve JSON"""
    usuario_repo = UsuarioRepository()
    
    # Validaciones
    if not username or len(username) < 3:
        raise HTTPException(
            status_code=400,
            detail="El nombre de usuario debe tener al menos 3 caracteres"
        )
    
    if not password or len(password) < 6:
        raise HTTPException(
            status_code=400,
            detail="La contraseña debe tener al menos 6 caracteres"
        )
    
    if password != password_confirm:
        raise HTTPException(status_code=400, detail="Las contraseñas no coinciden")
    
    # Verificar que el usuario no exista
    usuario_existente = usuario_repo.get_by_username(database, username)
    if usuario_existente:
        raise HTTPException(status_code=400, detail="El nombre de usuario ya existe")
    
    # Insertar el usuario
    try:
        usuario_repo.insertar_usuario(database, username, password, email)
        
        # Obtener el usuario recién creado para crear la sesión
        usuario = usuario_repo.get_by_username(database, username)
        crear_sesion(request, usuario.id, usuario.username, usuario.role)
        
        return {
            "user": {
                "id": usuario.id,
                "username": usuario.username,
                "email": usuario.email,
                "role": usuario.role
            },
            "message": "Usuario registrado exitosamente"
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error al crear el usuario: {str(e)}"
        )


@router.get("/logout")
async def logout(request: Request):
    """Cierra la sesión y devuelve JSON"""
    destruir_sesion(request)
    return {"message": "Sesión cerrada exitosamente"}
