import urllib.request, urllib.error
import os
import glob
from fpdf import FPDF


save_dir = "book/" # For images
extension = ".jpg"
page_width = 495
page_height = 640
page_size_mod = 2/5 # FPDF resizes the pages weirdly
quality = 100
page_limit = 202
image_list = []

def create_dir_if_needed(dest_dir):
	if not os.path.exists(dest_dir):
		os.makedirs(dest_dir)

def get_yn_answer(question):
	ans = ""
	while not ("y" in str(ans) or "n" in str(ans)):
		ans = input(question)

	return "y" in ans

def get_page_url(page_num):
	# Gets url of the page from page number
	return "https://img.yumpu.com/54479513/{0}/{1}x{2}/{0}{3}?quality={4}".format(
	page_num, page_width, page_height, extension, quality)

def download_page(url, dest_dir, name):
	# Downloads an image from given url
	create_dir_if_needed(dest_dir)
	urllib.request.urlretrieve(url, dest_dir + name)
	image_list.append(dest_dir + name)
	print("Downloading {} to {}{}".format(url, dest_dir, name))

def download_pages(page_list):
	# Downloads all pages to directory
	for item in page_list:
		if (item <= page_limit):
			download_page(get_page_url(item), save_dir, str(item) + extension)

def download_pages_range(start = 1, end = 202):
	if (start >= 0 and end <= 202):
		download_pages(range(start, end + 1))
	else:
		print("Wrong input download_pages_range(start, end)")

def get_all_downloaded_images():
	# Returns a list of all download image paths
	return [f for f in os.listdir(save_dir) 
	if f.endswith("jpg") and os.path.isfile(os.path.join(save_dir, f))]

def get_image_count():
	return len(get_all_downloaded_images())

def pack_pages(path, book_name):
	pdf = FPDF()
	print("Packing pages into {}{}.pdf".format(path, book_name))
	for image in image_list:
		pdf.add_page()
		pdf.image(image, None, None, 
			page_width * page_size_mod, page_height * page_size_mod)
	pdf.output(path + book_name + ".pdf", "F")
	print("Done packing pages")


starting = input("first page to download: ")
ending = input("last page to download: ")

download_pages_range(int(starting), int(ending))

print("You have downloaded a total of {} pages".format(get_image_count()))

if (get_yn_answer("Would you like to pack all the pages into a pdf? (y/n)")):
	book_name = input("What shall be the name of the pack? ")
	pack_pages("./", book_name)