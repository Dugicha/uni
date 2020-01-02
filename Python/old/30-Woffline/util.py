# util.py
import requests
import os
import sys
from url_util.url_util import (stri, is_url_file, is_url_fragment, 
    remove_url_fragment, goup, remove_leading_strings, get_resource_url, 
    is_url, get_origin_url)
from config import INVALID_FILE_NAME_CHARS

def save_pretty_soup(soup, save_dir):
    '''Saves backup of passed soup. Used for comparing'''
    with open(save_dir + "original.html", "w+", encoding="utf-8") as f:
        try: 
            f.write(soup.prettify())
            try:
                print(f"Soup \"{soup.title.string}\" backup saved")
            except:
                print("Soup backup saved")
        except error:
            print("Soup backup not saved")
            print("Error: ", error)
    print("="*15)

def download_image(img_tag, origin_url, save_dir, relative_save_folder):
    '''Downloads image from soup <img/> tag and returns relative src. 
    Uses origin url if necessary'''
    img_url = get_resource_url(img_tag, "src", origin_url)
    if img_url == None:
        return None
    img_url = remove_leading_strings(img_url, ["/", "../", "\\"])

    res_name = get_resource_name(img_url)
    res_name = add_extension(res_name, ".png")

    # Returned path used for DOM element
    attr_path = relative_save_folder + res_name
    # Where this file will be saved
    save_path = save_dir + res_name

    print(f"[IMG] {img_url} -> {save_path}")
    stream_file_to(img_url, save_path)
    return attr_path

def download_css(link_tag, origin_url, save_dir, relative_save_folder):
    '''Downloads css from soup <link> tag and returns relative href. 
    Uses origin url if necessary'''
    css_url = get_resource_url(link_tag, "href", origin_url)
    css_url = remove_leading_strings(css_url, ["/", "../", "\\"])

    css_name = get_resource_name(css_url)
    css_name = add_extension(css_name, ".css")

    attr_path = relative_save_folder + css_name
    save_path = save_dir + css_name

    # Download into variable
    print(f"[CSS] {css_url} -> {save_path}")
    r = requests.get(css_url)
    # Repoint and save to variable
    css_text = repoint_css_resources(r.text, css_name, save_dir, origin_url, 
        css_url=css_url)
    # Save to local file
    with open(save_path, "w+", encoding="utf-8") as f:
        f.write(css_text)
    return attr_path

def repoint_css_resources(css_text, css_name, save_dir, origin_url, 
    relative_save_folder = "", css_url = ""):
    '''Scans through css text, downloads pointed (with url()) resources and 
    repoints to them locally. 
    Names each resource: f"{css_name}_r_{get_resource_name(url)}"'''
    start_pattern = "url("
    end_pattern = ")"
    remove_at_start = ["../", "/", "\\"] # removes strings at start of url
    quotation_marks = ["\"", "\'"] # removes quotes if url is wrapped inside
    ret = ""
    temp = css_text[:]
    i = temp.find(start_pattern)
    last = -1
    while(i != -1):
        start = i + len(start_pattern)
        end = temp[start:].find(end_pattern) + start
        # Check for parenthesis syntax error in css 'url()'
        if end == -1:
            print("parenthesis not closed, breaking")
            break
        # Check for quotation marks| TODO: check for whitespace
        if temp[start] in quotation_marks:
            start += 1
            end -= 1
        # Extract url
        url = temp[start:end]
        #print("extracted url:", url, start, end)
        url = url.strip()
        # Remove leading slashes and other chars that screw up origin concat
        url = remove_leading_strings(url, remove_at_start)
        # Add CDN or site origin if necessary
        if (css_url != "" and 
            get_origin_url(css_url) != get_origin_url(origin_url)):
            print("CDN RELATIVE REPOINT")
            url = add_origin(url, css_url)
        else:
            url = add_origin(url, origin_url)
        #print("clean url:", url)
        res_name = f"{css_name}_r_{get_resource_name(url)}"
        # Save file
        save_path = f"{save_dir}{res_name}"
        print(f"[REPOINT] {url} -> {save_path}")
        if stream_file_to(url, save_path) == None:
            print("ERROR: file from url '{}' could not be downloaded to '{}'"
                .format(url, save_path))
            res_name = url
        else:
            res_name = relative_save_folder + res_name
        # TODO recursively download files from imported .css files
        # Last index of code to copy
        last = end + len(end_pattern)
        # Add code to ret css
        ret += temp[:start] + res_name + temp[end:last]
        # Cut off copied code
        temp = temp[last:]
        i = temp.find(start_pattern)
    # Add remaning code
    if len(temp) > 0:
        ret += temp
    return ret

