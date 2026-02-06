# Configuración de CI/CD con GitHub Actions y Watchtower

## ✅ Configuración Completada

Este proyecto ya está configurado para:
1. **GitHub Actions**: Construye y publica imágenes Docker automáticamente
2. **Watchtower**: Monitorea y actualiza contenedores cuando detecta nuevas imágenes

## 📋 Pasos para Activar el Sistema

### 1. Configurar Secrets en GitHub

Ve a tu repositorio en GitHub y configura los siguientes secrets:

1. Ve a: **Settings** → **Secrets and variables** → **Actions**
2. Haz clic en **"New repository secret"**
3. Añade estos dos secrets:

   - **DOCKERHUB_USERNAME**: Tu nombre de usuario de DockerHub (ej: `att360`)
   - **DOCKERHUB_TOKEN**: Un token de acceso de DockerHub
   
#### Cómo crear el DOCKERHUB_TOKEN:
1. Ve a https://hub.docker.com/settings/security
2. Clic en **"New Access Token"**
3. Dale un nombre (ej: "GitHub Actions")
4. Selecciona permisos: **"Read, Write, Delete"**
5. Copia el token generado y úsalo como `DOCKERHUB_TOKEN`

### 2. Cómo Funciona el Sistema

#### Flujo Automático:
```
1. Haces push a GitHub (rama main/master)
   ↓
2. GitHub Actions se activa automáticamente
   ↓
3. Construye las imágenes Docker (backend y frontend)
   ↓
4. Publica las imágenes en DockerHub con tag "latest"
   ↓
5. Watchtower (corriendo en tu servidor) detecta la nueva imagen
   ↓
6. Watchtower detiene los contenedores antiguos
   ↓
7. Watchtower descarga la nueva imagen
   ↓
8. Watchtower inicia los contenedores con la nueva versión
```

### 3. Configuración de Watchtower

Tu `docker-compose.yml` ya incluye Watchtower con esta configuración:

- ✅ **Intervalo**: 60 segundos (revisa cada minuto si hay nuevas imágenes)
- ✅ **Limpieza automática**: Elimina imágenes antiguas
- ✅ **Reinicio progresivo**: Actualiza un contenedor a la vez
- ✅ **Solo contenedores etiquetados**: Solo actualiza backend y frontend

### 4. Iniciar el Sistema

```bash
# En tu servidor/máquina donde correrá la aplicación
docker-compose up -d
```

Watchtower empezará a monitorear automáticamente.

### 5. Verificar que Funciona

#### Ver logs de Watchtower:
```bash
docker logs webclase-watchtower -f
```

Deberías ver mensajes como:
```
time="..." level=info msg="Checking containers for updated images"
time="..." level=info msg="Found new image: att360/webclase-backend:latest"
time="..." level=info msg="Stopping container: webclase-backend"
time="..." level=info msg="Starting container: webclase-backend"
```

#### Ver el progreso de GitHub Actions:
1. Ve a tu repositorio en GitHub
2. Clic en la pestaña **"Actions"**
3. Verás el workflow ejecutándose en cada push

### 6. Comandos Útiles

```bash
# Ver logs de Watchtower
docker logs webclase-watchtower -f

# Forzar actualización inmediata
docker exec webclase-watchtower /watchtower --run-once

# Ver estado de contenedores
docker-compose ps

# Ver logs de backend
docker logs webclase-backend -f

# Ver logs de frontend
docker logs webclase-frontend -f

# Reiniciar todo el sistema
docker-compose restart
```

### 7. Cambiar la Frecuencia de Actualización

Si quieres que Watchtower revise con más o menos frecuencia:

En `docker-compose.yml`, cambia:
```yaml
environment:
  - WATCHTOWER_POLL_INTERVAL=300  # 300 segundos = 5 minutos
```

### 8. Notificaciones (Opcional)

Para recibir notificaciones cuando Watchtower actualiza contenedores, puedes añadir:

```yaml
watchtower:
  environment:
    - WATCHTOWER_NOTIFICATIONS=slack
    - WATCHTOWER_NOTIFICATION_SLACK_HOOK_URL=tu_webhook_url
```

O para email:
```yaml
watchtower:
  environment:
    - WATCHTOWER_NOTIFICATIONS=email
    - WATCHTOWER_NOTIFICATION_EMAIL_FROM=tu@email.com
    - WATCHTOWER_NOTIFICATION_EMAIL_TO=tu@email.com
    - WATCHTOWER_NOTIFICATION_EMAIL_SERVER=smtp.gmail.com
    - WATCHTOWER_NOTIFICATION_EMAIL_SERVER_PORT=587
    - WATCHTOWER_NOTIFICATION_EMAIL_SERVER_USER=tu@email.com
    - WATCHTOWER_NOTIFICATION_EMAIL_SERVER_PASSWORD=tu_password
```

## 🎯 Resumen

Con esta configuración:
- ✅ Cada push a GitHub construye y publica imágenes automáticamente
- ✅ Watchtower detecta las nuevas imágenes cada 60 segundos
- ✅ Los contenedores se actualizan automáticamente sin intervención manual
- ✅ Las imágenes antiguas se limpian automáticamente
- ✅ Sistema totalmente automatizado de CI/CD

## 🔍 Solución de Problemas

### GitHub Actions no se ejecuta:
- Verifica que el workflow esté en `.github/workflows/docker-publish.yml`
- Asegúrate de que los secrets estén configurados correctamente
- Revisa la pestaña "Actions" para ver errores

### Watchtower no actualiza:
- Verifica que esté corriendo: `docker ps | grep watchtower`
- Revisa los logs: `docker logs webclase-watchtower -f`
- Asegúrate de que las imágenes tengan el label correcto

### Las imágenes no se publican:
- Verifica tus credenciales de DockerHub
- Confirma que el token tenga permisos de escritura
- Revisa los logs de GitHub Actions
