from urllib.request import Request as conReq
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

def reqUrl(url_name):
	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
	       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
	       'Accept-Encoding': 'none',
	       'Accept-Language': 'en-US,en;q=0.8',
	       'Connection': 'keep-alive'}

	req = conReq(url_name, headers=hdr)
	#connection with the site
	uClient = uReq(req)

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
