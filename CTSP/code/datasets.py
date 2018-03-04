import urllib2
import lxml.html

global url_list
url_list = []
def find_all_links(url, depth, constraint = None):
### This function will find all hyperlinks in a given website up to a 
### depth. It will also check all links against a constraint function. 
### It will return a list with all of these functions in them. 
	global url_list
	if constraint != None:
		if constraint(url):
			url_list += [url]
			return url_list
	else:
		url_list += [url]

	if depth == 0:
		return url_list

	connection = urllib2.urlopen(url)
	dom = lxml.html.fromstring(connection.read())

	for link in dom.xpath('//a/@href'):
		if "http" not in link:
			link = url + link
			print link
		find_all_links(link, depth - 1, constraint)






