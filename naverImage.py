from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io
import os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#bring HTML
base = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
quote = rep.quote_plus("아이유")
url = base + quote

res = req.urlopen(url)
savePath = "/Users/jahoy/Documents/imagedown/"

try:
    if not(os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    if e.errno != errno.EEXIST: # 파일이 존재 하지 않으면
        print("Failed to create directory!!!!!")
        raise

soup = BeautifulSoup(res, "lxml")

li_list = soup.select("div.img_area._item > a.thumb._thumb > img")
for i, div in enumerate(li_list,1):
    fullfilename = os.path.join(savePath, savePath+str(i)+'.jpg') 
    req.urlretrieve(div['data-source'], fullfilename) #url의 소스를 파일로 저장

print("Download Complete")
