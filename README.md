# DevOps Web - Aplicación de Despliegue

Esta es una aplicación web para la gestión y despliegue de aplicaciones web utilizando prácticas DevOps.

## 🚀 Características

- **Despliegue Automatizado**: Sistema de despliegue automatizado con Docker
- **CI/CD Pipeline**: Integración continua con GitHub Actions
- **Monitorización**: Panel de control para seguimiento en tiempo real
- **Documentación**: Guías completas de instalación y uso

## 📋 Requisitos

- Docker 20.10+
- Git
- Navegador web moderno
- Servidor web (nginx/apache) para producción

## 🔧 Instalación

### Opción 1: Ejecución Local

```bash
# Clonar el repositorio
git clone https://github.com/antoniotomast/webclase.git
cd webclase

# Abrir index.html en el navegador
open index.html
```

### Opción 2: Con Docker

```bash
# Construir la imagen
docker build -t devops-web .

# Ejecutar el contenedor
docker run -d -p 8080:80 devops-web

# Acceder a http://localhost:8080
```

### Opción 3: Con servidor web

```bash
# Con Python
python -m http.server 8000

# Con Node.js
npx http-server -p 8000

# Con PHP
php -S localhost:8000
```

## 📁 Estructura del Proyecto

```
webclase/
├── index.html          # Página principal
├── styles.css          # Estilos CSS
├── script.js           # Funcionalidad JavaScript
├── Dockerfile          # Configuración Docker
├── .github/
│   └── workflows/
│       └── deploy.yml  # Pipeline CI/CD
└── README.md           # Documentación
```

## 🐳 Docker

El proyecto incluye un Dockerfile para facilitar el despliegue:

```dockerfile
docker build -t devops-web .
docker run -p 8080:80 devops-web
```

## 🔄 CI/CD

El proyecto utiliza GitHub Actions para automatizar:
- Construcción de la aplicación
- Pruebas automatizadas
- Despliegue automático
- Notificaciones de estado

## 📊 Características del Panel

- **Estado del Sistema**: Monitorización en tiempo real
- **Registro de Actividad**: Logs detallados de operaciones
- **Despliegue Rápido**: Botón para iniciar despliegues
- **Documentación Integrada**: Guías y comandos útiles

## 🎨 Tecnologías

- HTML5
- CSS3 (Grid, Flexbox, Variables CSS)
- JavaScript (ES6+)
- Docker
- GitHub Actions

## 📝 Uso

1. Abre la aplicación en tu navegador
2. Navega por las diferentes secciones
3. Usa el botón "Ver Estado" para consultar el estado del sistema
4. Usa el botón "Iniciar Despliegue" para simular un despliegue

## 🤝 Contribuir

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## 👥 Autor

Antonio Tomas

## 🔗 Enlaces

- [Repositorio GitHub](https://github.com/antoniotomast/webclase)
- [Documentación Docker](https://docs.docker.com/)
- [GitHub Actions](https://docs.github.com/en/actions)