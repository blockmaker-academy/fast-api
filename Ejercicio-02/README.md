# Ejercicio 2: Modificar las APIs para recuperar usuarios por query params

1. Modificar la función get_all_users para permitir la recuperación de usuarios utilizando parámetros de consulta (query params) para filtrar por nombre y/o correo electrónico y/o edad.

   ```python
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
   ```

- Ahora, puedes hacer una solicitud GET a /users?name=John para obtener todos los usuarios con el nombre "John" o /users?email=test@example.com para obtener todos los usuarios con el correo electrónico "test@example.com" o /users?age=29 para obtener todos los usuarios con 29 de edad. También puedes combinar ambos parámetros de consulta para obtener resultados más específicos.

- Prueba de realizar las llamadas tanto en el Swagger de la aplicación como en Postman (Ruta de ejemplo para postman: http://localhost:8000/users?name=juan&age=30)
