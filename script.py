"""import requests

url = 'https://api.ote-godaddy.com/v1/domains/available'
API_KEY = '3mM44UcgtDEiVu_Y76godsEMvwFSb9FNNKw3g'
API_SECRET = '581ayjUYERs7rG3sjfdsSQ'
auth = (API_KEY, API_SECRET)
headers = {"Authorization" : "sso-key {}:{}".format(API_KEY, API_SECRET), "accept" : "application/json"}
#newSession = requests.session()

response = requests.get(url,  headers=headers, params=  {'domain' : "un-test.online"})

print(response.json())"""

from godaddy import GoDaddyDomain
from pprint import pprint
url = ' '
GODADDY_API_KEY = '3mM44UcgtDEiVu_Y76godsEMvwFSb9FNNKw3g'
GODADDY_API_SECRET = '581ayjUYERs7rG3sjfdsSQ'


godaddy = GoDaddyDomain(GODADDY_API_KEY, GODADDY_API_SECRET)
godaddy.definir_extensiones(['net', 'com', 'tech', 'tel', 'co', 'cloud', 'email'])
data = godaddy.ver_disponibilidad_dominios(['un-clic', '1-clic'])
pprint(data)
