from urllib import request
import lxml
from lxml import html
import Utils as utils
import re
from data_amount import *
import data_amount as data_amount

def prune(url, browse_boolean):
    """
    This function will return true when the graph should continue searching
    and false when the graph should stop. 
    """
    url = url.lower().strip()
    if 'linkedin'in url:
        return False
    elif 'twitter' in url:
        return False
    elif 'socrata' in url:
        return False
    elif 'login' in url:
        return False
    elif 'mail' in url:
        return False
    else:
        return ((browse_boolean and (('browse' not in url) or ('page' in url))) or not browse_boolean)


def get_all_dataset_pages(url, add_to_url, max_ds_num):
    """
    This function will get all urls ending in '/browse?limitTo=datasets&utf8%2Fbrowse%3FlimitTo=datasets&utf8=&page=##'
    """
    range_of_ds = range(1,(max_ds_num + 20)//10)
    ds_pages = []
    for i in range_of_ds:
        ds_pages += [(url + add_to_url + str(i))]
    return ds_pages


def search(url, add_to_url = '/browse?limitTo=datasets&utf8%2Fbrowse%3FlimitTo=datasets&utf8=&page=', browse_boolean = False, data_set_list = []):
    """
    This function will search through the 
    web graph in order to find the datasets
    """
    ds_len = data_amount.main(url)
    url = url + add_to_url
    url_list = []
    dataset_pages = get_all_dataset_pages(url, add_to_url, ds_len)
    pattern = re.compile(r'/([a-z]|[0-9]){4}-([a-z]|[0-9]){4}')
    
    for url in dataset_pages:
        try:
            http_response = request.urlopen(url)
            open_response = http_response.read().decode('utf-8')
            raw_html = lxml.html.fromstring(open_response)
        except:
            continue
        for link in raw_html.xpath('//a/@href'):
            if '#' in link:
                continue
            if ('limit' in link and add_to_url == ''):
                continue
            if link[-1:] == '#':
                continue
            if link in url:
                continue
            if "http" not in link:
                link = url + link
            else:
                if pattern.match(link[-10:]) is not None and 'socrata' not in link.lower():
                    print("Made it:{}".format(link))
                    if link in data_set_list:
                        continue
                    else:
                        data_set_list += [link]
                    continue
    return data_set_list

def main(url = 'https://data.sfgov.org'):
	return search(url)


if __name__ == '__main__':
	main()
