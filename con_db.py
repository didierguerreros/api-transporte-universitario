import psycopg2


def obtener_conexion():
    conexion = psycopg2.connect(
        host="localhost",
        database="fastapi_test",
        user="postgres",
        password="123456",
        port="5432"
    )

    return conexion

conexion = obtener_conexion()

print("Conexión exitosa a PostgreSQL")

conexion.close()