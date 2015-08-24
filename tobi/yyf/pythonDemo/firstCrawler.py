import re
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

__author__ = 'ye'


def tryOpenURL(src_):
    tryNum = 3
    while (tryNum > 0):
        try:
            tryNum -= 1
            req = Request(src_, headers={'User-Agent': "Magic Browser"})
            response = urlopen(req, None, 3)
            bytes =response.read()
            return bytes
        except Exception as e:
            if tryNum == 0:
                print(e, '该url重试3次后失败：',src_ )

def extractImageNameFromURL(urlStr):
    urlReverse = urlStr[::-1]
    match = re.match('[^/]+', urlReverse)
    if match:
        result = match.group()
    imageName = result[::-1]
    return imageName

def handleImageTagList(images):
    'BS4 Tag of Image'
    for image in images:
            imageName=''
            src_ = image.get("src")
            alt_ = image.get('alt')
            width_ = image.get('width')
            imgTypeBoolean = not src_.endswith('jpg') and not src_.endswith('gif') and not src_.endswith('png')
            if not src_ or  width_ or imgTypeBoolean or src_ in savedImgSet :
            #如果src为none，或者包含width（说明为小图片）或者不以3种格式结尾的图片 跳过
                continue
            else:
                imageName=extractImageNameFromURL(src_)
            try:
                bytes = tryOpenURL(src_)
                file_io = open('/home/ye/Pictures/test/' + imageName, 'wb')
                file_io.write(bytes)
                print('图片保存成功 : ',alt_,src_)
                file_io.close()
            finally:
                savedImgSet.add(src_)

def handleLink(url):
    if not url or url in searchedLink or not re.match(r"http://mz.youmtu.com", url) or url.endswith('.exe'):
        return
    bytes=tryOpenURL(url)
    bsObj=BeautifulSoup(bytes,"html5lib")
    images = bsObj.findAll("img")
    handleImageTagList(images)
    aLinks = bsObj.findAll("a")
    searchedLink.add(url)
    for aLink in aLinks:
        urlStr = aLink.get('href')
        handleLink(urlStr)

url= 'http://mz.youmtu.com'
# http://baozoumanhua.com
searchedLink=set()
savedImgSet=set()
handleLink(url)










