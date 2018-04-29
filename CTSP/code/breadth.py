
from Utils import *
from urllib import request
import re


def main(url = 'https://data.cityofberkeley.info/311/311-Cases/k489-uv4i'):
    print(get_key_words_and_titles(url))
    return get_key_words_and_titles(url)

def get_key_words_and_titles(url):
	return list(set(get_titles(url) + get_key_words(url)))

def get_titles(url):
	html = request.urlopen(url).read().decode('utf-8')
	reg = re.compile(r'<title>(.*)</title>', re.DOTALL).search(html).group(0)
	return reg[7:-8].split('|')[0].split('-')[0].strip().split()

def get_key_words(url):
	html = request.urlopen(url).read().decode('utf-8')
	reg = re.compile(r'<meta name="keywords" content="(.*)"/>', re.DOTALL).search(html).group(0)
	reg2 = reg.split('/>')[0]
	return reg2[31:len(reg2) -2].strip().split(',')

def name():
    return "Breadth of Dataset"

if __name__ == '__main__':
	main()
