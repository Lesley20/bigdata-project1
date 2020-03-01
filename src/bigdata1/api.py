#https://data.cityofnewyork.us/resource/nc67-uf89.json

import os
from sodapy import Socrata

def get_data(page_size: int) -> dict:
	try: 
		page_size = Socrata('data.cityofnewyork.us', os.environ['APP_KEY'])

		page_size.get('nc67-uf89', limit=10)
		page_size.get('nc67-uf89',select='COUNT(*)')

	except Exception as e:
		print(f'Something went wrong {e}')

		raise 