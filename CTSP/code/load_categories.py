def load_unique(filename):
	with open(filename, 'r') as f:
		all_cat = set(f.readline().split(','))
	return all_cat

def main(): 
	print(load_unique('../categories.txt'))

if __name__ == '__main__':
	main()