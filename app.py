from database import conectar_mariadb, conectar_mongodb

from bson import ObjectId, Decimal128
from decimal import Decimal

import pymysql

def crear_usuario():

    conexion = conectar_mariadb()

    if conexion is None:
        return

    try:

        print("\n--- REGISTRO DE USUARIO ---")

        nombre = input("Nombre: ")
        paterno = input("Apellido paterno: ")
        materno = input("Apellido materno: ")
        email = input("Correo: ")
        telefono = input("Telefono: ")
        rol = input("Rol (ADMIN, MANAGER, SALES, INVENTORY, CUSTOMER): ").upper()
        favorito = input("Cerveza Favorita ID: ").strip()

        branch = input("ID de sucursal (Enter para NULL): ")

        branch_id = int(branch) if branch else None

        with conexion.cursor() as cursor:

            sql = """
            INSERT INTO users
            (
                first_name,
                paternal_last_name,
                maternal_last_name,
                email,
                phone,
                role,
                branch_id,
                favorite_product_id
            )
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
            """

            cursor.execute(
                sql,
                (
                    nombre,
                    paterno,
                    materno,
                    email,
                    telefono,
                    rol,
                    branch_id,
                    favorito if favorito else None
                )
            )

        conexion.commit()

        print("\nUsuario creado correctamente.")

    except Exception as error:

        conexion.rollback()
        print("Error:", error)

    finally:

        conexion.close()



def consultar_usuarios():

    conexion = conectar_mariadb()

    if conexion is None:
        return

    try:

        with conexion.cursor(pymysql.cursors.DictCursor) as cursor:

            cursor.execute("""
                SELECT
                    user_id,
                    first_name,
                    paternal_last_name,
                    email,
                    role,
                    branch_id,
                    favorite_product_id
                FROM users
            """)

            usuarios = cursor.fetchall()

            for usuario in usuarios:

                print(usuario)

    except Exception as error:

        print("Error:", error)

    finally:

        conexion.close()




def actualizar_usuario():

    conexion = conectar_mariadb()

    if conexion is None:
        return

    try:

        print("\n--- ACTUALIZAR USUARIO ---")

        user_id = int(input("ID del usuario: "))

        # Verificar que el usuario exista
        with conexion.cursor() as cursor:

            cursor.execute("""
                SELECT * FROM users
                WHERE user_id = %s
            """, (user_id,))

            usuario = cursor.fetchone()

            if usuario is None:
                print("No se encontro el usuario.")
                return

        # Menu de campos disponibles
        print("\n¿Qué dato deseas actualizar?")

        print("1. Nombre")
        print("2. Apellido paterno")
        print("3. Apellido materno")
        print("4. Correo")
        print("5. Telefono")
        print("6. Rol")
        print("7. Cerveza favorita")
        print("8. Sucursal")

        opcion = input("\nSelecciona una opcion: ")

        # Relacion entre opciones y columnas
        campos = {
            "1": ("first_name", "Nuevo nombre: "),
            "2": ("paternal_last_name", "Nuevo apellido paterno: "),
            "3": ("maternal_last_name", "Nuevo apellido materno: "),
            "4": ("email", "Nuevo correo: "),
            "5": ("phone", "Nuevo telefono: "),
            "6": ("role", "Nuevo rol: "),
            "7": ("favorite_product_id", "Nuevo ID de cerveza favorita: "),
            "8": ("branch_id", "Nuevo ID de sucursal: ")
        }

        if opcion not in campos:
            print("Opcion no valida.")
            return

        columna, mensaje = campos[opcion]

        nuevo_dato = input(mensaje)

        # Convertir los valores correspondientes
        if opcion == "6":
            nuevo_dato = nuevo_dato.upper()

            roles_validos = [
                "ADMIN", "MANAGER", "SALES",
                "INVENTORY", "CUSTOMER"
            ]

            if nuevo_dato not in roles_validos:
                print("Rol no valido.")
                return

        if opcion == "8":
            nuevo_dato = int(nuevo_dato) if nuevo_dato else None

        if opcion in ("3", "5", "7") and nuevo_dato == "":
            nuevo_dato = None

        # Actualizar solamente el campo seleccionado
        with conexion.cursor() as cursor:

            sql = f"""
                UPDATE users
                SET {columna} = %s
                WHERE user_id = %s
            """

            cursor.execute(sql, (nuevo_dato, user_id))

        conexion.commit()

        print("\nDato actualizado correctamente.")

    except Exception as error:

        conexion.rollback()
        print("Error al actualizar:", error)

    finally:

        conexion.close()




def eliminar_usuario():

    conexion = conectar_mariadb()

    if conexion is None:
        return

    try:

        user_id = int(input("ID del usuario a eliminar: "))

        with conexion.cursor() as cursor:

            cursor.execute("""
                DELETE FROM users
                WHERE user_id = %s
            """, (user_id,))

        conexion.commit()

        if cursor.rowcount:
            print("Usuario eliminado.")
        else:
            print("Usuario no encontrado.")

    except Exception as error:

        conexion.rollback()
        print("Error:", error)

    finally:

        conexion.close()

