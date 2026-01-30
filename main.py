from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
from routers import auth_router_api, actores_router
import uvicorn

# Crear la aplicación FastAPI
app = FastAPI(
    title="API REST de Gestión de Actores",
    description="API REST con autenticación para gestionar actores"
)

# ⭐ IMPORTANTE: Agregar CORS para permitir peticiones desde React
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ⭐ IMPORTANTE: Agregar el middleware de sesiones
app.add_middleware(
    SessionMiddleware,
    secret_key="tu_clave_secreta_muy_segura_cambiala_en_produccion",
    session_cookie="session",
    max_age=3600 * 24 * 7,  # 7 días
    same_site="lax",
    https_only=False  # Cambiar a True en producción con HTTPS
)

# Configurar archivos estáticos (opcional, para servir archivos)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Incluir los routers de la API REST
app.include_router(auth_router_api.router)
app.include_router(actores_router.router)


# Ruta raíz de la API
@app.get("/")
async def root():
    """Endpoint raíz de la API"""
    return {
        "message": "API REST de Gestión de Actores",
        "version": "1.0",
        "endpoints": {
            "auth": "/api/auth",
            "actores": "/api/actores"
        }
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
