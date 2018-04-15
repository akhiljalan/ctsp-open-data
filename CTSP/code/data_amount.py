from Utils import *
import re
from urllib import request



def main():
	return get_num_from_origin('https://data.sfgov.org/')

def get_num_from_origin(origin_website = 'https://data.cityofberkeley.info'):
	try:
		return get_num_datasets(origin_website + '/browse?limitTo=datasets&utf8')
	except:
		return get_num_datasets(origin_website + 'browse?limitTo=datasets&utf8')
def get_num_datasets(data_cat_url):
	html = request.urlopen(data_cat_url).read()
	regexed_str = re.compile(r'<div class="browse2-results-title">(.+)</div>', re.DOTALL).search(html).group(0)
	temp = regexed_str.split('div')
	for i in temp[1].split():
		try:
			temp2 = int(i)
		except:
			pass
	return temp2

if __name__ == '__main__':
	data_set_name = main()
	print data_set_name
	#save_object(data_set_name, 'num_of_data_sets')
	#print(read_object('num_of_data_sets'))