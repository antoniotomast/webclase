from fastapi import Request
from typing import Optional
from datetime import datetime

# Clave secreta para firmar las cookies de sesión (cámbiala en producción)
# Actualizado: Sistema de sesiones con Watchtower auto-deploy
SECRET_KEY = "tu_clave_secreta_muy_segura_cambiala_en_produccion"


def crear_sesion(request: Request, user_id: int, username: str, role: str = 'user'):
    """Crea una sesión guardando los datos en request.session"""
    # Limpiar la sesión completamente primero
    request.session.clear()
    
    # Guardar solo tipos básicos (int, str, bool) - forzar conversión
    request.session["user_id"] = int(user_id)
    request.session["username"] = str(username)
    request.session["role"] = str(role)
    request.session["authenticated"] = True
    
    # Verificar que no haya objetos no serializables
    for key, value in list(request.session.items()):
        if isinstance(value, datetime):
            request.session[key] = value.isoformat()
        elif not isinstance(value, (int, str, bool, float, list, dict, type(None))):
            del request.session[key]
            print(f"WARNING: Removed non-serializable key '{key}' from session")
    
    print(f"DEBUG - Sesión creada: {request.session}")
    # para logout
    #request.session.popitem("username", None)  # Elimina si existe


def obtener_sesion(request: Request) -> Optional[dict]:
    """Obtiene los datos de la sesión"""
    if not request.session or not request.session.get("authenticated"):
        return None
    
    return {
        "user_id": request.session.get("user_id"),
        "username": request.session.get("username"),
        "role": request.session.get("role", "user")
    }


def destruir_sesion(request: Request):
    """Destruye la sesión limpiando los datos"""
    request.session.clear()


def usuario_autenticado(request: Request) -> bool:
    """Verifica si hay un usuario autenticado"""
    sesion = obtener_sesion(request)
    return sesion is not None


def obtener_usuario_actual(request: Request) -> Optional[dict]:
    """Obtiene el usuario actual de la sesión"""
    return obtener_sesion(request)
