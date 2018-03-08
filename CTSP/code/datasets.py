#!/usr/bin/env python2

import urllib2
import lxml.html
import csv


global url_list
global visited
global adjacency_lists
url_list = []
visited = []
adjacency_lists = {}

def find_all_links(url, depth, constraint = None):
	### This function will find all hyperlinks in a given website up to a 
	### depth. It will also check all links against a constraint function. 
	### It will return a list with all of these functions in them. 
	global url_list, visited, adjacency_lists
	#global visited
	#global adjacency_lists
	local_adj_list = []
	if url[-1] == "/":
		url = url[0 : len(url) - 1]
	print ("At depth: {}".format(depth))

	if "dev.socrata" in url:
		return local_adj_list
	if constraint != None:
		if constraint(url):
			print url
			#url_list += [url]
			local_adj_list += [url]
			return local_adj_list
	else:
		#url_list += [url]
		local_adj_list += [url]

	if depth == 0:
		return local_adj_list
	if url not in visited: 
		visited += [url]
	# if url in visited:
	# 	local_adj_list += [url]
	# else:
	# 	visited += [url]
	local_adj_list += [url]
	try:
		connection = urllib2.urlopen(url)
		dom = lxml.html.fromstring(connection.read())
	except:
		return local_adj_list

	for link in dom.xpath('//a/@href'):
		if "http" not in link:
			link = url + link
		link_adj_list = find_all_links(link, depth - 1, constraint)
		adjacency_lists[link] = link_adj_list
		url_list += link_adj_list

def constraint(url):
	### This defines a constraint function that looks at just the url. 
	return url[-5:] == "/data"

# if name == '__main__': 
find_all_links("https://data.cityofberkeley.info", 1)
with open('../data/test2.csv', 'wb') as myfile:
	wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
	for url in url_list:
		wr.writerow(url)
		try:
			# print(adjacency_lists[url])

			for linked_url in adjacency_lists[url]:
				print('From {} to ----- Linked url:{}'.format(url, linked_url))
				wr.writerow(adjacency_lists[linked_url])
		except KeyError as e: 
			pass
