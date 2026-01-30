# WebClase - Full Stack Application

Aplicación full stack con FastAPI (backend) y React (frontend).

## 🐳 Docker Images

Las imágenes Docker se construyen automáticamente con GitHub Actions:

- **Backend**: `ghcr.io/TU_USUARIO/webclase-backend:latest`
- **Frontend**: `ghcr.io/TU_USUARIO/webclase-frontend:latest`

## 🚀 Despliegue

### 1. Subir a GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/TU_REPO.git
git push -u origin main
```

### 2. Las imágenes Docker se construyen automáticamente

GitHub Actions detectará el push y:
- Construirá las imágenes del backend y frontend
- Las subirá a GitHub Container Registry
- Estarán disponibles en: `ghcr.io/TU_USUARIO/TU_REPO-backend:latest`

### 3. Ver las imágenes

Ir a tu repositorio → Packages

### 4. Usar las imágenes

```bash
# Descargar la imagen del backend
docker pull ghcr.io/TU_USUARIO/TU_REPO-backend:latest

# Descargar la imagen del frontend
docker pull ghcr.io/TU_USUARIO/TU_REPO-frontend:latest

# Ejecutar
docker run -p 8000:8000 ghcr.io/TU_USUARIO/TU_REPO-backend:latest
docker run -p 3000:3000 ghcr.io/TU_USUARIO/TU_REPO-frontend:latest
```

### 5. Usar con docker-compose

```yaml
services:
  backend:
    image: ghcr.io/TU_USUARIO/TU_REPO-backend:latest
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=sqlite:///./data/webclase.db
      - SECRET_KEY=tu_clave_secreta
  
  frontend:
    image: ghcr.io/TU_USUARIO/TU_REPO-frontend:latest
    ports:
      - "3000:3000"
    depends_on:
      - backend
```

## 📦 Estructura del Proyecto

```
├── backend (FastAPI)
│   ├── main.py
│   ├── routers/
│   ├── data/
│   └── domain/
├── frontend (React + Vite)
│   ├── src/
│   ├── package.json
│   └── vite.config.js
├── Dockerfile.backend
├── Dockerfile.frontend
└── docker-compose.yml
```

## 🔧 Desarrollo Local

```bash
# Backend
pip install -r requirements.txt
uvicorn main:app --reload

# Frontend
cd frontend
npm install
npm run dev
```

## 📝 Notas

- Las imágenes se actualizan automáticamente con cada push a `main`
- Las imágenes están en GitHub Container Registry (público por defecto)
- Puedes hacer pull de las imágenes desde cualquier lugar
