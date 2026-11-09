Instrucciones para ejecutar la practica 3
Requisitos
-	Visual Studio Code.
-	Python.
-	MariaDB.
-	MongoDB Community Server.

1. Preparación de las bases de datos
Es necesario crear las bases de datos con sus respectivas tablas en los dos gestores.
MariaDB
1.	Abrir HeidiSQL
2.	Ejecuta el script MariaDB.sql
3.	Comprueba que se creó la base de datos practica3.
4.	Verifica que existan las tablas “branches” y “users”.
5.	Ejecuta el script MariaDB Datos Prueba.sql
6.	Comprueba que se insertaron los registros de prueba.

MongoDB
1.	Abrir MongoDB Compass o mongosh.
2.	Ejecuta el script mongodb.js
3.	Comprueba que se creó la base de datos Practica_3.
4.	Verifica que existan las colecciones brands, categories y products.
5.	Comprueba que se insertaron las marcas, categorías y productos.

2. Preparar el proyecto en Visual Studio Code y el entorno virtual
Abre Visual Studio Code y selecciona el archivo Practica3_Multibase y comprobar que se encuentren los archivos del proyecto.
Crear el entorno virtual
Abre la terminal de Visual Studio Code y ejecuta los siguientes comandos en powershell para crear un entorno virtual para instalar las bibliotecas necesarias del proyecto:
py -m venv venv

Después Ejecuta:
.\venv\Scripts\Activate.ps1

Nota: Realiza todo esto como administrador.

Instalar las bibliotecas
En el archivo requirements.txt deben encontrarse las siguientes dependencias:
pymysql
pymongo
python-dotenv

Despues ejecuta en la terminal:
python -m pip install -r requirements.txt

Estas bibliotecas permiten conectar Python con MariaDB y MongoDB, además de administrar las variables de configuración.

3. Configurar las conexiones
Configurar el archivo .env
Abre el archivo .env y coloca los datos de conexión correspondientes:

MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=*Aquí deberá ir tu contraseña*
MYSQL_DATABASE=practica3

MONGO_URI=mongodb://localhost:27017/
MONGO_DATABASE=Practica_3

Nota: Si el usuario no tiene contraseña, deja el valor vacío.

Verificar config.py
Comprobar que el archivo config.py lea las variables de entorno y defina la configuración de MariaDB y MongoDB.
Este archivo permite mantener separados los datos de conexión del resto del programa.

Verificar database.py
Comprueba que el archivo database.py contenga las funciones:
•	conectar_mariadb()
•	conectar_mongodb()

4. Ejecutar el sistema

Antes de ejecutar el programa, verifica que MariaDB y MongoDB estén funcionando.

Ejecutar Python
Desde la terminal de Visual Studio Code ejecuta:

pyt app.py

El programa mostrará un menú principal con las operaciones disponibles.

Menú principal del sistema
SISTEMA MULTIBASE
MARIADB: USUARIOS
1. Crear usuario
2. Consultar usuarios
3. Actualizar usuario
4. Eliminar usuario
MONGODB: PRODUCTOS
5. Crear producto
6. Consultar productos
7. Actualizar producto
8. Eliminar producto
INTEGRACIÓN
9. Consulta global
1. Salir

Administrar usuarios
Utiliza las opciones del 1 al 4 para:
•	Registrar nuevos usuarios.
•	Consultar los usuarios existentes.
•	Actualizar los datos seleccionados de un usuario.
•	Eliminar usuarios.
Los registros se almacenan en la tabla “users” de MariaDB.

Administrar productos
Utiliza las opciones del 5 al 8 para:
•	Registrar productos.
•	Consultar productos.
•	Actualizar el precio de un producto.
•	Eliminar productos.
Los registros se almacenan en la colección “products” de MongoDB.
Para registrar productos se deben utilizar identificadores válidos de marcas y categorías existentes.

Integración
Para relacionar las dos bases de datos se utiliza el campo favorite_product_id de MariaDB y el campo _id de MongoDB.
Es necesario que el identificador almacenado en MariaDB corresponda a un producto existente en MongoDB.

Consulta global
El programa consultará los usuarios en MariaDB y buscará sus productos favoritos y las marcas correspondientes en MongoDB.
El resultado permitirá visualizar en una sola consulta:
•	Nombre del usuario.
•	Correo electrónico.
•	Producto favorito.
•	Marca del producto.
•	Precio del producto.
De esta manera se comprueba la integración de ambas fuentes mediante Python.

Independencia de las bases de datos
Puedes probar apagando las conexiones mediante los servicios de Windows, al hacerlo, las opciones relacionadas a la respectiva base de datos quedan deshabilitadas, comprobado por un mensaje de error al seleccionar. Cuando un sistema es apagado, la otra base de datos sigue funcionando, adicional a esto, la consulta global de igual manera queda deshabilitada.

Cerrar el programa
Seleccionar la opción:
0.	Salir
El programa finalizará y se podrán cerrar Visual Studio Code y los gestores de bases de datos.

Consideraciones para reproducir la práctica
•	Los servicios de MariaDB y MongoDB deben estar instalados y configurados previamente.
•	Se deben ejecutar los scripts SQL y JavaScript antes de utilizar el programa.
•	Las credenciales del archivo .env deben corresponder a las configuraciones locales.
•	Los identificadores de productos favoritos deben coincidir con los identificadores reales de MongoDB.
•	Para las pruebas CRUD se recomienda utilizar registros de prueba.
•	Durante la prueba de independencia solamente se debe detener uno de los servicios a la vez.
Resultado esperado: al finalizar estos pasos se tendrá un sistema de consola desarrollado en Python que permite administrar usuarios en MariaDB, productos en MongoDB y consultar información relacionada entre ambas fuentes de datos.
# Cerveceria-Yorch
Cerveceria que exporta sus productos
