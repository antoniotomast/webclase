from domain.model.Actor import Actor


class ActorRepository:

    def get_all(self, db) -> list[Actor]:
        cursor = db.cursor()
    
        cursor.execute("SELECT * FROM actores")

        actores_en_db = cursor.fetchall()
        actores: list[Actor] = list()
        for actor in actores_en_db:
            actor_obj = Actor(actor[0], actor[1])
            actores.append(actor_obj)
        cursor.close()
        
        return actores
    
    def insertar_actor(self, db, actor: Actor) -> None:
        cursor = db.cursor()
    
        cursor.execute("INSERT INTO actores (nombre) VALUES (%s)", (actor.nombre,))

        db.commit()
        cursor.close()

    def borrar_actor(self, db, id: int) -> None:
        cursor = db.cursor()

        cursor.execute("DELETE FROM actores WHERE id = %s", (id,))

        db.commit()
        cursor.close()
    
    def get_by_id(self, db, id: int) -> Actor:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM actores WHERE id = %s", (id,))
        actor_db = cursor.fetchone()
        cursor.close()
        
        if actor_db:
            return Actor(actor_db[0], actor_db[1])
        return None
    
    def actualizar_actor(self, db, id: int, nombre: str) -> None:
        cursor = db.cursor()
        cursor.execute("UPDATE actores SET nombre = %s WHERE id = %s", (nombre, id))
        db.commit()
        cursor.close()
