#https://data.cityofnewyork.us/resource/nc67-uf89.json

import os
from sodapy import Socrata

def get_data(page_size: float) -> dict:
	try: 
		client = Socrata('data.cityofnewyork.us', os.environ['APP_KEY'])

		client.get('nc67-uf89', limit=10)
		client.get('nc67-uf89', limit=10, offset=10)
		client.get('nc67-uf89',select='COUNT(*)')

	except Exception as e:
		print(f'Something went wrong {e}')

		raise 