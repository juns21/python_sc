import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl = "http://cafefiles.naver.net/20121020_201/rnldudnsdbsk_1350727997756Qh1sM_JPEG/%B5%BF%B9%B020.jpg"
htmlURL = "http://google.com"

savePath1 = "D:/Study/파이썬 입문 및 웹 크롤링을 활용한 다양한 자동화 어플리케이션 제작하기/section2/test.jpg"
savePath2 = "D:/Study/파이썬 입문 및 웹 크롤링을 활용한 다양한 자동화 어플리케이션 제작하기/section2/index.html"

dw.urlretrieve(imgUrl, savePath1)
dw.urlretrieve(htmlURL, savePath2)

print("다운로드 완료!")
