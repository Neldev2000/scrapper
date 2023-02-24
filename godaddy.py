import requests

def ver_disponibilidad(url, auth, dominio, extension):
    headers = {"Authorization" : f"sso-key {auth[0]}:{auth[1]}", "accept" : "application/json"}
    params = {'domain' : f"{dominio}.{extension}"}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        return dict()
        
    data = response.json()
    if data['available']:

        return {'dominio' : data['domain'], 'precio' : f"{data['price'] / (1000000*data['period'])} {data['currency']}/yr"}
    else: return dict()

class GoDaddyDomain():
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.extensiones = []
        self.url = 'https://api.ote-godaddy.com/v1/domains/available'
    def definir_extensiones(self, extensiones):
        self.extensiones = extensiones
    def ver_disponibilidad_dominios(self, lista_dominios):
        ret = []

        for dominio in lista_dominios:
            for ext in self.extensiones:
                data = ver_disponibilidad(self.url,(self.api_key, self.api_secret) ,dominio, ext)
                if not bool(data): continue
                ret.append(data)
            pass
        return ret
    
        

    