#!/usr/bin/env python2

import urllib2
import lxml.html
import csv


global url_list
global visited
global adjacency_lists
global depth_list
url_list = []
visited = []
adjacency_lists = {}
depth_list = []

def find_all_links(url, depth, constraint = None):
	### This function will find all hyperlinks in a given website up to a 
	### depth. It will also check all links against a constraint function. 
	### It will return a list with all of these functions in them. 
	global url_list, visited, adjacency_lists, depth_list
	local_adj_list = []
	if url[-1] == "/":
		url = url[0 : len(url) - 1]
	print ("At depth: {}".format(depth))
	depth_list += [depth]

	if "dev.socrata" in url:
		return local_adj_list
	if constraint != None:
		if constraint(url):
			print url
			local_adj_list += [url]
			return local_adj_list
	else:
		local_adj_list += [url]

	if depth == 0:
		return local_adj_list
	if url not in visited: 
		visited += [url]
	
	local_adj_list += [url]
	try:
		connection = urllib2.urlopen(url)
		dom = lxml.html.fromstring(connection.read())
		if len(dom.xpath('//a/@href')) < 4:
			return local_adj_list
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

if __name__ == '__main__': 
	find_all_links("https://data.cityofberkeley.info", 2)


f = open('../data/url_list.txt','w')
g = open('../data/edges.txt','w')
for i in range(len(url_list)):
	f.write("Depth: {} | URL: {} \n".format(depth_list[i], url_list[i]))
	url = url_list[i]
	try:
		for linked_url in adjacency_lists[url]:
	 		g.write('From {} to ----- Linked url:{} \n'.format(url, linked_url))
	except KeyError as e:
	 	pass
f.close()
g.close()

