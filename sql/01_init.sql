-- Script de inicialización para Docker
CREATE DATABASE IF NOT EXISTS oscar;
USE oscar;

-- Crear tabla de usuarios
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARBINARY(255) NOT NULL,
    email VARCHAR(100),
    role VARCHAR(20) DEFAULT 'user',
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_username (username)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Crear tabla de actores
CREATE TABLE IF NOT EXISTS actores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    edad INT,
    nacionalidad VARCHAR(50),
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_nombre (nombre)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Insertar usuario admin (contraseña: admin123)
INSERT INTO usuarios (username, password_hash, email, role) VALUES 
('admin', 0x243262243132244653545778506756506D3677782E73395438636B37654761424D2F4F61336E4A53794C574B79382E56306B595361626439566E4261, 'admin@example.com', 'admin')
ON DUPLICATE KEY UPDATE username=username;

-- Insertar 5 actores de ejemplo
INSERT INTO actores (nombre, edad, nacionalidad) VALUES
('Leonardo DiCaprio', 49, 'Estadounidense'),
('Robert De Niro', 80, 'Estadounidense'),
('Scarlett Johansson', 39, 'Estadounidense'),
('Denzel Washington', 69, 'Estadounidense'),
('Meryl Streep', 74, 'Estadounidense');
