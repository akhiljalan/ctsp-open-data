import urllib3 as ul
import lxml.html

global url_list
url_list = []

def isdata(link):
	return link[-5:] == "/data"

def find_all_links(url, depth, constraint = None):
### This function will find all hyperlinks in a given website up to a 
### depth. It will also check all links against a constraint function. 
### It will return a list with all of these functions in them. 
	if constraint != None:
		if constraint(url):
			url_list += [url]
			return url_list
	else:
		url_list += [url]

	if depth == 0:
		return url_list

	connection = ul.urlopen(url)
	dom = lxml.html.fromstring(connection.read())

	for link in dom.xpath('//a/@href'):
		if "http" not in link:
			link = url + link
		find_all_links(link, depth - 1, constraint)

find_all_links("https://data.cityofberkeley.info", 3, isdata)






