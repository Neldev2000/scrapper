import requests



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
                data = self._ver_disponibilidad(dominio, ext)
                if not bool(data): continue
                ret.append(data)
            pass
        return ret
    
    def _ver_disponibilidad(self,dominio, extension):
        headers = {"Authorization" : f"sso-key {self.api_key}:{self.api_secret}", "accept" : "application/json"}
        params = {'domain' : f"{dominio}.{extension}"}
        response = requests.get(self.url, headers=headers, params=params)
        if response.status_code != 200:
            return dict()
            
        data = response.json()
        if data['available']:

            return {'dominio' : data['domain'], 'precio' : f"{data['price'] / (1000000*data['period'])} {data['currency']}/yr"}
        else: return dict()
    
        

    