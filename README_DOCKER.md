# 🐳 Guía Docker - WebClase

## Requisitos Previos
- Docker Desktop instalado y ejecutándose
- Puertos 3000 y 8000 disponibles

## 🚀 Levantar la Aplicación

### Opción 1: Construir y levantar todo
```bash
docker-compose up --build
```

### Opción 2: Solo levantar (si ya está construido)
```bash
docker-compose up
```

### Opción 3: En segundo plano (detached mode)
```bash
docker-compose up -d
```

## 🔍 Ver Logs
```bash
# Ver logs de todos los servicios
docker-compose logs -f

# Ver logs solo del backend
docker-compose logs -f backend

# Ver logs solo del frontend
docker-compose logs -f frontend
```

## 🛑 Detener la Aplicación

### Detener contenedores
```bash
docker-compose down
```

### Detener y eliminar volúmenes
```bash
docker-compose down -v
```

## 🌐 Acceder a la Aplicación

- **Frontend (React)**: http://localhost:3000
- **Backend (API)**: http://localhost:8000
- **Documentación API**: http://localhost:8000/docs

## 🔧 Comandos Útiles

### Ver contenedores en ejecución
```bash
docker ps
```

### Reconstruir sin caché
```bash
docker-compose build --no-cache
```

### Acceder al contenedor del backend
```bash
docker exec -it webclase-backend bash
```

### Acceder al contenedor del frontend
```bash
docker exec -it webclase-frontend sh
```

## 🐛 Solución de Problemas

### Puerto ocupado
Si el puerto 3000 o 8000 está ocupado:
1. Detén el proceso que lo está usando
2. O cambia el puerto en `docker-compose.yml`:
   ```yaml
   ports:
     - "OTRO_PUERTO:3000"
   ```

### Error de CORS
Si hay problemas de CORS, verifica que `main.py` tenga configurado:
```python
allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"]
```

### Base de datos no persiste
Los datos se guardan en el volumen `./data`. Asegúrate de no usar `docker-compose down -v` si quieres mantener los datos.

### Problemas de red entre contenedores
Los contenedores usan la red `webclase-network` y se comunican por sus nombres de servicio:
- Backend: `http://backend:8000`
- Frontend: `http://frontend:3000`

## 📝 Notas

- El frontend usa el proxy de Vite para redirigir las peticiones `/api` al backend
- Los cambios en el código requieren reconstruir la imagen: `docker-compose up --build`
- Para desarrollo local sin Docker, sigue usando `uvicorn main:app --reload` y `npm run dev`
