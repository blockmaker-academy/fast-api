"""Users CRUD API"""
from typing import List
from fastapi import FastAPI, HTTPException, Query, Path
from pydantic import BaseModel, constr, EmailStr, Field

app = FastAPI(
    title="Users CRUD API",
    description="API de prueba para crear, leer, actualizar y borrar usuarios",
    version="1.0.0"
)

database = {}


class User(BaseModel):
    id: int = Field(description="Id del usuario", example=1)
    name: constr(min_length=1, max_length=50) = Field(
        description="Nombre del usuario", example="John Doe")
    email: EmailStr = Field(
        description="Email del usuario", example="john@example.com")
    age: int = Field(description="Edad del usuario", example=25)


class CreateUserSuccessfulResponse(BaseModel):
    message: str = Field(
        description="Mensaje de exito en la operación",
        example="Usuario creado correctamente"
    )


class UpdateUserSuccessfulResponse(BaseModel):
    message: str = Field(
        description="Mensaje de exito en la operación",
        example="Usuario actualizado correctamente"
    )


class DeleteUserSuccessfulResponse(BaseModel):
    message: str = Field(
        description="Mensaje de exito en la operación",
        example="Usuario eliminado correctamente"
    )


@app.get(
    "/",
    tags=["Health Check"],
    description="Ruta raiz para comprovar que la api esta activa"
)
def root():
    """(health-check = comprovacion de estado)"""
    return {"success": True}


@app.post("/users", tags=["Users"], response_model=CreateUserSuccessfulResponse, status_code=201)
def create_user(user: User):
    # Comprovamos si el el id introducido esta ya en uso
    if user.id in database:
        # Si el usuario con el id introducido ya existe, devolvemos un error
        raise HTTPException(
            status_code=400, detail="El Usuario con el id introducido ya existe")
    # Comprovamos si el el email introducido esta ya en uso
    if user.email in database:
        # Si el usuario con el email introducido ya existe, devolvemos un error
        raise HTTPException(
            status_code=400, detail="El Usuario con el email introducido ya existe")
    # Simulamos la creacion del usuario en la base de datos
    database[user.id] = user
    # Devolvemos un mensaje para hacer saber que el usuario se ha creado correctamente
    return {"message": "Usuario creado correctamente"}


@app.get("/users", tags=["Users"])
def get_all_users(
    name: str = Query(description="Nombre del usuario", example="John"),
    email: str = Query(description="Email del usuario",
                       example="john@example.com"),
    age: int = Query(description="Edad del usuario", example=23)
) -> List[User]:
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


@app.get("/users/{user_id}", tags=["Users"])
def get_user(user_id: int = Path(description="El id del usuario que queremos recuperar", example=1)) -> User:
    # Recuperamos el usuario de nuestra base de datos en memoria
    user = database.get(user_id)
    # Si hemos encontrado el usuario, lo develolvemos como respuesta
    if user:
        return user
    # En caso de no encontrarlo, devolvemos un error con codio 404
    raise HTTPException(
        status_code=404, detail="Usuario no encontrado")


@app.put("/users/{user_id}", tags=["Users"])
def update_user(user: User, user_id: int = Path(..., description="El id del usuario que queremos actualizar", example=1)) -> UpdateUserSuccessfulResponse:
    # Comprovamos si el usuario con el id pasado existe.
    if user_id in database:
        # En caso de existir actualizamos el usuaro con los nuevos datos.
        database[user_id] = user
        # Devolvemos un mensaje para informar de que se ha actualizado correctamente.
        return {"message": "Usuario actualizado correctamente"}
    # En caso de no encontrarlo, devolvemos un error con codio 404
    raise HTTPException(
        status_code=404, detail="Usuario no encontrado")


@app.delete("/users/{user_id}", tags=["Users"])
def delete_user(user_id: int = Path(description="El id del usuario que queremos eliminar", example=1)) -> DeleteUserSuccessfulResponse:
    # Comprovamos si el usuario con el id pasado existe.
    if user_id in database:
        # Elimina el usuario de la base de datos simulada
        del database[user_id]
        # Devolvemos un mensaje para informar de que se ha borrado correctamente.
        return {"message": "Usuario eliminado correctamente"}
    # En caso de no encontrarlo, devolvemos un error con codio 404
    raise HTTPException(
        status_code=404, detail="Usuario no encontrado")
