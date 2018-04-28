from urllib import request
import lxml
from lxml import html
import Utils as utils
import breadth as breadth
import re
import graph_dataset_search as gds
import data_amount as data_amount
import json
import pandas as pd

def get_stats(url, data_url):
    """
    Takes open data platform url and dataset url and gets significant statistics from it, 
    writes to csv. 
    """
    try:
		json_url = "{}/api/views/{}/rows.json?accessType=DOWNLOAD".format(url, data_url[-9:])
		with request.urlopen(json_url) as jurl:
		    data = json.loads(jurl.read().decode())
		name =  data['meta']['view']['name']
		created = data['meta']['view']['createdAt']
		category = data['meta']['view']['category']
		indexUpdated = data['meta']['view']['indexUpdatedAt']
		downloadCount = data['meta']['view']['downloadCount']
		viewCount = data['meta']['view']['viewCount']
		viewLastModified = data['meta']['view']['viewLastModified']
		tags = breadth.get_key_words(data_url)
	except:
		return None
    return {'Name': [name],'URL': [data_url], 'Category': [category], 'Created': [created], 
    'Index Updated': [indexUpdated], 'Number of Downloads': [downloadCount], 'Number of Views': [viewCount], 'View Last Modified': [viewLastModified], 'Tags': [tags]}


def write_all_csv(filename, data_dict):
	for i in data_dict:
		utils.write_to_csv(i, data_dict[i], filename)




def main():
	all_city_data = utils.read_from_csv('../data/all_city_data.csv')
	city_to_url_dict = dict(zip(all_city_data['City Name'], all_city_data['City Open Data URL']))

	for city in city_to_url_dict:
		city = str(city)
		filename = '../data/{}.csv'.format(str(city).replace(' ',''))
		ds_list = gds.main(city_to_url_dict[str(city)])
		for ds in ds_list:
			temp = get_stats(city_to_url_dict[city], ds)
			write_all_csv(filename, temp)
	
	#write_all_csv('SF', temp)


if __name__ == '__main__':
	main()