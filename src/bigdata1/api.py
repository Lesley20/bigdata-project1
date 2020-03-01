#https://data.cityofnewyork.us/resource/nc67-uf89.json

from sodapy import Socrata


client = Socrata('data.cityofnewyork.us', app_token)

client.get('nc67-uf89', limit=10)

client.get('nc67-uf89', limit=10, offset=10)

client.get('nc67-uf89',select='COUNT(*)')