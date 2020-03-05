#https://data.cityofnewyork.us/resource/nc67-uf89.json

import os
from sodapy import Socrata

def get_data(page_size: int, num_pages: int):
	try: 
		client = Socrata('data.cityofnewyork.us', os.environ['APP_KEY'])

		for i in range (num_pages): 
			client.get('nc67-uf89', limit={page_size}, offset={})
			#client.get('nc67-uf89',select='COUNT(*)')

	except Exception as e:
		print(f'Something went wrong {e}')
		raise 