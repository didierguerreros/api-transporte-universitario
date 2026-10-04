from fastapi import FastAPI
from con_db import obtener_conexion

api = FastAPI()

#Recurso_data rutas, paradas y horarios
'''rutas = [
    {
        "id": 1,
        "nombre": "Ruta Norte",
        "horario": "06:00",
        "paradas": [
            "Portal Norte",
            "Universidad",
            "Campus Deportivo"
        ]
    },
    {
        "id": 2,
        "nombre": "Ruta Sur",
        "horario": "06:30",
        "paradas": [
            "Terminal",
            "Centro",
            "Universidad"
        ]
    },
    {
        "id": 3,
        "nombre": "Ruta Oriente",
        "horario": "07:00",
        "paradas": [
            "Barrio Oriente",
            "Hospital",
            "Universidad"
        ]
    }
]'''

#Endpoint general
@api.get("/")
def inicio():
    return {
        "mensaje": "API de Transporte Universitario funcionando"
    }

#Endpoint rutas
@api.get("/rutas")
def consultar_rutas():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id_ruta, nombre, descripcion, estado
        FROM rutas
    """)

    resultados = cursor.fetchall()

    cursor.close()
    conexion.close()

    return resultados

#Endpoint rutas por ID
@api.get("/rutas/{id}")
def consultar_ruta(id: int):

    for ruta in rutas:
        if ruta["id"] == id:
            return ruta

    return {
        "mensaje": "Ruta no encontrada"
    }

#Endpoint rutas por ID y paradas
@api.get("/rutas/{id}/paradas")
def consultar_paradas(id: int):

    for ruta in rutas:
        if ruta["id"] == id:
            return {
                "ruta": ruta["nombre"],
                "paradas": ruta["paradas"]
            }
    return {
        "mensaje": "Ruta no encontrada"
    }

#Endpoint rutas por ID y horarios
@api.get("/rutas/{id}/horario")
def consultar_horario(id: int):

    for ruta in rutas:
        if ruta["id"] == id:
            return {
                "ruta": ruta["nombre"],
                "horario": ruta["horario"]
            }

    return {
        "mensaje": "Ruta no encontrada"
    }

