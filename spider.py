#!/usr/bin/env python
import requests
import re
import urlparse


target_url = "http://192.168.29.97/mutillidae/favicon.ico"
target_links = []
def extract_link_from(url):
    request = requests.get(url)
    return re.findall('(?:href=")(.*?)"',request.content)
def crawler(url):
    href_links = extract_link_from(url)
    for link in href_links:
        link = urlparse.urljoin(url,link)
        if "#" in link:
             link = link.split("#")[0]

        if url in link and link not in target_links :
            target_links.append(link)
            print(link)
            crawler(link)


crawler(target_url)