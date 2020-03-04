import sys 
import argparse

from src.bigdata1.api import get_data

if __name__ == "__main__":
	parse = argparse.ArgumentParser(description="Process parameters")
	parse.add_argument("--page_size", type = int)
	parse.add_argument("--num_pages", type = int)

	args = parser.parse_args()
	get_data(arg.page_size)



"""
argparse will figure out how to parse those out of sys.argv. 

"""