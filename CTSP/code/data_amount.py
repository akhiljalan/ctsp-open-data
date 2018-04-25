from Utils import *
import re
from urllib import request



def main(url):
	return int(get_num_from_origin(url))

def get_num_from_origin(origin_website = 'https://data.cityofberkeley.info'):
	try:
		return get_num_datasets(origin_website + '/browse?limitTo=datasets&utf8')
	except:
		return get_num_datasets(origin_website + 'browse?limitTo=datasets&utf8')
def get_num_datasets(data_cat_url):
	html = request.urlopen(data_cat_url).read().decode('utf-8')
	regexed_str = re.compile(r'<div class="browse2-results-title">(.+)</div>', re.DOTALL).search(html).group(0)
	temp = regexed_str.split('div')
	for i in temp[1].split():
		try:
			temp2 = int(i)
		except:
			continue
	return temp2

def name():
    return "Amount of Data"

if __name__ == '__main__':
	data_set_name = main('https://datasf.org/opendata')
	
