import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

imgUrl = "http://cafefiles.naver.net/20121020_201/rnldudnsdbsk_1350727997756Qh1sM_JPEG/%B5%BF%B9%B020.jpg"
htmlURL = "http://google.com"

savePath1 = "D:/Study/파이썬 입문 및 웹 크롤링을 활용한 다양한 자동화 어플리케이션 제작하기/section2/test2.jpg"
savePath2 = "D:/Study/파이썬 입문 및 웹 크롤링을 활용한 다양한 자동화 어플리케이션 제작하기/section2/index2.html"


f = dw.urlopen(imgUrl).read()
f2 = dw.urlopen(htmlURL).read()

saveFile1 = open(savePath1, 'wb')     # w: write, r: read, a: add
saveFile1.write(f)
saveFile1.close()


with open(savePath2, 'wb') as saveFile2:
    saveFile2.write(f2)

print('다운로드 완료!')


#   urlopen:
#   변수 할당 -> 파싱 -> 저장(db....)
#
#   urlretrieve:
#   저장 -> open() -> 변수에 할당 -> 파싱 -> 저장