def download_js(script_tag, origin_url, save_dir, relative_save_folder):
    '''Downloads javascript from soup <script> tag and returns relative src. 
    Uses origin url if necessary'''
    js_url = get_resource_url(script_tag, "src", origin_url)
    js_url = remove_leading_strings(js_url, ["/", "../", "\\"])

    res_name = get_resource_name(js_url)
    res_name = add_extension(res_name, ".js")

    attr_path = relative_save_folder + res_name
    save_path = save_dir + res_name

    print(f"[JS] {js_url} -> {save_path}")

    r = requests.get(js_url)
    with open(save_path, "w+", encoding="utf-8") as f:
        f.write(r.text)
    return attr_path

def stream_file_to(url, save_path, chunk_size=1024):
    '''Streams file at url into save_path with passed chunk_size'''
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(save_path, "wb") as f:
            for chunk in r.iter_content(chunk_size):
                f.write(chunk)
        return save_path
    else:
        return None

used_resource_names = [] # stores all resource names
def get_resource_name(r):
    '''Returns clean resource file name from url for local storage''' 
    ret = ""
    # Remove everything until last slash
    for c in r.strip()[::-1]:
        # slashes
        if c in ["\\", "/"]:
            break
        else:
            ret = c + ret
    # Clean up file name
    ret = "_" + replace_chars(ret, INVALID_FILE_NAME_CHARS, "")
    while ret in used_resource_names:
        ret = "_" + ret
    used_resource_names.append(ret)
    return ret

def replace_chars(text, invalids, char):
    '''Returns a string where arg2 characters in arg1 are replaced by arg3'''
    ret = ""
    # Turns invalids into list
    if not (isinstance(invalids, list) or isinstance(invalids, str) 
        or isinstance(invalids, tuple)):
        invalids = [invalids]
    # Iterate and add valid ones only
    for c in text:
        if c in invalids:
            ret = ret + char
        else:
            ret = ret + c
    return ret

def add_extension(file_name, extension):
    '''Adds passed file extension to file name at the end if not present'''
    if file_name[-len(extension):] != extension:
        return file_name + extension
    else:
        return file_name

def add_origin(url, origin_url):
    '''Adds passed origin at start of url if it's a relative url'''
    if is_url(url):
        return url
    else:
        if origin_url[-1] != "/" and url[0] != "/":
            return origin_url + "/" + url
        else:
            return origin_url + url

def create_directory(d):
    '''Creates directory with given path if it doesn't exist. 
    Returns success'''
    try:
        if not os.path.exists(d):
            os.makedirs(d)
        return True
    except:
        return False

def format_url(url):
    '''Adds last slash and protocol to url'''
    ret = url[:]

    remove_url_fragment(ret)

    # Add ending slash
    if url[:-1] != "/" and not is_url_file(url) and not is_url_fragment(url):
        ret = ret + "/"

    # Remove protocol
    if url[:4] != "http":
        ret = "http://" + ret
    return ret

def clean_up_file_name(name):
    return replace_chars(name, INVALID_FILE_NAME_CHARS, "")

def clean_up_new_tag(tag):
    '''Removes unnecessary attributes from soup DOM element'''
    if tag:
        remove = ["crossorigin", "integrity"]
        for attr in remove:
            if tag.get(attr):
                del tag[attr]
        return tag
    else:
        return

def is_link_external_style(link_tag):
    return (("stylesheet" in link_tag.get("rel")) or 
        (link_tag.get("href")[-4:] == ".css") or
        (link_tag.get("type") == "text/css"))