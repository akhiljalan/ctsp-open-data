# #!/usr/bin/env python2

from urllib import request
import lxml
from lxml import html



# url_list = []
# visited = []
# adjacency_lists = {}
# depth_list = []

def find_incident_nodes(url):
	'''
	url: The current node (webpage) as a string. 
	''' 
	# all incident nodes from current url 
	local_adj_list = []

	try:
		http_response = request.urlopen(url)
		open_response = http_response.read()
		raw_html = lxml.html.fromstring(open_response)
	except error as e: 
		print(e)
		# print('Error: {}'.format(e))
		return local_adj_list

	# adjacency_lists[url] = []
	for link in raw_html.xpath('//a/@href'):
		if link in ['#', url]: 
			print('Ignoring link {} from {}'.format(link, url))
			pass
		if "http" not in link:
			# avoid relative links
			link = url + link
		local_adj_list.append(link)

	return local_adj_list

def bfs_search(start_url): 
	all_adj_list = {}
	visited_nodes = []
	queue = [start_url]
	while queue != [] and len(visited_nodes) < 10:
		current_url = queue.pop(0)
		visited_nodes.append(current_url)

		#do BFS on one layer. 
		incident_nodes = find_incident_nodes(current_url)

		#update adjacency list 
		all_adj_list[current_url] = incident_nodes


		for node in incident_nodes: 
			if node not in visited_nodes: 
				queue.append(node)
		print('From {} to {}'.format(current_url, all_adj_list[current_url]))
	return all_adj_list

def main(): 
	link = 'https://www.cityofberkeley.info'
	link2 = 'https://stats.stackexchange.com/questions/51185/connection-between-fisher-metric-and-the-relative-entropy'
	bfs_search(link2)

if __name__ == "__main__":
	main()