
from urllib import request
from lxml import html
import os 
import csv

adjacency_lists = {}

def find_links(url):
	adjacency_lists[url] = []
	
	try:
	connection = urllib.request.urlopen(url)
	dom = lxml.html.fromstring(connection.read())
	except:
		print("permission errors")

	for link in dom.xpath:
		if "http" not in link:

		else if "data" in link:
		else:
			link = url + link
		adjacency_lists[url] += link
		find_links(link)

def createTextFile():
    try:
        myFilePath = os.path.join(filePath, 'SimpleFile.txt')
        with open(myFilePath,'w') as myFile:
            myFile.write("This is a Simple Text file\n")
            myFile.write("This is line number 1\n")
            
            myList = ["This is line number 2\n",
                      "This is line number 3\n",
                      "This is line number 4\n"]
            myFile.writelines(myList)
    except IOError as (errno, strerror):
        print("I/O error({0}): {1}".format(errno, strerror)) 
        
    return

def fromDictToCSV():
    
    try:
        myFilePath = os.path.join(filePath, 'MyDictionary.csv')
        with open(myFilePath,'w', newline='') as myCSVFile:
            csvWriter = csv.DictWriter(myCSVFile, fieldnames=headings, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
            csvWriter.writeheader()
            for data in myDictData:
                csvWriter.writerow(data)
    except IOError as (errno, strerror):
        print("I/O error({0}): {1}".format(errno, strerror)) 
        
    return
