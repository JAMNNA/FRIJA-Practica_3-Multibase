import pymysql
from pymongo import MongoClient
from config import MYSQL_CONFIG, MONGO_URI, MONGO_DATABASE


# ==========================================
# CONEXION MARIA DB
# ==========================================

def conectar_mariadb():

    try:

        config = MYSQL_CONFIG.copy()
        config.pop("cursorclass", None)

        conexion = pymysql.connect(
            **config,
            connect_timeout=5,
            autocommit=False
        )

        return conexion

    except Exception as error:

        print("Error conectando a MariaDB:", error)

        return None


# ==========================================
# CONEXION MONGODB
# ==========================================

def conectar_mongodb():

    try:

        cliente = MongoClient(
            MONGO_URI,
            serverSelectionTimeoutMS=3000
        )

        cliente.admin.command("ping")

        db = cliente[MONGO_DATABASE]

        return cliente, db

    except Exception as error:

        print("Error conectando a MongoDB:", error)

        return None, None