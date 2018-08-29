from bs4 import BeautifulSoup
import sys
import io
import re #regex

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

fp = open("cars.html", encoding="utf-8")
soup = BeautifulSoup(fp, "html.parser")


def car_func(selctor):
    print("car_func", soup.select_one(selctor).string)


car_func("#gr")
car_func("li#gr")
car_func("ul > li#gr")
car_func("#cars #gr")
car_func("#cars > #gr")
car_func("li[id='gr']")

print(soup.select("li")[3].string)
print(soup.find_all("li")[3].string)

# 람다식
car_lamda = lambda q : print("car_lamda", soup.select_one(q).string)
car_lamda("#gr")
car_lamda("li#gr")
car_lamda("ul > li#gr")
car_lamda("#cars #gr")
car_lamda("#cars > #gr")
car_lamda("li[id='gr']")
