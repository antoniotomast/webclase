# Sistema de Gestión de Actores - React + FastAPI

Sistema de gestión de actores con autenticación de usuarios. Los usuarios pueden ver actores, mientras que los administradores pueden añadir, actualizar y eliminar actores.

## 🏗️ Arquitectura

- **Frontend**: React 18 + Vite + React Router
- **Backend**: FastAPI (Python) - REST API
- **Base de Datos**: MySQL
- **Autenticación**: Sesiones con cookies

## 📋 Características

### Autenticación
- ✅ Registro de usuarios
- ✅ Login/Logout
- ✅ Sesiones persistentes
- ✅ Protección de rutas

### Gestión de Actores
- ✅ **Usuarios**: Solo pueden ver la lista de actores
- ✅ **Administradores**: Pueden ver, añadir y eliminar actores

## 📁 Estructura del Proyecto

```
webclase/
├── frontend/                 # Aplicación React
│   ├── src/
│   │   ├── components/      # Componentes reutilizables
│   │   │   ├── Navbar.jsx
│   │   │   ├── PrivateRoute.jsx
│   │   │   └── AdminRoute.jsx
│   │   ├── context/         # Context API
│   │   │   └── AuthContext.jsx
│   │   ├── pages/           # Páginas/Vistas
│   │   │   ├── Login.jsx
│   │   │   ├── Register.jsx
│   │   │   ├── Home.jsx
│   │   │   ├── Actores.jsx
│   │   │   ├── InsertarActor.jsx
│   │   │   └── BorrarActor.jsx
│   │   ├── services/        # Servicios API
│   │   │   └── api.js
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── index.css
│   ├── package.json
│   └── vite.config.js
│
├── routers/                 # Routers de la API REST
│   ├── auth_router_api.py  # Autenticación
│   └── actores_router.py   # CRUD de actores
│
├── data/                    # Repositorios
│   ├── database.py
│   ├── usuario_repository.py
│   └── actor_repository.py
│
├── domain/model/           # Modelos de dominio
│   ├── Usuario.py
│   └── Actor.py
│
├── utils/                  # Utilidades
│   ├── session.py
│   └── dependencies.py
│
├── sql/                    # Scripts SQL
│   ├── create_usuarios_table.sql
│   └── create_actores_table.sql
│
├── main.py                 # Punto de entrada de FastAPI
└── requirements.txt        # Dependencias de Python
```

## 🚀 Instalación y Configuración

### Requisitos Previos
- Python 3.8+
- Node.js 18+ y npm
- MySQL

### 1. Configurar la Base de Datos

```sql
-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS webclase;
USE webclase;

-- Ejecutar los scripts SQL
-- sql/create_usuarios_table.sql
-- sql/create_actores_table.sql
```

### 2. Configurar el Backend (FastAPI)

```bash
# Instalar dependencias de Python
pip install -r requirements.txt

# Crear usuario administrador (opcional)
python crear_usuario_inicial.py

# Ejecutar el servidor
python main.py
```

El backend estará disponible en: `http://localhost:8000`

### 3. Configurar el Frontend (React)

```bash
# Navegar a la carpeta frontend
cd frontend

# Instalar dependencias
npm install

# Ejecutar el servidor de desarrollo
npm run dev
```

El frontend estará disponible en: `http://localhost:3000`

## 🔑 Credenciales por Defecto

Si ejecutaste `crear_usuario_inicial.py`:
- **Usuario**: admin
- **Contraseña**: admin123

## 📡 Endpoints de la API

### Autenticación (`/api/auth`)

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/auth/me` | Obtener usuario actual |
| POST | `/api/auth/login` | Iniciar sesión |
| POST | `/api/auth/registro` | Registrar nuevo usuario |
| GET | `/api/auth/logout` | Cerrar sesión |

### Actores (`/api/actores`)

| Método | Endpoint | Descripción | Permisos |
|--------|----------|-------------|----------|
| GET | `/api/actores` | Listar todos los actores | Autenticado |
| GET | `/api/actores/{id}` | Obtener un actor por ID | Autenticado |
| POST | `/api/actores` | Crear un nuevo actor | Admin |
| DELETE | `/api/actores/{id}` | Eliminar un actor | Admin |

## 🛡️ Sistema de Permisos

### Usuario Regular
- ✅ Ver lista de actores
- ❌ Añadir actores
- ❌ Eliminar actores

### Administrador (username === 'admin')
- ✅ Ver lista de actores
- ✅ Añadir actores
- ✅ Eliminar actores

## 🔧 Desarrollo

### Backend
```bash
# Modo desarrollo con recarga automática
python main.py
```

### Frontend
```bash
cd frontend
npm run dev
```

### Build para Producción

**Frontend:**
```bash
cd frontend
npm run build
```

Los archivos de producción estarán en `frontend/dist/`

## 📝 Archivos de Configuración Importantes

### `frontend/vite.config.js`
Configura el proxy para enviar peticiones `/api` al backend:
```javascript
proxy: {
  '/api': {
    target: 'http://localhost:8000',
    changeOrigin: true,
  }
}
```

### `main.py`
Configura CORS para permitir peticiones desde React:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## 🐛 Solución de Problemas

### Error de CORS
- Verifica que el backend tenga configurado CORS correctamente
- Asegúrate de que `allow_credentials=True` en el middleware CORS

### Error de autenticación
- Verifica que las cookies estén habilitadas
- Comprueba que `withCredentials: true` esté en axios

### Base de datos
- Verifica las credenciales en `data/database.py`
- Asegúrate de que MySQL esté corriendo
- Ejecuta los scripts SQL de inicialización

## 📚 Tecnologías Utilizadas

### Frontend
- React 18
- React Router v6
- Axios
- Vite

### Backend
- FastAPI
- Pydantic
- bcrypt (hashing de contraseñas)
- MySQL Connector

## 👤 Autor

Proyecto educativo de gestión de actores con autenticación.

## 📄 Licencia

Este proyecto es de uso educativo.
