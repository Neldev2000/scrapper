import requests

url = 'https://api.dev.name.com/v4/domains:checkAvailability'
#API_KEY = '3mM44UcgtDEiVu_Y76godsEMvwFSb9FNNKw3g'
#API_SECRET = '581ayjUYERs7rG3sjfdsSQ'
api_username = 'nvivas-test'
api_token = '48ffd9a63658d5f62dd133a143aa2fb6ed934c89'
enlaces = ['test.com']
json = {"username" : api_username, 'password' : api_token, "Content-Type" : "application/json"}
data = {'domainNames' : f"{enlaces}"}
print(data, json)

response = requests.post(url, data = data, json = json)
print(response.json())
#response = requests.get(url,  headers=headers, params=  {'domain' : "un-test.online"})

#print(response.json())
"""
from godaddy import GoDaddyDomain
from pprint import pprint
url = ' '
GODADDY_API_KEY = '3mM44UcgtDEiVu_Y76godsEMvwFSb9FNNKw3g'
GODADDY_API_SECRET = '581ayjUYERs7rG3sjfdsSQ'


godaddy = GoDaddyDomain(GODADDY_API_KEY, GODADDY_API_SECRET)
godaddy.definir_extensiones(['net', 'com', 'tech', 'tel', 'co', 'cloud', 'email'])
data = godaddy.ver_disponibilidad_dominios(['un-clic', '1-clic'])
pprint(data)
"""