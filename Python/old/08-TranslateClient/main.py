import json
import urllib.request
from pprint import pprint

q = input("translate: ")
url = "http://translate.ge/api/{}".format(q)

f = urllib.request.urlopen(url)

with f as dataFile:
	parsedJson = json.load(dataFile)	

print(parsedJson["rows"][0]["value"]["Text"])