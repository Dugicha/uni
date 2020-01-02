import config 
import requests
import sys
from util import *
from url_util.url_util import get_origin_url
from bs4 import BeautifulSoup


url = format_url(input("url: "))
current_depth = input("depth: ")

file_name = ""
base_url = get_origin_url(url)
if base_url[-1] != "/":
    base_url = base_url + "/"

print()

create_directory(config.SITES_PATH)


# Get website
res = requests.get(url)
# Soupify
soup = BeautifulSoup(res.content, "html5lib")

def woffline(url, depth):
    #TODO recursively woffline all .html files
    pass

def fully_download(soup):
    # Fully downloads and organizes resources from given soup
    pass



# Save original as backup for testing and comparison
save_pretty_soup(soup, config.SITES_PATH)

dir_name = config.SITES_PATH[:]
# If html has title, set that as file name
try:
    title = clean_up_file_name(soup.title.string)
    dir_name += title
    file_name = f"{dir_name}/{title}.html"
except:
    title = config.DEFAULT_FILE_NAME
    dir_name += title
    file_name = f"{dir_name}/{title}.html"

# Create separate directory for site
print("file_name = " + file_name)
create_directory(dir_name)
file = open(file_name, "w+", encoding="utf-8")

# Create resource directory
res_dir = dir_name + "/" + config.RES_PATH
create_directory(res_dir)

# Download resources
## Styles
for style in filter(is_link_external_style, soup.find_all("link")):
    style["href"] = download_css(style, base_url, res_dir, config.RES_PATH)
    clean_up_new_tag(style)
### Repoint resources in internal styles
for i, style in enumerate(soup.find_all("style")):
    css_name = "inline_style" + str(i)
    style.string = repoint_css_resources(style.string, css_name, res_dir, 
                                         base_url, config.RES_PATH)
## Images
for img in soup.find_all("img"):
    img["src"] = download_image(img, base_url, res_dir, config.RES_PATH)
    clean_up_new_tag(img)
## Scripts
for script in soup.find_all("script"):
    src = script.get("src")
    # Download if not inline
    if src:
        script["src"] = download_js(script, base_url, res_dir, config.RES_PATH)
        clean_up_new_tag(script)
## HTML
for child in soup.descendants:
    try:
        if child.get("style"):
            child["style"] = repoint_css_resources(child["style"], child.name,
                                                   res_dir, base_url, config.RES_PATH)
    except AttributeError:
        pass

# Write final html
file.write(soup.prettify())
file.close()

print("Website downloaded!") 
print()
