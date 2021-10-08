import requests
from requests.exceptions import HTTPError, RequestException
from json.decoder import JSONDecodeError

class HttpCall:

    __url = ''
    __respEncoding = ''
    __respData = ''
    __errorMsg = ''

    def __init__(self, url):
        self.__url = url

    def __setError(self, errorMsg):
        self.__errorMsg = errorMsg
        return self

    def getError(self):
        return self.__errorMsg

    def errorFound(self):
        return len(self.__errorMsg) > 0

    def getEncoding(self):
        return self.__respEncoding

    def getResponseData(self):
        return self.__respData

    def call(self):
        try:
            req = requests.get(self.__url) 
            req.raise_for_status()
            self.__respEncoding = req.encoding
            self.__respData = req.json()

        # Exceptions
        except HTTPError as ex:
            self.__setError("Error en la petición HTTP: " + str(ex))
        except ConnectionError as con:
            self.__setError("Error de conexión: " + str(con))
        except RequestException as reqex:
            self.__setError("Error en la petición: " + str(reqex))
        except JSONDecodeError as eJson:
            self.__setError("Error al parsear los datos en formato JSON: " + str(eJson))
        finally:
            return self




