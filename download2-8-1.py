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
base = "https://search.naver.com/search.naver?where=image&query="
quote = rep.quote_plus("아이유")
url = base + quote

res = req.urlopen(url)

savePath = "D:\\Study\\파이썬 입문 및 웹 크롤링을 활용한 다양한 자동화 어플리케이션 제작하기\\imagedown\\"

try:
    if not (os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더 만들기 실패!")
        raise

soup = BeautifulSoup(res, "html.parser")
img_list = soup.select("div.img_area > a.thumb._thumb > img")
#print('img_list', img_list)


for i, img_list in enumerate(img_list, 1):
    #print(img_list['data-source'])
    fullFileNmae = os.path.join(savePath, "imagedown"+str(i+50)+".jpg")
    req.urlretrieve(img_list['data-source'], fullFileNmae)

print("다운로드 완료!")
