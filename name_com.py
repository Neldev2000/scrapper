import requests

class NameDomains():
    def __init__(self, api_token, api_username):
        self.api_token = api_token
        self.api_username = api_username
        self.extensiones = []
        self.url = 'https://api.dev.name.com/v4/domains:checkAvailability'
    def definir_extensiones(self, extensiones):
        self.extensiones = extensiones
    def ver_disponibilidad_dominios(self, lista_dominios):
        ret = []

        for dominio in lista_dominios:
            for ext in self.extensiones:
                data = self._ver_disponibilidad(dominio, ext)
                if not bool(data): continue
                ret.append(data)
            pass
        return ret
    
    def _ver_disponibilidad(self,enlaces):
        json = {"-u" : f"{self.api_username}:{self.api_token}", "Content-Type" : "application/json"}
        data = {'domainNames' : f"{enlaces}"}
        response = requests.post(self.url, data=data, json=json)
        if response.status_code != 200:
            return dict()
            
        data = response.json()
        if data['available']:

            return {'dominio' : data['domain'], 'precio' : f"{data['price'] / (1000000*data['period'])} {data['currency']}/yr"}
        else: return dict()