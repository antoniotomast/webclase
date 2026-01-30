from typing import Annotated
from fastapi import APIRouter, Request, Form,Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from data.database import database
from data.usuario_repository import UsuarioRepository
from utils.session import crear_sesion, destruir_sesion, obtener_usuario_actual
from utils.dependencies import require_auth
import random

# Crear el routers
juego_router = APIRouter(prefix="/juego", tags=["juego"],dependencies=[Depends(require_auth)] )

# Configurar las plantillas
templates = Jinja2Templates(directory="templates")

@juego_router.get("/", response_class=HTMLResponse)
async def mostrar_juego(request: Request):
    return templates.TemplateResponse("juego.html", {"request": request})

@juego_router.post("/", response_class=HTMLResponse)
async def mostrar_juego(request: Request,
                        numero: Annotated[str, Form()] = None):
    # la primera vez que se accede no existe la variable de sesión
    if "numero_intentos" not in request.session:
        reiniciar_juego(request)



    # las siguientes veces
    request.session["numero_intentos"] += 1
    if (request.session["numero_intentos"] > 10):
        mensaje = "¡Has superado el número máximo de intentos!"

    elif (int(numero) < request.session["numero_aleatorio"]):
        mensaje = f"El número es mayor , te quedan {10 - request.session['numero_intentos']} intentos."

    elif (int(numero) > request.session["numero_aleatorio"]):
        mensaje = f"El número es menor, te quedan {10 - request.session['numero_intentos']} intentos."
    else:
        mensaje = f"¡Correcto! Has adivinado el número en {request.session['numero_intentos']} intentos."
        reiniciar_juego(request)

    return templates.TemplateResponse("juego.html", {"request": request, "mensaje": mensaje})


def reiniciar_juego(request: Request):

    request.session["numero_intentos"] = 0
    request.session["numero_aleatorio"] = random.randint(1, 100)  # Aquí podrías generar un número aleatorio


@juego_router.get("/1", response_class=HTMLResponse)
async def mostrar_juego1(request: Request,
                        numero: Annotated[str, Form()] = None):
    return templates.TemplateResponse("juego1.html", {"request": request})
