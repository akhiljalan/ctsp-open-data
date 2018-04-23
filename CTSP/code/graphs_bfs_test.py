# #!/usr/bin/env python2

from urllib import request
import lxml
from lxml import html
import Utils as utils
from bs4 import BeautifulSoup



# url_list = []
# visited = []
# adjacency_lists = {}
# depth_list = []

# def condition(link):
# 	to_avoid = ["dev.socrata.com", "www.socrata.com"] 
def parse(page_html):
	parsed_html = BeautifulSoup(html, "lxml")
	print(parsed_html)
	return parsed_html.body.find('div', attrs={'class':'browse2-results'}) + parsed_html.body.find('div', attrs={'class':'browse2-results-pagination-controls'}) 

def find_incident_nodes(url):
	'''
	url: The current node (webpage) as a string. 
	''' 
	# all incident nodes from current url 
	local_adj_list = []

	try:
		http_response = request.urlopen(url)
		open_response = http_response.read()
		# print(open_response)
		parsed_html = parse(open_response)
		raw_html = lxml.html.fromstring(parsed_html)

	except: 
		# print('Error: {}'.format(e))
		return local_adj_list

	# adjacency_lists[url] = []
	print(raw_html.xpath('//a/@href'))
	for link in raw_html.xpath('//a/@href'):
		if link in ['#', url] or not ("berkeley" in link or "data" in link): 
			# print(url + link)
			# print('Ignoring link {} from {}'.format(link, url))
			continue	
		if "http" not in link:
			# avoid relative links
			link = url + link
		local_adj_list.append(link)

	return local_adj_list

def homepages(city):
	homepages = {}
	homepages["berkeley"] = ["https://www.cityofberkeley.info/Home.aspx", "https://www.cityofberkeley.info/Home.aspx#", "https://www.cityofberkeley.info", "http://www.ci.berkeley.ca.us/Home.aspx"]
	return 

def look_ahead(adj_list):
	berkeley = ["https://www.cityofberkeley.info/Home.aspx", "https://www.cityofberkeley.info/Home.aspx#", "https://www.cityofberkeley.info", "http://www.ci.berkeley.ca.us/Home.aspx"]
	for l in adj_list:
		if l in berkeley:
			return "homepage"
		elif l[:-5] == "/data":
			return "data"
	return ""

def bfs_search(start_url): 
	all_adj_list = {}
	visited_nodes = []
	queue = [start_url]
	num_data_sets = 0
	breadth = 0
	while queue != [] and num_data_sets < 25:
		current_url = queue.pop(0)
		if "berkeley" in current_url or "data" in current_url:
			visited_nodes.append(current_url)

			#do BFS on one layer. 
			incident_nodes = find_incident_nodes(current_url)

			#update adjacency list 
			all_adj_list[current_url] = incident_nodes
			# print(num_data_sets)
			# print(current_url)
			# print(incident_nodes)
			stop = look_ahead(incident_nodes)
			# if stop == "homepage":
			# 	continue
			if stop == "data":
				num_data_sets += 1
				continue
			else:
				for node in incident_nodes: 
					if node not in visited_nodes: 
						queue.append(node)
			
		# print(current_url)
		# print(len(visited_nodes))
		# print('From {} to {}'.format(current_url, all_adj_list[current_url]))
	return all_adj_list

def main(): 
	link = 'https://www.cityofberkeley.info'
	link2 = 'https://stats.stackexchange.com/questions/51185/connection-between-fisher-metric-and-the-relative-entropy'
	link3 = 'https://data.cityofberkeley.info'
	link4 = "https://data.cityofberkeley.info/browse?limitTo=datasets&utf8"
	link_dict = bfs_search(link4)
	param, value = link4.split("//", 1)
	param, value = value.split('/', 1)
	utils.save_object(link_dict, value + param)


if __name__ == "__main__":
	main()