# Ejercicio 4: Mejorar documentación API con Swagger

En este ejercicio, mejoraremos la documentación de nuestra API para lograr una API bien documentada, utilizando herramientas como Swagger. Aprenderemos a proporcionar descripciones claras y detalladas de los endpoints, parámetros y respuestas, garantizando una documentación completa y precisa.

### Pasos

1. Añade un título, descripción y version de la api en el Swagger

   ```python
    app = FastAPI(
            title="Users CRUD API",
            description="API de prueba para crear, leer, actualizar y borrar usuarios",
            version="1.0.0"
        )
   ```

2. Documenta el modelo de datos añadiendo descripción y ejemplos

   ```python
    # Actualiza el import de pydantic añadiendo "Field"
    from pydantic import BaseModel, constr, EmailStr, Field
    # Añade descipción y ejemplo en cada propiedad del modelo
    class User(BaseModel):
        id: int = Field(description="Id del usuario", example=1)
        name: constr(min_length=1, max_length=50) = Field(
            description="Nombre del usuario", example="John Doe")
        email: EmailStr = Field(
            description="Email del usuario", example="john@example.com")
        age: int = Field(description="Edad del usuario", example=25)
   ```

3. Documenta el enpoint de comprovación de estado de la api

   ```python
   # Añade la propiedad tags para que aparezca agrupado en la colección y la descripción
    @app.get("/", tags=["Health Check"], description="Ruta raiz para comprovar que la api esta activa"
            )
    def root():
        """(health-check = comprovacion de estado)"""
        return {"success": True}
   ```

4. Utiliza las respuestas de error de FastAPI para manejar casos en los que los datos no cumplen con las validaciones. Puedes personalizar los mensajes de error y los códigos de estado de las respuestas según tus necesidades.

   ```python
   from fastapi import FastAPI, HTTPException

   @app.post("/users")
   def create_user(user: User):
     if user.id in database:
     raise HTTPException(status_code=400, detail="Usuario ya existe")
     database[user.id] = user
    return {"message": "Usuario creado correctamente"}
   ```

5. Añade documentación a la ruta de crear usuario

   ```python
   # Creamos una clase para tener el tipo de respuesta y poder poner el ejemplo
    class CreateUserSuccessfulResponse(BaseModel):
        message: str = Field(
            description="Mensaje de exito",
            example="Usuario creado correctamente"
        )
    # Añadimos de el modelo de respuesta y indicamos tambien el codigo de estado.
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
   ```

6. Añade documentación a la ruta de obtener todos los usuarios

   ```python
   # Añadimos el import de List de typing
   from typing import List
   # Añadimos el import de Query de fastapi
   from fastapi import FastAPI, HTTPException, Query

    def get_all_users(
        # Añadimos una descripción y ejemplo de la query name
        name: str = Query(description="Nombre del usuario", example="John", default=None),
        # Añadimos una descripción y ejemplo de la query email
        email: str = Query(description="Email del usuario", example="john@example.com", default=None),
        # Añadimos una descripción y ejemplo de la query age
        age: int = Query(description="Edad del usuario", example=23, default=None)
        # Añadimos un typo de retorno indicando que esta función retorna una Lista de modelos User
    ) -> List[User]:
        ...EL RESTO DEL CODIGO DE LA FUNCIÓN (NO CAMBIAMOS NADA)
   ```

7. Añade documentación a la ruta de obtener usuario

   ```python
   # Añadimos el import de Path de fastapi
   from fastapi import FastAPI, HTTPException, Query, Path


    @app.get("/users/{user_id}", tags=["Users"])
    # Añadimos descripcion y ejemplo al parametro de ruta
    def get_user(user_id: int = Path(description="El id del usuario que queremos recuperar", example=1)) -> User:
        ...EL RESTO DEL CODIGO DE LA FUNCIÓN (NO CAMBIAMOS NADA)
   ```

8. Añade documentación a la ruta de actualizar usuario

   ````python
    # Creamos una clase para tener el tipo de respuesta y poder poner el ejemplo
   class UpdateUserSuccessfulResponse(BaseModel):
    message: str = Field(
        description="Mensaje de exito en la operación",
        example="Usuario actualizado correctamente"
    )

    @app.put("/users/{user_id}", tags=["Users"])
    # Añadimos descripcion y ejemplo al parametro de ruta y el tipo de respuesta
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
           ```
   ````

9. Añade documentación a la ruta de borrar usuario

   ```python
    # Creamos una clase para tener el tipo de respuesta y poder poner el ejemplo
    class DeleteUserSuccessfulResponse(BaseModel):
        message: str = Field(
            description="Mensaje de exito en la operación",
            example="Usuario eliminado correctamente"
        )


    @app.delete("/users/{user_id}", tags=["Users"])
    # Añadimos descripcion y ejemplo al parametro de ruta y añadimos el tipo de respuesta
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
   ```

Si ahora actualizas la pagina de http://localhost:8000/docs encontraras la api actualizada con toda la documentación añadida.
