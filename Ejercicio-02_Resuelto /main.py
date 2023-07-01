"""Users CRUD API"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

database = {}


class User(BaseModel):
    id: int
    name: str
    email: str
    age: int


@app.get("/")
# Ruta raiz para comprovar que la api esta activa
def root():
    """Api root endnpoint health-check (health-check = comprovacion de estado)"""
    return {"success": True}


@app.post("/users")
def create_user(user: User):
    # Simulamos la creacion del usuario en la base de datos
    database[user.id] = user
    # Devolvemos un mensaje para hacer saber que el usuario se ha creado correctamente
    return {"message": "Usuario creado correctamente"}


@app.get("/users")
def get_all_users(name: str = None, email: str = None, age: int = None):
    # Lista para almacenar los usuarios filtrados
    filtered_users = []

    # Iterar sobre todos los usuarios en la base de datos
    for user in database.values():
        # Verificar si se proporcionan tanto el nombre, el correo electrónico y la edad
        if name and email and age:
            # Si el nombre, el correo electrónico y la edad coinciden con los proporcionados, se agrega el usuario a la lista filtrada
            if user.name == name and user.email == email and user.age == age:
                filtered_users.append(user)
        # Verificar si se proporciona solo el nombre y la edad
        elif name and age:
            # Si el nombre y la edad coinciden con los proporcionados, se agrega el usuario a la lista filtrada
            if user.name == name and user.age == age:
                filtered_users.append(user)
        # Verificar si se proporciona solo el correo electrónico y la edad
        elif email and age:
            # Si el correo electrónico y la edad coinciden con los proporcionados, se agrega el usuario a la lista filtrada
            if user.email == email and user.age == age:
                filtered_users.append(user)
        # Verificar si se proporciona solo el nombre
        elif name:
            # Si el nombre coincide con el proporcionado, se agrega el usuario a la lista filtrada
            if user.name == name:
                filtered_users.append(user)
        # Verificar si se proporciona solo el correo electrónico
        elif email:
            # Si el correo electrónico coincide con el proporcionado, se agrega el usuario a la lista filtrada
            if user.email == email:
                filtered_users.append(user)
        # Verificar si se proporciona solo la edad
        elif age:
            # Si la edad coincide con la proporcionada, se agrega el usuario a la lista filtrada
            if user.age == age:
                filtered_users.append(user)
        # Si no se proporcionan ni el nombre, el correo electrónico ni la edad, se agrega el usuario a la lista filtrada
        else:
            filtered_users.append(user)
    # Devolver la lista de usuarios filtrados
    return filtered_users


@app.get("/users/{user_id}")
def get_user(user_id: int = None, email: str = None):
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
