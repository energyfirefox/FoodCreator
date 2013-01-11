#! /usr/bin/env python


import urllib2, re
from bs4 import BeautifulSoup

url = 'http://www.say7.info/cook/'
page = urllib2.urlopen(url)
soup = BeautifulSoup(page)

f = open('menu.html', 'w')
print >> f, "<meta charset='utf-8'>"
for link in soup.find_all(class_="desc"):
    receipt = link.find("a")    
    print >> f, receipt, "<br>"
    
f.close()
