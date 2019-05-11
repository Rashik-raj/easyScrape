from easyScrape import reqUrl, createFile
url = "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card"
items = reqUrl(url)
createFile(items)