import unittest
from bs4 import BeautifulSoup
from url_util.url_util import (chari, stri, find_next, goup, get_origin_url, 
    is_url_file, is_url_fragment, remove_url_file, remove_url_fragment,
    remove_leading_strings, get_resource_url, is_url, shorten_url)

class TestUrlUtil(unittest.TestCase):

    def test_chari(self):
        testeq = self.assertEqual
        testeq(chari("Lorem", "L"), [0])
        testeq(chari("Lorem Ipsum", "l"), [])
        testeq(chari("Lorem Ipsum", "m"), [4, 10])
        testeq(chari("", "Lorem Ipsum"), [])
        testeq(chari("", ""), [])
        testeq(chari("Hi", ""), [])

    def test_stri(self):
        testeq = self.assertEqual
        testeq(stri("Lorem Ipsum", "L"), chari("Lorem Ipsum", "L"))
        testeq(stri("Lorem Ipsum", "m"), chari("Lorem Ipsum", "m"))
        testeq(stri("", "Lorem Ipsum"), [])
        testeq(stri("", ""), [])
        testeq(stri("Hi", ""), [])
        testeq(stri("Lorem Ipsum", "sum"), [8])
        testeq(stri("Lorem Ipsum", "sum", True), [11])
        testeq(stri("Lorem Ipsum Lorem Ipsum", "sum"), [8, 20])
        testeq(stri("Lorem Ipsum Lorem Ipsum", "sum", True), [11, 23])
        testeq(stri("NaNaNaNaaaa, Batmaaan!", "Na", True), [2, 4, 6, 8])

    def test_find_next(self):
        testeq = self.assertEqual
        testeq(find_next("Lorem", "o"), 1)
        testeq(find_next("Lorem", "a"), -1)
        testeq(find_next("Lorem Ipsum", "m"), 4)
        testeq(find_next("Lorem Ipsum", "m", "e"), 10)
        testeq(find_next("Lorem Ipsum", "m", ["e"]), 10)
        testeq(find_next("Lorem Ipsum", "m", ["e", "u"]), -1)
        testeq(find_next("Lorem Ipsumm", "m", ["e", "u"]), 11)
        testeq(find_next("Loreem Ipsumm", "m", ["e", "u"]), 5)
        testeq(find_next("Loreem", "e", "e"), -1)
        testeq(find_next("", "Lorem Ipsum"), -1)
        testeq(find_next("", ""), -1)
        testeq(find_next("Hi", ""), -1)

    def test_goup(self):
        testeq = self.assertEqual
        testeq(goup("https://slami.ge/"), "https://slami.ge/")
        testeq(goup("www.google.com/gmail"), "www.google.com/")
        testeq(goup("https://lua.org/docs.html"), "https://lua.org/")
        testeq(goup("lua.org/end/docs.html"), "lua.org/end/")
        testeq(goup("https://http.cat"), "https://http.cat")
        testeq(goup("http://a.ge"), "http://a.ge")
        testeq(goup("http://a.ge/"), "http://a.ge/")
        testeq(goup("http://a.ge/b"), "http://a.ge/")
        testeq(goup("http://a.ge/b/"), "http://a.ge/")
        testeq(goup(goup("a.co/b/c/d")), "a.co/b/")
        testeq(goup(goup("http://a.ge/b/c/d")), "http://a.ge/b/")
        testeq(goup(goup(goup("http://a.ge/b/c/d"))), "http://a.ge/")
        testeq(goup(goup(goup(goup("http://a.ge/b/c/d")))), "http://a.ge/")

    def test_get_origin_url(self):
        testeq = self.assertEqual
        testeq(get_origin_url("https://slami.ge/"), "https://slami.ge/")
        testeq(get_origin_url("www.google.com/gmail"), "www.google.com/")
        testeq(get_origin_url("https://lua.org/docs.html"), "https://lua.org/")
        testeq(get_origin_url("lua.org/end/docs.html"), "lua.org/")
        testeq(get_origin_url("https://http.cat"), "https://http.cat")
        testeq(get_origin_url("http://a.ge/b/c/d"), "http://a.ge/")

    def test_is_url(self):
        testeq = self.assertEqual
        testeq(is_url("https://slami.ge/"), True)
        testeq(is_url(""), False)
        testeq(is_url("Hello"), False)
        testeq(is_url("https://lua.org/end/docs.html"), True)
        testeq(is_url("lua.org/docs.html"), False)

    def test_is_url_file(self):
        testeq = self.assertEqual
        testeq(is_url_file("https://slami.ge/"), False)
        testeq(is_url_file("www.google.com/gmail"), False)
        testeq(is_url_file("https://lua.org/docs.html"), True)
        testeq(is_url_file("https://lua.org/end/docs.html"), True)
        testeq(is_url_file("lua.org/docs.html"), True)
        testeq(is_url_file("https://http.cat"), False)
        testeq(is_url_file("egg.js"), True)

    def test_is_url_fragment(self):
        testeq = self.assertEqual
        testeq(is_url_fragment("https://slami.ge/"), False)
        testeq(is_url_fragment("google.com"), False)
        testeq(is_url_fragment("www.lua.org/docs.html"), False)
        testeq(is_url_fragment("http://wikipedia.org/wiki/May_9#Events"), True)

    def test_get_resource_url(self):
        testeq = self.assertEqual
        origin_url = "http://images.com/"
        res_url = "http://images.com/cat.png"
        tag = BeautifulSoup(f"<img src=\"{res_url}\"></img>", "html5lib").img
        testeq(get_resource_url(tag, "src", origin_url), res_url)
        testeq(get_resource_url(tag, "href", origin_url), res_url)

        origin_url = "http://images.com/"
        res_url = "images/cat.png"
        tag = BeautifulSoup(f"<img src=\"{res_url}\"></img>", "html5lib").img
        testeq(get_resource_url(tag, "src", origin_url), origin_url + res_url)
        testeq(get_resource_url(tag, "href", origin_url), origin_url + res_url)
        res_url = "http://bing.com/images/cat.png"
        tag = BeautifulSoup(f"<img src=\"{res_url}\"></img>", "html5lib").img
        testeq(get_resource_url(tag, "src", origin_url), res_url)
        testeq(get_resource_url(tag, "href", origin_url), res_url)

    def test_remove_url_fragment(self):
        testeq = self.assertEqual
        testeq(remove_url_fragment("https://slami.ge/"), "https://slami.ge/")
        testeq(remove_url_fragment("google.com/"), "google.com/")
        testeq(remove_url_fragment("lua.org/docs.html"), "lua.org/docs.html")
        testeq(remove_url_fragment("https://wikipedia.org/wiki/May_9#Events"), 
            "https://wikipedia.org/wiki/May_9")
        testeq(remove_url_fragment("https://a.bc.co"), "https://a.bc.co")
    
    def test_remove_url_file(self):
        testeq = self.assertEqual
        testeq(remove_url_file("https://http.cat/"), "https://http.cat/")
        testeq(remove_url_file("http://http.cat/404.jpg"), "http://http.cat/")
        testeq(remove_url_file("lua.org/docs.html"), "lua.org/")
        testeq(remove_url_file("google.com/#"), "google.com/#")
        testeq(remove_url_file("https://a.bc.co"), "https://a.bc.co")
    
    def test_remove_leading_strings(self):
        testeq = self.assertEqual
        rem = ["/", "../", "\\"]
        testeq(remove_leading_strings("/cat.png", rem), "cat.png")
        testeq(remove_leading_strings("../cat.png", rem), "cat.png")
        testeq(remove_leading_strings("//cat.png", rem), "/cat.png")
        testeq(remove_leading_strings("/cat.png", "/"), "cat.png")
        testeq(remove_leading_strings("\\docs\\img", rem), "docs\\img")
        testeq(remove_leading_strings("../docs/img", rem), "docs/img")
        testeq(remove_leading_strings("/images", ""), "/images")
        testeq(remove_leading_strings("", "/"), "")
    
    def test_shorten_url(self):
        testeq = self.assertEqual
        testeq(shorten_url("abcdef", 4), "ab...ef")
        testeq(shorten_url("abcdef", 6), "abcdef")
        testeq(shorten_url("abcdefghijklmn", 4), "ab...mn")
        testeq(shorten_url("abcdefghijklmn", 7), "abc...lmn")
        testeq(shorten_url(""), "")
        testeq(shorten_url("", 0), "")

if __name__ == "__main__":
    unittest.main()
