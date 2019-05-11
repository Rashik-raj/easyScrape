# easyScrape
It is library file to make your webScrape easy and faster to use

### PRE-REQUISITION
**Must have installed beautifulSoup package**

### USE DIRECTION
1. Download easyScrape.py
2. Import easyScrape
3. Pass url-name to reqUrl() function and store it into a variable
4. If needed you can create a file for the data you have scraped by passing scraped data into createFile() function

### Example
```
from easyScrape import reqUrl, createFile
url = "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card"
items = reqUrl(url)
createFile(items)
```
