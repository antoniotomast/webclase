Write-Host "🔄 Esperando a que MySQL esté listo..." -ForegroundColor Cyan
Start-Sleep -Seconds 5

Write-Host "🔐 Generando hash de contraseña para admin..." -ForegroundColor Cyan
$PASSWORD_HASH = docker exec webclase-backend python -c "import bcrypt; print(bcrypt.hashpw(b'admin123', bcrypt.gensalt()).decode('utf-8'))"

Write-Host "👤 Insertando usuario admin..." -ForegroundColor Cyan
docker exec webclase-mysql mysql -uroot -proot oscar -e "INSERT INTO usuarios (username, password_hash, email, role) VALUES ('admin', '$PASSWORD_HASH', 'admin@example.com', 'admin') ON DUPLICATE KEY UPDATE password_hash='$PASSWORD_HASH', role='admin';"

Write-Host "🎬 Insertando actores..." -ForegroundColor Cyan
docker exec webclase-mysql mysql -uroot -proot oscar -e @"
INSERT INTO actores (nombre, apellidos, año_nacimiento) VALUES 
('Leonardo', 'DiCaprio', 1974),
('Meryl', 'Streep', 1949),
('Tom', 'Hanks', 1956),
('Scarlett', 'Johansson', 1984),
('Denzel', 'Washington', 1954)
ON DUPLICATE KEY UPDATE nombre=nombre;
"@

Write-Host "✅ Datos insertados correctamente!" -ForegroundColor Green
Write-Host ""
Write-Host "📊 Verificando datos..." -ForegroundColor Cyan
docker exec webclase-mysql mysql -uroot -proot oscar -e "SELECT * FROM usuarios;"
docker exec webclase-mysql mysql -uroot -proot oscar -e "SELECT * FROM actores;"
Write-Host ""
Write-Host "🔑 Credenciales de acceso:" -ForegroundColor Yellow
Write-Host "   Usuario: admin" -ForegroundColor White
Write-Host "   Contraseña: admin123" -ForegroundColor White