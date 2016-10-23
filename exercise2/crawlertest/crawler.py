import re
import requests
from urllib.parse import urljoin

link = "http://ktmt.github.io/blog/archives/"
req = requests.get(link)
listUrl = re.findall(r'href="(.*?)"', req.content.decode(), re.M|re.I)
urls = []

for i in listUrl:
    u = urljoin(link, i)
    if u.find("ktmt.github.io/blog/") != -1 and u.find(link[0:-1]) == -1 and u.find("disqus_thread") == -1:
        urls.append(u)

for u in urls:
    if u.rfind("/") == len(u) - 1:
        name_file = u[u.rfind("/", 0, len(u) - 1) + 1: -1]
    else:
        name_file = u[u.rfind("/") + 1: ]

    name_file = "/home/aqii/training/demo_crawl/" + name_file + ".html"

    req = requests.get(u)

    with open(name_file, "wt") as f:
        f.write(req.content.decode())
