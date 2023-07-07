# Ejercicio 1: Generar un CRUD con FastAPI

En este ejercicio, aprenderemos a crear un CRUD (Crear, Leer, Actualizar, Eliminar) utilizando FastAPI, un framework de desarrollo web rápido para construir APIs en Python.

## Objetivo

El objetivo de este ejercicio es familiarizarse con FastAPI y comprender cómo implementar operaciones CRUD básicas en una API.

## Pasos

### 1. Configuración del entorno:

- Asegúrate de tener Python 3.7 o superior instalado en tu sistema.
- Crea un nuevo entorno virtual utilizando herramientas como venv o conda.
- Activa el entorno virtual antes de continuar.
- Para crear el entorno con venv, ejecutar el siguiente comando en la terminal en la carpeta del proyecto:

  ```bash
  python3 -m venv venv
  ```

- Ejecutar el siguiente comando en la misma terminal para activar el entorno virtual y poder ejecutar comandos e instalar librerias:

  ```bash
  source venv/bin/activate
  ```

### 2. Instalación de dependencias:

- Abre una terminal y navega hasta el directorio de tu proyecto.

#### Opción 1: Instalar dependencias directamente con `pip`:

- Ejecuta el siguiente comando para instalar las dependencias necesarias:

  ```bash
  pip install fastapi uvicorn pydantic
  ```

#### Opción 2: Utilizar un archivo requirements.txt:

- Crea un archivo llamado requirements.txt en el directorio de tu proyecto.

- Dentro del archivo requirements.txt, agrega las siguientes líneas con las dependencias necesarias:

  ```
  fastapi~=0.95.2
  pydantic~=1.10.8
  uvicorn[standard]
  ```

- Guarda y cierra el archivo requirements.txt.

- Ejecuta el siguiente comando en la terminal para instalar las dependencias a partir del archivo requirements.txt:

  ```bash
  pip install -r requirements.txt
  ```

  ##### Nota: Ambas opciones instalarán las dependencias necesarias en tu entorno virtual. Puedes elegir la opción que prefieras según tus necesidades o preferencias.

### 3. Crear archivo principal:

- Crea un archivo llamado main.py y ábrelo en tu editor de texto preferido.

### 4. Importar módulos necesarios:

- En el archivo main.py, importa los siguientes módulos:

```python
from fastapi import FastAPI
from pydantic import BaseModel
```

### 5. Configurar la aplicación FastAPI:

- Crea una instancia de la aplicación FastAPI:

```python
app = FastAPI()
```

### 6. Simulamos una base de datos en memoria

```python
database = {}
```

### 7. Definir modelos de datos:

- Define modelos de datos utilizando la clase BaseModel de Pydantic.
  Por ejemplo, considera el siguiente modelo para una entidad "Usuario":

  ```python
  class User(BaseModel):
    id: int
    name: str
    email: str
    age: int
  ```

### 8. Implementar operaciones CRUD:

- Añade rutas y funciones de controlador para cada operación CRUD:

  - Crear usuario:

    ```python
    @app.post("/users")
    def create_user(user: User):
      # Simulamos la creacion del usuario en la base de datos
      database[user.id] = user
      # Devolvemos un mensaje para hacer saber que el usuario se ha creado correctamente
      return {"message": "Usuario creado correctamente"}
    ```

  - Obtener todos los usuarios:

    ```python
    @app.get("/users")
    def get_all_users():
      # Devolvemos la lista de todos los usuarios en la db fake de memoria
      return list(database.values())
    ```

  - Obtener un usuario por ID:

    ```python
    @app.get("/users/{user_id}")
    def get_user(user_id: int):
        # Recuperamos el usuario de nuestra base de datos en memoria usando path params
        user = database.get(user_id)
        # Si hemos encontrado el usuario, lo develolvemos como respuesta
        if user:
            return user
        # En caso de no encontrarlo, develovemos este mensaje
        return {"error": "Usuario no encontrado"}
    ```

  - Actualizar un usuario:

    ```python
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
    ```

  - Eliminar un usuario:

    ```python
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
    ```

### 9. Ejecutar la aplicación:

- En la terminal, ejecuta el siguiente comando para iniciar la aplicación:

```bash
uvicorn main:app --reload
```

- Esto iniciará el servidor de desarrollo y podrás acceder a tu API en http://localhost:8000.

### 11. Probar la API:

- Dado que Fast API nos construye directamente una interfaz de swagger podemos ir a la ruta http://localhost:8000/docs y probar la api. Otra opcion es utilizar herramientas como Postman o un navegador web para enviar solicitudes HTTP a las rutas de tu API y verificar su funcionamiento.
