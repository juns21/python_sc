from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io
import re #regex

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "http://finance.daum.net/index.daum?nil_profile=stockgnb&nil_menu=stock_top"
res = req.urlopen(url).read()

soup = BeautifulSoup(res, "html.parser")
#print('soup', soup.prettify())

top = soup.select("ul#topMyListNo1 > li")
#print(top)

for i,e in enumerate(top, 1):
    #print('e>>>', type(e))
    #print('e>>>', e.find('a').string)
    print(i, ",", e.find('a').string, " : ", e.find('span').string)
