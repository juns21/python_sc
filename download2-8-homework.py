from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io
import os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

opener = req.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
req.install_opener(opener)

# HTML 가져오기
base = "https://www.inflearn.com/"
quote = rep.quote_plus("추천-강좌")
url = base + quote

res = req.urlopen(url)

savePath = "D:\\Study\\파이썬 입문 및 웹 크롤링을 활용한 다양한 자동화 어플리케이션 제작하기\\homework\\"

try:
    if not(os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더 만들기 실패!")
        raise

soup = BeautifulSoup(res, "html.parser")
img_list = soup.select("ul.slides > li")
#print("img_list", img_list)

j = 1
for i, e in enumerate(img_list, 1):
    if(i >= 13):
        #print(i, ", ", e.select_one("h4.block_title > a").string)
        with open(savePath+"text_"+str(j)+".txt", "wt") as f:
            f.write(e.select_one("h4.block_title > a").string)

        fullFileNmae = os.path.join(savePath, savePath+str(j)+".png")
        req.urlretrieve(e.select_one("div.block_media > a > img")['src'], fullFileNmae)
        j += 1

print("다운로드 완료!")
