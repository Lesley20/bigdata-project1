#https://data.cityofnewyork.us/resource/nc67-uf89.json

import os
from sodapy import Socrata

def get_data(page_size: int) -> dict:
	try: 
		client = Socrata('data.cityofnewyork.us', os.environ['APP_KEY'])

		client.get('nc67-uf89', limit={page_size}) #
		#client.get('nc67-uf89',select='COUNT(*)')

	except Exception as e:
		print(f'Something went wrong {e}')

		raise 

#def get_result:
	#try:
		#pass

	#except Exception as e:
		#pass