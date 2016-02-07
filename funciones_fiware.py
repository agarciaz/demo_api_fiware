""" autor: Angel Garcia Zavala """

import requests
import json
import matplotlib.pyplot as plt

servidor = "192.168.56.101"
puerto = 1026

# funcion que consulta la version del context brocker
def version_fiware ():
    r = requests.get ("http://%s:%d/version" % (servidor, puerto))
    print r.text

# funciones test 
def test_version ():
    version_fiware ()

if __name__ == "__main__":
    test_version ()
