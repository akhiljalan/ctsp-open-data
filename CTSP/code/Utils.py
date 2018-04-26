import csv
import pickle
import os
import pandas as pd
import sys


def save_object(obj, filename):
	"""
	 Serializes an object to a binary file format
    """
	filepath = os.path.join("../data/dict", filename)
	with open(filepath, 'wb') as output:  
	# Overwrites any existing file.
		pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

def read_object(filename):
	"""
	Reads a serialized object froma a binary format
	"""
	with open(filename, 'rb') as openfile: 
		try:
			return pickle.load(openfile)
		except EOFError:
			return



def write_to_csv(col_name, col_data, filename):
	"""
	Writes a column name and data (in list format) to a 
	.csv filename. 
 	"""
	try:
		temp_df = pd.read_csv(filename)
		temp_df[col_name] = col_data
	except:
		temp_df = pd.DataFrame(
		{
		col_name:col_data
		}
	)
	temp_df.to_csv(filename, index = False)


def read_from_csv(filename):
	"""
	Reads a csv into a pandas dataframe
	"""
	try:
		return pd.read_csv(filename)
	except:
		return None
 	
