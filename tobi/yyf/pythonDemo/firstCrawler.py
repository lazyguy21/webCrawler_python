from urllib.request import urlopen
from bs4 import BeautifulSoup

__author__ = 'ye'
html = urlopen("http://mz.youmtu.com")
bsObj=BeautifulSoup(html)
images = bsObj.findAll("img")
print(type(images))
for image in images:
    print(image['alt'],image["src"])
    file_io = open('../'+image['alt'], 'wb')
    tryNum=3
    while(tryNum>0):
        try:
            tryNum-=tryNum
            imgObj = urlopen(image['src'],None,3)
            break
        except:
            if tryNum==1:
                print('该url重试3次后失败：',image['alt'],image["src"])
    file_io.write(imgObj.read())
    file_io.close()





