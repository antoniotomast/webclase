# Script para verificar el sistema CI/CD
# PowerShell version

Write-Host "===================================" -ForegroundColor Cyan
Write-Host "Verificación del Sistema CI/CD" -ForegroundColor Cyan
Write-Host "===================================" -ForegroundColor Cyan
Write-Host ""

# 1. Verificar archivos necesarios
Write-Host "→ Verificando archivos necesarios..." -ForegroundColor Yellow
Write-Host ""

if (Test-Path ".github\workflows\docker-publish.yml") {
    Write-Host "  ✅ GitHub Actions workflow encontrado" -ForegroundColor Green
} else {
    Write-Host "  ❌ Falta el archivo .github\workflows\docker-publish.yml" -ForegroundColor Red
}

if (Test-Path "docker-compose.yml") {
    Write-Host "  ✅ docker-compose.yml encontrado" -ForegroundColor Green
} else {
    Write-Host "  ❌ Falta el archivo docker-compose.yml" -ForegroundColor Red
}

if (Test-Path "Dockerfile.backend") {
    Write-Host "  ✅ Dockerfile.backend encontrado" -ForegroundColor Green
} else {
    Write-Host "  ❌ Falta el archivo Dockerfile.backend" -ForegroundColor Red
}

if (Test-Path "Dockerfile.frontend") {
    Write-Host "  ✅ Dockerfile.frontend encontrado" -ForegroundColor Green
} else {
    Write-Host "  ❌ Falta el archivo Dockerfile.frontend" -ForegroundColor Red
}

Write-Host ""
Write-Host "===================================" -ForegroundColor Cyan
Write-Host "Estado de Docker" -ForegroundColor Cyan
Write-Host "===================================" -ForegroundColor Cyan

try {
    $dockerVersion = docker --version
    Write-Host "  ✅ Docker instalado: $dockerVersion" -ForegroundColor Green
} catch {
    Write-Host "  ❌ Docker no está instalado o no está en PATH" -ForegroundColor Red
}

try {
    $composeVersion = docker-compose --version
    Write-Host "  ✅ Docker Compose instalado: $composeVersion" -ForegroundColor Green
} catch {
    Write-Host "  ❌ Docker Compose no está instalado o no está en PATH" -ForegroundColor Red
}

Write-Host ""
Write-Host "===================================" -ForegroundColor Cyan
Write-Host "Próximos Pasos:" -ForegroundColor Cyan
Write-Host "===================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "1. Configura los secrets en GitHub:" -ForegroundColor Yellow
Write-Host "   • Ve a tu repositorio → Settings → Secrets and variables → Actions"
Write-Host "   • Añade: DOCKERHUB_USERNAME (tu usuario de DockerHub)"
Write-Host "   • Añade: DOCKERHUB_TOKEN (token de acceso de DockerHub)"
Write-Host ""
Write-Host "2. Haz push a GitHub:" -ForegroundColor Yellow
Write-Host "   git add ."
Write-Host "   git commit -m 'Configurar CI/CD con GitHub Actions y Watchtower'"
Write-Host "   git push origin main"
Write-Host ""
Write-Host "3. Verifica GitHub Actions:" -ForegroundColor Yellow
Write-Host "   • Ve a la pestaña 'Actions' en tu repositorio GitHub"
Write-Host "   • Observa el workflow ejecutándose"
Write-Host ""
Write-Host "4. Inicia el sistema en tu servidor:" -ForegroundColor Yellow
Write-Host "   docker-compose up -d"
Write-Host ""
Write-Host "5. Monitorea Watchtower:" -ForegroundColor Yellow
Write-Host "   docker logs webclase-watchtower -f"
Write-Host ""
Write-Host "===================================" -ForegroundColor Cyan
Write-Host "📖 Documentación completa en README_CI_CD.md" -ForegroundColor White
Write-Host "===================================" -ForegroundColor Cyan
Write-Host ""

# Preguntar si quiere iniciar docker-compose
Write-Host "¿Deseas iniciar los contenedores ahora? (S/N): " -ForegroundColor Yellow -NoNewline
$respuesta = Read-Host

if ($respuesta -eq "S" -or $respuesta -eq "s") {
    Write-Host ""
    Write-Host "Iniciando contenedores..." -ForegroundColor Green
    docker-compose up -d
    Write-Host ""
    Write-Host "✅ Contenedores iniciados. Para ver logs:" -ForegroundColor Green
    Write-Host "   docker-compose logs -f"
} else {
    Write-Host "Ok, puedes iniciar los contenedores más tarde con: docker-compose up -d" -ForegroundColor Yellow
}
