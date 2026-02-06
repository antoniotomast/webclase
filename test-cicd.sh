#!/bin/bash

# Script para probar el flujo de CI/CD
# Este script te ayuda a verificar que todo esté configurado correctamente

echo "==================================="
echo "Verificación del Sistema CI/CD"
echo "==================================="
echo ""

# 1. Verificar archivos necesarios
echo "✓ Verificando archivos necesarios..."
if [ -f ".github/workflows/docker-publish.yml" ]; then
    echo "  ✅ GitHub Actions workflow encontrado"
else
    echo "  ❌ Falta el archivo .github/workflows/docker-publish.yml"
fi

if [ -f "docker-compose.yml" ]; then
    echo "  ✅ docker-compose.yml encontrado"
else
    echo "  ❌ Falta el archivo docker-compose.yml"
fi

if [ -f "Dockerfile.backend" ]; then
    echo "  ✅ Dockerfile.backend encontrado"
else
    echo "  ❌ Falta el archivo Dockerfile.backend"
fi

if [ -f "Dockerfile.frontend" ]; then
    echo "  ✅ Dockerfile.frontend encontrado"
else
    echo "  ❌ Falta el archivo Dockerfile.frontend"
fi

echo ""
echo "==================================="
echo "Próximos Pasos:"
echo "==================================="
echo "1. Configura los secrets en GitHub:"
echo "   - DOCKERHUB_USERNAME"
echo "   - DOCKERHUB_TOKEN"
echo ""
echo "2. Haz push a GitHub:"
echo "   git add ."
echo "   git commit -m 'Configurar CI/CD con GitHub Actions y Watchtower'"
echo "   git push origin main"
echo ""
echo "3. Verifica GitHub Actions:"
echo "   - Ve a la pestaña 'Actions' en GitHub"
echo "   - Observa el workflow ejecutándose"
echo ""
echo "4. Inicia el sistema en tu servidor:"
echo "   docker-compose up -d"
echo ""
echo "5. Monitorea Watchtower:"
echo "   docker logs webclase-watchtower -f"
echo ""
echo "==================================="
echo "Documentación completa en README_CI_CD.md"
echo "==================================="
