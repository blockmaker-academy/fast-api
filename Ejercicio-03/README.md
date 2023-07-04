Ejercicio 3: Validación de datos en la API
En este ejercicio, practicaremos la validación de datos en la API utilizando las herramientas proporcionadas por FastAPI y Pydantic.

### Pasos

1. Añade validaciones a los modelos de datos existentes. Por ejemplo, especifica que el campo "name" debe tener una longitud mínima y máxima, o que el campo "email" debe tener un formato de correo electrónico válido.

   ```python
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

3. Utiliza las respuestas de error de FastAPI para manejar casos en los que los datos no cumplen con las validaciones. Puedes personalizar los mensajes de error y los códigos de estado de las respuestas según tus necesidades.

   ```python
   from fastapi import HTTPException

   @app.post("/users")
   def create_user(user: User):
     if user.id in database:
     raise HTTPException(status_code=400, detail="Usuario ya existe")
     database[user.id] = user
    return {"message": "Usuario creado correctamente"}
   ```
