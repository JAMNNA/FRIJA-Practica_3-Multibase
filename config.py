import os
from dotenv import load_dotenv

load_dotenv()


# ==========================================
# CONFIGURACION MARIADB
# ==========================================

MYSQL_CONFIG = {

    "host": os.getenv("MYSQL_HOST", "localhost"),

    "port": int(os.getenv("MYSQL_PORT", 3306)),

    "user": os.getenv("MYSQL_USER", "root"),

    "password": os.getenv("MYSQL_PASSWORD", "Hocotate"),

    "database": os.getenv("MYSQL_DATABASE", "practica3")

}


# ==========================================
# CONFIGURACION MONGODB
# ==========================================

MONGO_URI = os.getenv(
    "MONGO_URI",
    "mongodb://localhost:27017/"
)

MONGO_DATABASE = os.getenv(
    "MONGO_DATABASE",
    "Practica_3"
)