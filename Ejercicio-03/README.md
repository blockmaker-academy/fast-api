Ejercicio 3: Validación de datos en la API
En este ejercicio, practicaremos la validación de datos en la API utilizando las herramientas proporcionadas por FastAPI y Pydantic.

### Pasos

1. Añade validaciones a los modelos de datos existentes. Por ejemplo, especifica que el campo "name" debe tener una longitud mínima y máxima, o que el campo "email" debe tener un formato de correo electrónico válido.

   ```python
   # Añadimos las importaciones de constr y EmailStr para la validación
   from pydantic import BaseModel, constr, EmailStr

   class User(BaseModel):
   id: int
   name: constr(min_length=1, max_length=50)
   email: EmailStr
   age: int
   ```

2. Implementa validaciones en las rutas de la API. Asegúrate de que los datos proporcionados en una solicitud de creación de usuario son válidos antes de insertarlos en la base de datos.

   ```python
   @app.post("/users")
   def create_user(user: User):
      # Comprovamos si el el id introducido esta ya en uso
      if user.id in database:
         # Si el usuario con el id introducido ya existe, devolvemos un error
        return {"error": "El Usuario con el id introducido ya existe"}
      # Comprovamos si el el email introducido esta ya en uso
      if user.email in database:
         # Si el usuario con el email introducido ya existe, devolvemos un error
        return {"error": "El Usuario con el email introducido ya existe"}
      # Simulamos la creacion del usuario en la base de datos
      database[user.id] = user
      # Devolvemos un mensaje para hacer saber que el usuario se ha creado correctamente
      return {"message": "Usuario creado correctamente"}
   ```

3. Utiliza las respuestas de error de FastAPI para manejar casos en los que los datos no cumplen con las validaciones. Puedes personalizar los mensajes de error y los códigos de estado de las respuestas según tus necesidades.

   ```python
   # Añadimos el import de HTTPException
   from fastapi import HTTPException
   # Modificamos la ruta create user añadiendo las respuestas de error usando HTTPException
   @app.post("/users")
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

   # Modificamos la ruta get user añadiendo las respuestas de error usando HTTPException
   @app.get("/users/{user_id}")
   def get_user(user_id: int = None):
      # Recuperamos el usuario de nuestra base de datos en memoria
      user = database.get(user_id)
      # Si hemos encontrado el usuario, lo develolvemos como respuesta
      if user:
         return user
      # En caso de no encontrarlo, devolvemos un error con codio 404
      raise HTTPException(
         status_code=404, detail="Usuario no encontrado")

   # Modificamos la ruta update user añadiendo las respuestas de error usando HTTPException
   @app.put("/users/{user_id}")
   def update_user(user_id: int, user: User):
      # Comprovamos si el usuario con el id pasado existe.
      if user_id in database:
         # En caso de existir actualizamos el usuaro con los nuevos datos.
         database[user_id] = user
         # Devolvemos un mensaje para informar de que se ha actualizado correctamente.
         return {"message": "Usuario actualizado correctamente"}
      # En caso de no encontrarlo, devolvemos un error con codio 404
      raise HTTPException(
         status_code=404, detail="Usuario no encontrado")

   # Modificamos la ruta delete user añadiendo las respuestas de error usando HTTPException
   @app.delete("/users/{user_id}")
   def delete_user(user_id: int):
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
