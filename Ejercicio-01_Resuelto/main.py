"""Users CRUD API"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str
    age: int

database = {
    0: User(id=0, name="John", email="john@gmail.com", age=20),
    1: User(id=1, name="Mike", email="mike@gmail.com", age=30),
}


@app.get("/")
# Ruta raiz para comprovar que la api esta activa
def root():
    """Api root endnpoint health-check"""
    return {"success": True}


@app.post("/users")
def create_user(user: User):
    # Simulamos la creacion del usuario en la base de datos
    database[user.id] = user
    # Devolvemos un mensaje para hacer saber que el usuario se ha creado correctamente
    return {"message": "Usuario creado correctamente"}


@app.get("/users")
def get_all_users():
    # Devolvemos la lista de todos los usuarios en la db fake de memoria
    return list(database.values())


@app.get("/users/{user_id}")
def get_user(user_id: int):
    # Recuperamos el usuario de nuestra base de datos en memoria
    user = database.get(user_id)
    # Si hemos encontrado el usuario, lo develolvemos como respuesta
    if user:
        return user
    # En caso de no encontrarlo, develovemos este mensaje
    return {"error": "Usuario no encontrado"}


@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    # Comprovamos si el usuario con el id pasado existe.
    if user_id in database:
        # En caso de existir actualizamos el usuaro con los nuevos datos.
        database[user_id] = user
        # Devolvemos un mensaje para informar de que se ha actualizado correctamente.
        return {"message": "Usuario actualizado correctamente"}
    # En caso de no encontrar el usuario, devolvemos esete mensaje
    return {"error": "Usuario no encontrado"}


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    # Comprovamos si el usuario con el id pasado existe.
    if user_id in database:
        # Elimina el usuario de la base de datos simulada
        del database[user_id]
        # Devolvemos un mensaje para informar de que se ha borrado correctamente.
        return {"message": "Usuario eliminado correctamente"}
    # En caso de no encontrar el usuario, devolvemos esete mensaje
    return {"error": "Usuario no encontrado"}
