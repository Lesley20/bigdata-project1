#https://data.cityofnewyork.us/resource/nc67-uf89.json

import os
from sodapy import Socrata


client = Socrata('data.cityofnewyork.us', os.environ['APP_KEY'])

client.get('nc67-uf89', limit=10)

client.get('nc67-uf89', limit=10, offset=10)

client.get('nc67-uf89',select='COUNT(*)')