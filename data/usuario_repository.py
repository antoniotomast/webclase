from domain.model.Usuario import Usuario
import bcrypt


class UsuarioRepository:

    def get_by_username(self, db, username: str) -> Usuario:
        """Obtiene un usuario por su nombre de usuario"""
        cursor = db.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE username = %s", (username,))
        usuario_db = cursor.fetchone()
        cursor.close()
        
        if usuario_db:
            # Columnas: id, username, password_hash, email, role, fecha_creacion
            return Usuario(
                id=usuario_db[0],
                username=usuario_db[1],
                password_hash=usuario_db[2],
                email=usuario_db[3],
                role=usuario_db[4] if len(usuario_db) > 4 else 'user'
            )
        return None

    def get_by_id(self, db, user_id: int) -> Usuario:
        """Obtiene un usuario por su ID"""
        cursor = db.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE id = %s", (user_id,))
        usuario_db = cursor.fetchone()
        cursor.close()
        
        if usuario_db:
            # Columnas: id, username, password_hash, email, role, fecha_creacion
            return Usuario(
                id=usuario_db[0],
                username=usuario_db[1],
                password_hash=usuario_db[2],
                email=usuario_db[3],
                role=usuario_db[4] if len(usuario_db) > 4 else 'user'
            )
        return None

    def get_all(self, db) -> list[Usuario]:
        """Obtiene todos los usuarios"""
        cursor = db.cursor()
        cursor.execute("SELECT * FROM usuarios")
        usuarios_en_db = cursor.fetchall()
        usuarios: list[Usuario] = list()
        
        for usuario in usuarios_en_db:
            # Columnas: id, username, password_hash, email, role, fecha_creacion
            usuario_obj = Usuario(
                id=usuario[0],
                username=usuario[1],
                password_hash=usuario[2],
                email=usuario[3],
                role=usuario[4] if len(usuario) > 4 else 'user'
            )
            usuarios.append(usuario_obj)
        cursor.close()
        
        return usuarios

    def insertar_usuario(self, db, username: str, password: str, email: str = None, role: str = 'user') -> None:
        """Inserta un nuevo usuario con contraseña hasheada"""
        cursor = db.cursor()
        
        # Hashear la contraseña con bcrypt
        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
        cursor.execute(
            "INSERT INTO usuarios (username, password_hash, email, role) VALUES (%s, %s, %s, %s)",
            (username, password_hash, email, role)
        )
        
        db.commit()
        cursor.close()

    def verificar_password(self, password: str, password_hash: str) -> bool:
        """Verifica si la contraseña coincide con el hash"""
        # # Convertir password_hash a bytes si es necesario
        # if isinstance(password_hash, str):
        #     password_hash = password_hash.encode('utf-8')
        # elif isinstance(password_hash, bytearray):
        #     password_hash = bytes(password_hash)
        
        return bcrypt.checkpw(password.encode('utf-8'), bytes(password_hash))

    def actualizar_password(self, db, user_id: int, nueva_password: str) -> None:
        """Actualiza la contraseña de un usuario"""
        cursor = db.cursor()
        
        # Hashear la nueva contraseña
        password_hash = bcrypt.hashpw(nueva_password.encode('utf-8'), bcrypt.gensalt())
        
        cursor.execute(
            "UPDATE usuarios SET password_hash = %s WHERE id = %s",
            (password_hash, user_id)
        )
        
        db.commit()
        cursor.close()
