""" autor: Angel Garcia Zavala """

import requests
import json
import matplotlib.pyplot as plt

servidor = "192.168.56.101"
puerto = 1026
# encabezados de la llamada, manda y recibe json
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

# funcion que regresa los datos en estructura json para agregar datos al context brocker
def datos_agregar_json (id, tipo, lista_atributos):
    datos = {
        "contextElements": [
            {
                "type": tipo,
                "isPattern": "false",
                "id": id,
                "attributes": lista_atributos
            }
        ],
        "updateAction": "APPEND"
    }
    return datos


# funcion que consulta la version del context brocker
def version_fiware ():
    r = requests.get ("http://%s:%d/version" % (servidor, puerto))
    print r.text

# funcion para agregar datos al context brocker
def inserta_datos (datos_json):
    r = requests.post ('http://%s:%d/v1/updateContext' % (servidor, puerto), headers=headers, data=json.dumps (datos_json))
    print r.status_code, r.text, r.json ()

# funciones test 
def test_version ():
    version_fiware ()

# funcion para agregar datos al context brocker
def test_agrega_habitaciones ():
    atributos_h1 = [
        {
            "name": "temperatura",
            "type": "float",
            "value": "20"
        },
        {
            "name": "presion",
            "type": "integer",
            "value": "720"
        }
    ]

    atributos_h2 = [
        {
            "name": "temperatura",
            "type": "float",
            "value": "25"
        },
        {
            "name": "presion",
            "type": "integer",
            "value": "725"
        }
    ]

    habitacion1 = datos_agregar_json ("habitacion1", "habitacion", atributos_h1)
    habitacion2 = datos_agregar_json ("habitacion2", "habitacion", atributos_h2)
    # print json.dumps (habitacion1)
    inserta_datos (habitacion1)
    inserta_datos (habitacion2)


if __name__ == "__main__":
    # test_version ()
    test_agrega_habitaciones ()
