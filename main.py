import sys 

import src.api 

if __name__ == "__main__":
	args = sys.argv[1:]
	num_args = len(args)


	page_size = args[0].split('=')[1] #just obtain the number 1000
	num_pages = args[1].split('=')[1]
	output = args[2]

	 


"""
through process:

1. get argument from main.py
	page_size
	page_num
2. call function from api.py 
3. api.py will send the request 
4. then display output in json

"""