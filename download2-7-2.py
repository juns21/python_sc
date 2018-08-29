from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io
import re #regex

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://finance.naver.com/sise/"
res = req.urlopen(url).read().decode(req.urlopen(url).headers.get_content_charset())

soup = BeautifulSoup(res, "html.parser")
#print('soup', soup.prettify())

top10 = soup.select("table#siselist_tab_0 > tr")
#print('top10', top10)

i = 1;
for e in top10:
    if e.find("a") is not None:
        print(i, e.select_one(".tltle").string, ": ", e.select("td")[4].string)
        i += 1
