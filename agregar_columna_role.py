"""
Script para agregar la columna 'role' a la tabla usuarios existente
y actualizar el usuario 'admin' para que tenga role='admin'
"""
from data.database import database

def agregar_columna_role():
    cursor = database.cursor()
    
    try:
        # Agregar columna role si no existe
        print("Agregando columna 'role' a la tabla usuarios...")
        cursor.execute("""
            ALTER TABLE usuarios 
            ADD COLUMN IF NOT EXISTS role VARCHAR(20) DEFAULT 'user'
        """)
        database.commit()
        print("✓ Columna 'role' agregada exitosamente")
        
        # Actualizar usuario admin existente
        print("\nActualizando usuarios con username 'admin' para que tengan role='admin'...")
        cursor.execute("""
            UPDATE usuarios 
            SET role = 'admin' 
            WHERE username = 'admin' AND (role IS NULL OR role = 'user')
        """)
        database.commit()
        rows_affected = cursor.rowcount
        print(f"✓ {rows_affected} usuario(s) actualizado(s) a role='admin'")
        
        # Mostrar todos los usuarios y sus roles
        print("\nUsuarios en la base de datos:")
        cursor.execute("SELECT id, username, email, role FROM usuarios")
        usuarios = cursor.fetchall()
        
        for usuario in usuarios:
            print(f"  - ID: {usuario[0]}, Username: {usuario[1]}, Email: {usuario[2]}, Role: {usuario[3]}")
        
    except Exception as e:
        database.rollback()
        print(f"✗ Error: {e}")
    finally:
        cursor.close()
        database.close()

if __name__ == "__main__":
    agregar_columna_role()
