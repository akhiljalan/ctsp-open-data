import networkx as nx
import sys
sys.path.insert(0, 'code/')
from Utils import *
from data_amount import *
import pandas as pd

def get_all_data_nums(filename):
	"""Gets the number of datasets in a csv and writes it to the csv
	"""
	df = read_from_csv(filename)

def main():
	all_city_dataset = 'data/all_city_data.csv'
	get_all_data_nums(all_city_dataset)
	return

if __name__ == '__main__':
	main()