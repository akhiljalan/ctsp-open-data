from urllib import request
import lxml
from lxml import html
import Utils as utils
import breadth as breadth
import re
import graph_dataset_search as gds
import data_amount as data_amount
import json


def get_stats(url, data_url):
    """
    Takes open data platform url and dataset url and gets significant statistics from it, 
    writes to csv. 
    """
    
    json_url = "{}/api/views/{}/rows.json?accessType=DOWNLOAD".format(url, data_url[-9:])


    
    with request.urlopen(json_url) as url:
        data = json.loads(url.read().decode())
        
    name =  data['meta']['view']['name']
    created = data['meta']['view']['createdAt']
    category = data['meta']['view']['category']
    indexUpdated = data['meta']['view']['indexUpdatedAt']
    numComments = data['meta']['view']['numberOfComments']
    viewCount = data['meta']['view']['viewCount']
    viewLastModified = data['meta']['view']['viewLastModified']
    tags = str(breadth.get_key_words(data_url))[2:-2]
    return {'Name': name, 'Category': category, 'Created': created, 
    'Index Updated': indexUpdated, 'Number of Comments': numComments, 'Number of Views': viewCount, 'View Last Modified': viewLastModified, 'Tags': tags}


def write_all_csv(name, data_dict):
	filename = '../{}_data.csv'.format(name)
	for i in data_dict:
		write_to_csv(i, data_dict[i], filename)


def main(url = 'https://data.sfgov.org', data_url = 'https://data.sfgov.org/Transportation/Air-Traffic-Passenger-Statistics/rkru-6vcg' ):
	temp = get_stats(url, data_url)
	write_all_csv('SF', temp)


if __name__ == '__main__':
	main()