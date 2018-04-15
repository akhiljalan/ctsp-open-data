import csv
import pickle
import os


def save_object(obj, filename):
	### Serializes an object to a binary file format
    
    filepath = os.path.join("../data/dicts", filename)
    with open(filepath, 'wb') as output:  # Overwrites any existing file.
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

def read_object(filename):
	### Reads a serialized object froma a binary format
	with open(filename, 'rb') as openfile: 
		try:
			return pickle.load(openfile)
		except EOFError:
			return


# def write_to_csv(obj):
# 	###TODO

# def read_from_csv(filename):
# 	###TODO
