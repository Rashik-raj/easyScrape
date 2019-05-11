from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

def reqUrl(url_name):

	#connection with the site
	uClient = uReq(url_name)

	#read the html
	page_html = uClient.read()

	#close the connection
	uClient.close()

	#beautify the html file for easy read
	page_soup = soup(page_html,"html.parser")

	return page_soup

def createFile(contents):
	file_name = "scrape.txt"
	f = open(file_name, "w")
	f.write(str(contents))
	f.close()
