# Librerías para la practica 1
from Application.Infrastructure.HTTP.HttpCall import HttpCall
import csv

# Constantes
URL = 'https://www.zaragoza.es/sede/servicio/equipamiento/basic/electrolineras.json'
DATASET_PARSED_FILE = 'dataset_result/practica_1_tcvd.csv' # Relativo al proyecto

# Init
httpRequest = HttpCall(URL)
if httpRequest.call().errorFound():
    raise Exception(httpRequest.getError())

# Comprobar datos y almacenarlos
respData = httpRequest.getResponseData()

# Inicializar fichero
ficheroCSV = csv.writer(open(DATASET_PARSED_FILE, "w+", encoding=httpRequest.getEncoding()))

# Cabecera para entender el dataset y escritura
ficheroCSV.writerow(["id", "title", "tipoEquipamiento", "titularidadPublica", "streetAddress", "postalCode", "portalId", "geometry", "latitud", "longitud", "creationDate", "lastUpdated"])

for resp in respData["result"]:
    ficheroCSV.writerow(
                [
                    resp["id"],
                    resp["title"],
                    resp["tipoEquipamiento"][0],
                    "Si" if resp["titularidadPublica"] == True else "No",
                    resp["streetAddress"],
                    resp["postalCode"],
                    resp["portalId"],
                    resp["geometry"],
                    resp["latitud"],
                    resp["longitud"],
                    resp["creationDate"],
                    resp["lastUpdated"]
                ]
            )