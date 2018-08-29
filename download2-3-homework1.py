import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

imgUrl = "https://ssl.pstatic.net/tveta/libs/1205/1205127/e9b14088d045f22259b8_20180817164222010.jpg"
AviUrl = "https://tvetamovie.pstatic.net/libs/1208/1208373/e6c452e2a60cea624ca3_20180816184632894.mp4-pBASE-v0-f62522-20180816184947484.mp4"

savePath1 = "D:/Study/파이썬 입문 및 웹 크롤링을 활용한 다양한 자동화 어플리케이션 제작하기/section2/homwork1.jpg"
savePath2 = "D:/Study/파이썬 입문 및 웹 크롤링을 활용한 다양한 자동화 어플리케이션 제작하기/section2/homwork2.mp4"

f1 = dw.urlopen(imgUrl).read()
f2 = dw.urlopen(AviUrl).read()

with open(savePath1, 'wb') as saveFile1:
    saveFile1.write(f1)

with open(savePath2, 'wb') as saveFile2:
    saveFile2.write(f2)


print('다운로드 완료!')
