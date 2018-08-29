from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io
import re #regex

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://www.daum.net/"
res = req.urlopen(url).read()

soup = BeautifulSoup(res, "html.parser")
#print('soup', soup.prettify())

hotlist = soup.select("div.realtime_part > ol > li")
#print('hotlist', hotlist)

for i, e in enumerate(hotlist, 1):
    #print(e.find("a"))
    print(i, "위 ", e.find("a").string, ": ", e.find("a").attrs['href'])
