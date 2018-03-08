import urllib2
import lxml.html

global url_list
url_list = []
visited = []
def find_all_links(url, depth, constraint = None):
	### This function will find all hyperlinks in a given website up to a 
	### depth. It will also check all links against a constraint function. 
	### It will return a list with all of these functions in them. 
	global url_list
	if url[-1] == "/":
		url = url[1: len(url) - 1]
	if constraint != None:
		if constraint(url):
			url_list += [url]
			return url_list
	else:
		url_list += [url]

	if depth == 0:
		return url_list
	if url in visited:
		return url_list
	else:
		visited += [url]

	try:
		connection = urllib2.urlopen(url)
		dom = lxml.html.fromstring(connection.read())
	except:
		return

	for link in dom.xpath('//a/@href'):
		if "http" not in link:
			link = url + link
			print link
		find_all_links(link, depth - 1, constraint)

def constraint(url):
	return url[-5:] == "/data"


find_all_links("https://data.cityofberkeley.info", 3, constraint)