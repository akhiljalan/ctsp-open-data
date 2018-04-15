def load_unique(filename):
	with open(filename, 'r') as f:
		all_cat = set(f.readline().split(','))
	return all_cat

def load_with_repeats(filename): 
	with open(filename, 'r') as f:
		all_cat = f.readline().split(',')
	return all_cat


def get_categories_from_txt():
	return load_unique('../categories.txt')

if __name__ == '__main__':
	print('No main lol')