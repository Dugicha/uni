from urllib.request import Request, urlopen

g_images_link = "https://www.google.com/search?biw=1280&bih=893&tbm=isch&sa=1&ei=2B08WqW5IK_b6QSFrZiIDg&q=bee&oq=bee&gs_l=psy-ab.3..0i67k1j0j0i67k1l2j0j0i67k1j0l4.46144.46383.0.46575.3.3.0.0.0.0.143.255.0j2.2.0....0...1c.1.64.psy-ab..1.2.254....0.HUusY9oBoAc"

req = Request(g_images_link, headers={"User-Agent": "Mozilla/5.0"})
html = urlopen(req)

f = open("ans.txt", "w")
f.write(str(html.read()))
f.close()

print(html.read())
