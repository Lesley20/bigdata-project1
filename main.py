#import sys 
import argparse

from src.bigdata1.api import get_data

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("--page_size", type = int)
	parser.add_argument("--num_pages", type = int)

	args = parser.parse_args()
	get_records(args.page_size, args.num_pages)



"""
argparse will figure out how to parse those out of sys.argv. 

"""