# url_util
# Url operations and formating utilities

def chari(s, char):
    '''Returns indexes where char was found in text'''
    if s == "" or char == "":
        return[]
    a = []
    for i, c in enumerate(s):
        if c == char:
            a.append(i)
    return a

def stri(text, pattern, end = False):
    '''Returns indexes where passed pattern was found in text. If end == True, 
    returns found index + 1 after each occurence'''
    if pattern == "" or text == "":
        return []
    ret = []
    pat_i = 0 # index of current char in pattern
    for i, c in enumerate(text):
        if c == pattern[pat_i]:
            pat_i += 1
            if pat_i == len(pattern):
                if end:
                    ret.append(i + 1)
                else:
                    ret.append(i - len(pattern) + 1)
                pat_i = 0
        else:
            pat_i = 0
    return ret

def find_next(text, char, escape = None):
    '''Returns first index where char is found in text while escaping chars 
    passed in escape. Returns -1 if none found'''
    if text == "" or char == "":
        return -1
    if isinstance(escape, str):
        escape = [escape]

    escape_next = False
    for i, c in enumerate(text):
        if escape_next:
            escape_next = False
            continue
        elif escape and c in escape:
            escape_next = True
            continue
        if c == char:
            return i
        
    return -1

def goup(url):
    '''Goes up a single dir in given link and returns it'''
    try:
        # Remove trailing slash
        rem = False
        if url[-1] == "/":
            rem = True
            url = url[:-1]
        slash_indexes = chari(url, "/")
        # If protocol specified
        if url.find("://") != -1:
            # If top level
            if len(slash_indexes) == 2:
                if rem:
                    url += "/"
                return url
            else: 
                # return everything up to and including last slash
                return url[:slash_indexes[-1] + 1]
        else:
            # If top level
            if len(slash_indexes) == 0:
                if rem:
                    url += "/"
                return url
            else:
                # return everything up to and including last slash
                return url[:slash_indexes[-1] + 1]
    except ValueError:
        return url

def get_origin_url(url):
    '''Goes up a dir in passed url until it reaches origin'''
    new_url = url[:]
    up_url = goup(new_url)
    while new_url != up_url:
        new_url = up_url
        up_url = goup(up_url)
    return up_url

def is_url(url):
    try:
        return url[:4] == "http"
    except:
        return False

def is_url_file(url):
    '''Checks if url points to a file'''
    try:
        ls = url.index("/")
        rs = url.rindex("/")
        return (rs < url.rindex(".") and (rs - ls > 1 or rs == ls))
    except ValueError:
        ls = 0
        rs = 0
        return (rs < url.rindex(".") and (rs - ls > 1 or rs == ls))

def is_url_fragment(url):
    '''Checks if url has a fragment/anchor'''
    try:
        return url.rindex("/") < url.index("#")
    except ValueError:
        return False

def get_resource_url(res_tag, attr_name, origin_url):
    '''Gets resource url from passed attr of passed tag. If passed attr is not 
    found, searches for urls that point to files and returns the first one.'''
    src = res_tag.get(attr_name)
    # If already has src
    if src != None:
        if is_url(src):
            return src
        elif is_url_file(src):
            if src[0] == "/" and origin_url[-1] == "/":
                src = src[1:]
            return origin_url + src
    else:
        # Scan for urls in attrs
        for k, v in res_tag.attrs.items():
            if is_url(v):
                return v
            elif is_url_file(v):
                if v[0] == "/" and origin_url[-1] == "/":
                    v = v[1:]
                return origin_url + v

def remove_url_file(url):
    '''Returns url with its pointed file removed'''
    try:
        if is_url_file(url):
            return url[:url.rindex("/") + 1]
        else:
            return url
    except ValueError:
        return url

def remove_url_fragment(url):
    '''Removes all fragments/anchors from url and returns final url'''
    try:
        i = url.index("#")
        return url[:i]
    except ValueError:
        return url

def remove_leading_strings(url, strings_to_remove):
    '''Removes leading string from url out of given strings and returns url'''
    ret = url[:]
    if isinstance(strings_to_remove, str):
        strings_to_remove = [strings_to_remove]
    for s in strings_to_remove:    
        if ret[:len(s)] == s:
                ret = ret[len(s):]
                break
    return ret

def shorten_url(url, max_length = 47):
    if max_length < 1:
        max_length = 1
    l = len(url)
    if l > max_length:
        char_count = max_length//2
        ret = url[:char_count] + "..." + url[-char_count:]
        return ret
    else:
        return url
