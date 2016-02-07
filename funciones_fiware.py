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

# funcion que regresa los datos en estructura json para modificar datos al context brocker
def datos_modificar_json (id, tipo, lista_atributos):
    datos = {
        "contextElements": [
            {
                "type": tipo,
                "isPattern": "false",
                "id": id,
                "attributes": lista_atributos
            }
        ],
        "updateAction": "UPDATE"
    }
    
    return datos

# funcion que regresa los datos en estructura json para consultar datos al context brocker
def datos_consulta_json (id, tipo, es_expreg=False):
    val_expreg = "false"
    if es_expreg:
        val_expreg = "true"
    datos = {
        "entities": [
            {
                "type": tipo,
                "isPattern": val_expreg,
                "id": id
            }
        ]
    }
    return datos

# funcion que regresa los datos en estructura json para consultar datos al context brocker
# utilizando atributos
def datos_consulta_json_atributo (id, tipo, atributos, es_expreg=False):
    datos = datos_consulta_json (id, tipo, es_expreg)
    datos["attributes"] = atributos
    return datos

# funcion que consulta la version del context brocker
def version_fiware ():
    r = requests.get ("http://%s:%d/version" % (servidor, puerto))
    print r.text

# funcion para agregar datos al context brocker
def inserta_datos (datos_json):
    r = requests.post ('http://%s:%d/v1/updateContext' % (servidor, puerto), headers=headers, data=json.dumps (datos_json))
    # print r.status_code, r.text, r.json ()

# funcion para consultar datos al context brocker
def consulta_datos (datos_json):
    r = requests.post ('http://%s:%d/v1/queryContext' % (servidor, puerto), headers=headers, data=json.dumps (datos_json))
    # print r.status_code, json.dumps (r.json())
    return r.json ()

# funcion para borrar datos al context brocker
def borra_datos (id):
    r = requests.delete ('http://%s:%d/v1/contextEntities/%s' % (servidor, puerto, id), headers=headers)
    print r.status_code, r.text

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

def test_consulta_habitaciones ():
    datos = datos_consulta_json ("habitacion*", "habitacion", True)
    # print datos
    r = consulta_datos (datos)
    print r

def test_modifica_datos ():
    atributos_h1 = [
        {
            "name": "temperatura",
            "type": "float",
            "value": "0"
        }
    ]
    habitacion1 = datos_modificar_json ("habitacion1", "habitacion", atributos_h1)
    inserta_datos (habitacion1)

def test_borra_datos ():
    id = "habitacion1"
    borra_datos (id)


def test_grafica ():
    atributos_es1 = [
        {
            "name": "temperatura",
            "type": "float",
            "value": "20"
        },
        {
            "name": "presion",
            "type": "integer",
            "value": "720"
        },
        {
            "name": "ubicacion",
            "type": "string",
            "value": "noroeste"
        }
    ]
    atributos_es2 = [
        {
            "name": "temperatura",
            "type": "float",
            "value": "25"
        },
        {
            "name": "presion",
            "type": "integer",
            "value": "720"
        },
        {
            "name": "ubicacion",
            "type": "string",
            "value": "noreste"
        }
    ]
    atributos_es3 = [
        {
            "name": "temperatura",
            "type": "float",
            "value": "30"
        },
        {
            "name": "presion",
            "type": "integer",
            "value": "720"
        },
        {
            "name": "ubicacion",
            "type": "string",
            "value": "centro"
        }
    ]
    atributos_es4 = [
        {
            "name": "temperatura",
            "type": "float",
            "value": "35"
        },
        {
            "name": "presion",
            "type": "integer",
            "value": "720"
        },
        {
            "name": "ubicacion",
            "type": "string",
            "value": "suroeste"
        }
    ]
    atributos_es5 = [
        {
            "name": "temperatura",
            "type": "float",
            "value": "40"
        },
        {
            "name": "presion",
            "type": "integer",
            "value": "720"
        },
        {
            "name": "ubicacion",
            "type": "string",
            "value": "sureste"
        }
    ]
    estacion1 = datos_agregar_json ("estacion1", "estacion", atributos_es1)
    estacion2 = datos_agregar_json ("estacion2", "estacion", atributos_es2)
    estacion3 = datos_agregar_json ("estacion3", "estacion", atributos_es3)
    estacion4 = datos_agregar_json ("estacion4", "estacion", atributos_es4)
    estacion5 = datos_agregar_json ("estacion5", "estacion", atributos_es5)
    # print json.dumps (estacion1)
    inserta_datos (estacion1)
    inserta_datos (estacion2)
    inserta_datos (estacion3)
    inserta_datos (estacion4)
    inserta_datos (estacion5)

    atributos = ["temperatura"]
    datos = datos_consulta_json_atributo ("estacion*", "estacion", atributos, True)
    r = consulta_datos (datos)
    # print r["contextResponses"]
    temperaturas = []
    for i in r["contextResponses"]:
    	# print i["contextElement"]["id"], int (i["contextElement"]["attributes"][0]["value"])
        temperaturas.append (int (i["contextElement"]["attributes"][0]["value"]))
        
    # print temperaturas
    plt.figure ()
    plt.title ("temperaturas")
    plt.bar (range(len(temperaturas)), temperaturas)
    plt.show ()


if __name__ == "__main__":
    # test_version ()
    # test_agrega_habitaciones ()
    # test_modifica_datos ()
    # test_borra_datos ()
    # test_consulta_habitaciones ()
    test_grafica ()
