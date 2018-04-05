#!/usr/bin/env python2

import urllib2
import lxml.html
import csv
import h5py
import deepdish as dd

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
	

	if "dev.socrata" in url:
		return local_adj_list
	if constraint != None:
		if constraint(url):
			print url
			#url_list += [url]
			local_adj_list += [url]
			return local_adj_list
	else:
		url_list += [url]
		local_adj_list += [url]
#fine
	if url not in visited: 
		visited += [url]

	if depth == 0:

		return local_adj_list
	
	
	# if url in visited:
	# 	local_adj_list += [url]
	# else:
	# 	visited += [url]
	# local_adj_list += [url]
	try:
		connection = urllib2.urlopen(url)
		dom = lxml.html.fromstring(connection.read())

	except:
		return local_adj_list

	adjacency_lists[url] = []
	for link in dom.xpath('//a/@href'):

		if "http" not in link:
			link = url + link

		
		link_adj_list = find_all_links(link, depth - 1)


		# if link_adj_list == None:
		# 	return 
		# print link_adj_list
		adjacency_lists[url] += [link]
		adjacency_lists[link] = link_adj_list

		url_list += link_adj_list 
		depth_list += [depth]

	return local_adj_list


def constraint(url):
	### This defines a constraint function that looks at just the url. 
	return url[-5:] == "/data"

if __name__ == "__main__":
	link = "https://www.cityofberkeley.info"
	find_all_links(link, 1)
	links_from_berkeley = adjacency_lists

	dd.io.save('berkeley_city_links_dict.h5', {'adjacency_lists': links_from_berkeley}, 
		compression=('blosc', 9))

	f = open('../data/url_list2.txt','w')
	g = open('../data/edges2.txt','w')
	for i in range(len(url_list)):
		try:
			f.write("Depth: {} | URL: {} \n".format(depth_list[i], url_list[i]))
		except IndexError as e:
			print "There was an error"
		url = url_list[i]
		try:
			for linked_url in adjacency_lists[url]:
		 		g.write('From {} to ----- Linked url:{} \n'.format(url, linked_url))
		except KeyError as e:
		 	pass
	f.close()
	g.close()

