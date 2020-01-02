import config 
import requests
from util import *
from url_util.url_util import (get_origin_url, is_url, shorten_url, 
    remove_url_fragment, remove_url_file)
from bs4 import BeautifulSoup

url = format_url(input("url: "))
depth = int(input("depth: "))

# Extract base url
base_url = get_origin_url(url)
if base_url[-1] != "/":
    base_url = base_url + "/"

print()

# Create "sites" directory
create_directory(config.SITES_PATH)
current_dir = "sites"
saved_urls = []

def save_url(url, depth, path="", failed=False):
    saved_urls.append(
        {"url": url, "depth": depth, "path": path, "failed": failed})

def is_url_saved(url):
    for obj in saved_urls:
        if url == obj["url"]:
            return True
    return False

def get_saved_url(url):
    for obj in saved_urls:
        if url == obj.get("url"):
            return obj

def get_relative_url(url, href):
    '''Returns address referenced by href element at url'''
    # Return href if absloute url
    if href[:4] == "http":
        return href
    goup_count = len(stri(href, "../")) + 1
    temp = url[:]
    for i in range(goup_count):
        temp = goup(temp)
    # Add slash if not present
    if href[0] != "/" and temp[-1] != "/":
        temp = temp + "/"
    return temp + href

def get_site_name(url):
    parent_url = goup(url)
    if url != parent_url:
        url = url.replace(parent_url, "")
    name = remove_url_fragment(url)
    name = remove_leading_strings(name,
        ["/", "../", "\\", "http://", "https://"])
    dot_index = name.rfind(".")
    if dot_index != -1:
        name = name[:dot_index]
    return clean_up_file_name(name)

def woffline(current_url, current_dir, remaining_depth):
    current_depth = depth - remaining_depth
    try: # TODO add max retry count when not responding or max timeout
        res = requests.get(current_url)
    except:
        save_url(current_url, current_depth, True)
        return "#"
    soup = BeautifulSoup(res.content, "html5lib")
    name = get_site_name(current_url)
    # Create directory if starting page
    if current_depth == 0:
        new_dir = current_dir + "/" + name
        create_directory(new_dir)
    else:
        new_dir = current_dir
    file_path = new_dir + "/" + name + ".html"
    for a in soup.find_all("a"):
        href = a.get("href")
        if remaining_depth > 0 and href:
            pattern = ".html"
            # TODO add check function to determine if link is a webpage
            if href[-len(pattern):] == pattern or href[0] == "/":
                url = get_relative_url(current_url, href)
                print("[URL] " + url)
                if is_url_saved(url):
                    a["href"] = get_saved_url(url).get("path")
                else:
                    a["href"] = woffline(url, new_dir, remaining_depth - 1)
    fully_download(soup, file_path)
    ret = name + ".html"
    save_url(current_url, current_depth, ret, False)
    return ret

def fully_download(soup, file_path):
    file = open(file_path, "w+", encoding="utf-8")
    # TODO: Download resources here
    file.write(soup.prettify())
    file.close()
    print("[DONE]: "+ file_path)
    return file_path

woffline(url, current_dir, depth)