import networkx as nx
from Utils import *
from urllib import request
import re


def main(url = 'https://data.cityofberkeley.info/311/311-Cases/k489-uv4i'):
	return get_key_words_and_titles(url)

def get_key_words_and_titles(url):
	return get_titles(url) + get_key_words(url)

def get_titles(url):
	html = request.urlopen(url).read()
	reg = re.compile(r'<title>(.*)</title>', re.DOTALL).search(html).group(0)
	return reg[7:-8].split('|')[0].split('-')[0].split()

def get_key_words(url):
	html = request.urlopen(url).read()
	reg = re.compile(r'<meta name="keywords" content="(.*)"/>', re.DOTALL).search(html).group(0)
	reg2 = reg.split('/>')[0]
	return reg2[31:len(reg2) -2].split(',')

if __name__ == '__main__':
	main()