#MONGODB
def crear_producto():

    cliente, db = conectar_mongodb()

    if db is None:
        return

    try:

        nombre = input("Nombre del producto: ")

        brand_id = ObjectId(input("ID de la marca: "))
        category_id = ObjectId(input("ID de la categoria: "))

        presentation = input("Presentacion: ")
        content_ml = int(input("Contenido en ml: "))

        alcohol = Decimal(input("Contenido de alcohol: "))
        precio = Decimal(input("Precio de venta: "))

        producto = {

            "name": nombre,

            "brand_id": brand_id,

            "category_id": category_id,

            "presentation": presentation,

            "content_ml": content_ml,

            "alcohol_content": Decimal128(alcohol),

            "sale_price": Decimal128(precio),

            "status": "ACTIVE"
        }

        resultado = db.products.insert_one(producto)

        print("Producto creado correctamente.")
        print("ID generado:", resultado.inserted_id)

    except Exception as error:

        print("Error:", error)

    finally:

        cliente.close()

def consultar_productos():

    cliente, db = conectar_mongodb()

    if db is None:
        return

    try:

        productos = db.products.find()

        for producto in productos:

            print({
                "ID": str(producto["_id"]),
                "Nombre": producto["name"],
                "Precio": str(producto["sale_price"]),
                "Estado": producto["status"]
            })

    except Exception as error:

        print("Error:", error)

    finally:

        cliente.close()


def actualizar_producto():

    cliente, db = conectar_mongodb()

    if db is None:
        return

    try:

        producto_id = ObjectId(input("ID del producto: "))

        nuevo_precio = Decimal(input("Nuevo precio: "))

        resultado = db.products.update_one(

            {"_id": producto_id},

            {
                "$set": {
                    "sale_price": Decimal128(nuevo_precio)
                }
            }

        )

        if resultado.matched_count:
            print("Producto actualizado.")
        else:
            print("Producto no encontrado.")

    except Exception as error:

        print("Error:", error)

    finally:

        cliente.close()


def eliminar_producto():

    cliente, db = conectar_mongodb()

    if db is None:
        return

    try:

        producto_id = ObjectId(input("ID del producto a eliminar: "))

        resultado = db.products.delete_one({
            "_id": producto_id
        })

        if resultado.deleted_count:
            print("Producto eliminado.")
        else:
            print("Producto no encontrado.")

    except Exception as error:

        print("Error:", error)

    finally:

        cliente.close()



def consulta_global():

    print("\nCONSULTA GLOBAL MULTIBASE")

    # Primera fuente: MariaDB
    conexion = conectar_mariadb()

    if conexion is None:
        print("No se pudo consultar MariaDB.")
        return

    usuarios = []

    try:

        with conexion.cursor(pymysql.cursors.DictCursor) as cursor:

            cursor.execute("""
                SELECT
                    user_id,
                    first_name,
                    paternal_last_name,
                    email,
                    favorite_product_id
                FROM users
                WHERE favorite_product_id IS NOT NULL
            """)

            usuarios = cursor.fetchall()

    except Exception as error:

        print("Error en MariaDB:", error)
        return

    finally:

        conexion.close()

    # Segunda fuente: MongoDB
    cliente, db = conectar_mongodb()

    if db is None:

        print("MongoDB no esta disponible.")
        print("No se puede completar la consulta global.")
        return

    try:

        for usuario in usuarios:

            favorito = usuario["favorite_product_id"]

            try:

                producto_id = ObjectId(favorito)

            except Exception:

                print("ID de producto invalido:", favorito)
                continue

            producto = db.products.find_one({
                "_id": producto_id
            })

            if producto is None:

                print("Producto no encontrado para:",
                      usuario["first_name"])

                continue

            marca = db.brands.find_one({
                "_id": producto["brand_id"]
            })

            nombre_marca = (
                marca["name"] if marca else "Marca desconocida"
            )

            print("\n--------------------------------")

            print("USUARIO")
            print("ID:", usuario["user_id"])
            print("Nombre:", usuario["first_name"])
            print("Correo:", usuario["email"])

            print("\nPRODUCTO FAVORITO")
            print("Producto:", producto["name"])
            print("Marca:", nombre_marca)
            print("Precio:", producto["sale_price"])

            print("--------------------------------")

    except Exception as error:

        print("Error consultando MongoDB:", error)

    finally:

        cliente.close()

#Menú de opciones

def menu():

    while True:

        print("\n================================")
        print(" SISTEMA MULTIBASE DE DATOS")
        print("================================")

        print("\n--- CRUD DE USUARIOS (MariaDB) ---")

        print("1. Crear usuario")
        print("2. Consultar usuarios")
        print("3. Actualizar usuario")
        print("4. Eliminar usuario")

        print("\n--- CRUD DE PRODUCTOS (MongoDB) ---")

        print("5. Crear producto")
        print("6. Consultar productos")
        print("7. Actualizar producto")
        print("8. Eliminar producto")

        print("\n--- INTEGRACION MULTIBASE ---")

        print("9. Ejecutar consulta global")

        print("\n0. Salir")

        opcion = input("\nSelecciona una opcion: ")

        if opcion == "1":
            crear_usuario()

        elif opcion == "2":
            consultar_usuarios()

        elif opcion == "3":
            actualizar_usuario()

        elif opcion == "4":
            eliminar_usuario()

        elif opcion == "5":
            crear_producto()

        elif opcion == "6":
            consultar_productos()

        elif opcion == "7":
            actualizar_producto()

        elif opcion == "8":
            eliminar_producto()

        elif opcion == "9":
            consulta_global()

        elif opcion == "0":
            print("Cerrando sistema...")
            break

        else:
            print("Opcion no valida.")


if __name__ == "__main__":

    menu()