import urllib.request, urllib.error
from fpdf import FPDF


saveDirectory = "./book/" # For images
extension = ".jpg"
pageWidth = 983
pageHeight = 1270
pageSizeMod = 1/4.5 # FPDF resizes the pages weirdly
quality = 90
pageNum = 200 # Starting page
lastPageNum = 202 # Last page
imageList = []

baseLink = "https://img.yumpu.com/54479513/{0}/{1}x{2}/{0}{3}?quality={4}".format(
	pageNum, pageWidth, pageHeight, extension, quality)

# Downloads image from url to destination
def downloadImage(url, destDir, name):
	a = urllib.request.urlretrieve(url, destDir + name)
	print("Saving {} to {}{}".format(url, destDir, name))

# Returs if given link replies with error code 404
# This site doesn't return 404, just returns an image, so this doesn't work  >:^C
def is404(url):
	try:
	 	req = urllib.request.urlopen(url)
	except urllib.error.HTTPError as e:
	 	return e == 404
	return False

def hasPassedLastPage(pageNum):
	return pageNum > lastPageNum

# Gets the name of a given page with its extension
def getPageName(pageNum):
	return "{}{}".format(pageNum, extension)


currentUrl = baseLink

while (not hasPassedLastPage(pageNum)):
	imageList.append(saveDirectory + getPageName(pageNum))
	downloadImage(currentUrl, saveDirectory, getPageName(pageNum))
	
	# Increment page
	pageNum += 1
	currentUrl = "https://img.yumpu.com/54479513/{0}/{1}x{2}/{0}{3}?quality={4}".format(
		pageNum, pageWidth, pageHeight, extension, quality)

print("Finished downloading")
print("Packing files into book.pdf")
pdf = FPDF()
for image in imageList:
	pdf.add_page()
	pdf.image(image, 0, 0, pageWidth*pageSizeMod, pageHeight*pageSizeMod)
pdf.output("book.pdf", "F")
print("Done")
