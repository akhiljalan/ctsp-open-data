# import networkx as nx
from Utils import *
from urllib.request import urlopen, Request
import urllib
from urllib.request import urlopen


def extract_last_modified(response_string): 
	arr = response_string.split('\n')
	found = False
	for item in arr: 
		if 'Last-Modified:' in item:
			print(item[len('Last-Modified:'):])
			found = True
	if not found: 
		print('Nothing')




def print_meta(link): 
	try: 
		# print(urlopen(link).info().__str__())
		response_str = urlopen(link).info().__str__()
		print(response_str)
		extract_last_modified(response_str)
	except: 
		print('An error occurred with {}'.format(link))

def get_raw_str(url):
	response = urlopen(url)
	raw = response.read()
	raw_str = raw.decode('utf-8')
	return raw_str

def main():
	link1 = 'https://data.cityofberkeley.info/311/311-Cases/k489-uv4i'
	link_str = get_raw_str(link1)
	print(len(link_str))
	# 

	# print(len(stuff))
	# cities = ['http://www.ci.antioch.ca.us/', 'https://www.menlopark.org/', 'http://www.ci.richmond.ca.us/',
	# 			'https://www.cityofpaloalto.org/', 'https://sfgov.org/', 'https://www.srcity.org/', 
	# 			'http://www.cityofnapa.org/', 'https://www.sanjoseca.gov/']
	# other_links = ['https://www.cnn.com/2011/11/02/world/meast/egypt-refugees/index.html', 
	# 				'https://www.cnn.com/2018/04/12/sport/kenya-rugby-sevens-commonwealth-games-spt/index.html']
	# for city in other_links: 
	# 	print('------------------------------------------')
	# 	print('Trying: {}'.format(city))
	# 	print_meta(city)
	

if __name__ == '__main__':
	main()