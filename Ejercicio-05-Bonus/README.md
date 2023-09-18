# Ejercicio 5 - BONUS: Despliegue de API en Deta Space

En este ejercicio bonus, aprenderemos cómo desplegar nuestra API desarrollada con FastAPI en Deta Space. Deta Space es una plataforma en la nube que facilita el despliegue de aplicaciones web y APIs.

## Pasos para el despliegue en Deta Space

Para completar este ejercicio, seguiremos los pasos proporcionados en el siguiente enlace: https://fastapi.tiangolo.com/deployment/deta/

Asegúrate de tener una cuenta en Deta Space antes de comenzar. Si no tienes una cuenta, puedes registrarte gratuitamente en https://deta.sh/.

## Paso 1: Preparación del proyecto

- Antes de desplegar nuestra API en Deta Space, debemos asegurarnos de que nuestro proyecto cumpla con los requisitos necesarios. Asegúrate de tener instalado Deta CLI y tener una estructura de proyecto adecuada.

1. Instala Deta CLI siguiendo las instrucciones en https://docs.deta.sh/docs/cli/install.

2. Asegúrate de que tu proyecto cumpla con la estructura adecuada. Si no estás seguro, puedes revisar los siguientes enlaces para obtener más información:
    -  [https://deta.space/docs/en/build/quick-starts/python](https://deta.space/docs/en/build/quick-starts/python)
    -  [https://deta.space/docs/en/build/new-apps](https://deta.space/docs/en/build/new-apps)

## Paso 2: Despliegue en Deta Space

- Ahora estamos listos para desplegar nuestra API en Deta Space. Sigue los pasos a continuación:

1. Abre una terminal y navega hasta el directorio raíz de tu proyecto.

2. Inicia sesión en Deta CLI ejecutando el siguiente comando y siguiendo las instrucciones proporcionadas:

    ```bash
    deta login
    ```

3. Crea un nuevo espacio en Deta Space con el siguiente comando:

    ```bash
    deta new
    ```

- Sigue las instrucciones en la terminal para configurar tu espacio.

4. Asegúrate de que el archivo principal de tu aplicación FastAPI se llama main.py.

5. Despliega tu API en Deta Space ejecutando el siguiente comando:

    ```bash
    deta deploy
    ```

Deta CLI generará una URL para tu API desplegada. Guárdala, ya que la necesitaremos para realizar peticiones a nuestra API en Deta Space.

¡Felicidades! Has desplegado con éxito tu API en Deta Space. Ahora puedes acceder a ella y realizar peticiones utilizando la URL generada por Deta CLI.

## Paso 3: Prueba de la API

- Una vez desplegada la API en Deta Space, es importante asegurarnos de que todo funcione correctamente. Prueba tu API siguiendo estos pasos:

1. Abre tu navegador web o utiliza herramientas como Postman o el Swagger de la aplicación accediendo a la ruta generada por Deta Space y añadiendo /docs al final.

2. Realiza una petición GET o POST a la URL de tu API en Deta Space.

    ```bash
    GET/POST <URL_de_tu_API>
    ```

- Recuerda que debes utilizar la URL generada por Deta CLI en el paso anterior.

3. Si todo funciona correctamente, deberías recibir una respuesta de tu API.

¡Enhorabuena! Has completado con éxito el despliegue de tu API desarrollada con FastAPI en Deta Space. Ahora puedes compartir tu API con otros y aprovechar todas las ventajas de Deta Space para alojar tus aplicaciones web y APIs de forma sencilla y rápida.

Si tienes alguna pregunta o necesitas más información, no dudes en consultar la documentación oficial de Deta Space y FastAPI. ¡Disfruta del despliegue de tu API!
