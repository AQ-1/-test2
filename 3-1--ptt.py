# encoding=utf-8

''' requests發出get請求範例 '''
import requests as req
url='https://www.pttweb.cc/hot/news/today'
res=req.get(url)
res.encoding = 'utf-8'
print(res.text)
print(res.status_code)


''' find(name)，抓取<a> '''
import requests as req
url='https://www.pttweb.cc/hot/news/today'
res=req.get(url)
res.encoding = 'utf-8'
from bs4 import BeautifulSoup
soup=BeautifulSoup(res.text, 'html.parser')
a_tag=soup.find(name='a')
print(a_tag)


''' find(name)，先找到<div>再找該<div>的<h1> '''
import requests as req
url='https://www.pttweb.cc/hot/news/today'
res=req.get(url)
res.encoding = 'utf-8'
from bs4 import BeautifulSoup
soup=BeautifulSoup(res.text, 'html.parser')
div_tag=soup.find(name='div')
h1_tag=div_tag.find(name='h1')
print(h1_tag)


''' find(name)，清單，找到符合清單中標籤名稱的第一個 '''
import requests as req
url='https://www.pttweb.cc/hot/news/today'
res=req.get(url)
res.encoding = 'utf-8'
from bs4 import BeautifulSoup
soup=BeautifulSoup(res.text, 'html.parser')
h3_or_span=soup.find(name=['h3', 'span'])
print(h3_or_span)


''' find(name)，使用正規表示法，找出有包含r字元的標籤名稱 '''
import requests as req
url='https://www.pttweb.cc/hot/news/today'
res=req.get(url)
res.encoding = 'utf-8'
from bs4 import BeautifulSoup
soup=BeautifulSoup(res.text, 'html.parser')
import re
include_r=soup.find(name=re.compile('.*r.*'))
print(include_r)


''' find(name)，以自訂規則擷取標籤 '''
def custom_filter(tag):
    try:
        tag['class'].index('e7-recommendScore')
        return tag.name=='div' and int(tag.text[3:])<0
    except:
        return False
import requests as req

url='https://www.pttweb.cc/hot/news/today'
res=req.get(url)
res.encoding = 'utf-8'
from bs4 import BeautifulSoup
soup=BeautifulSoup(res.text, 'html.parser')
cus_filter_tag=soup.find(name=custom_filter)
print(cus_filter_tag)

#取得標籤名稱
print(cus_filter_tag.name)
#取得標籤的所有屬性
print(cus_filter_tag.attrs)
#依據屬性取得值
print(cus_filter_tag.get('class') )
#檢查有無該屬性，回傳boolean
print(cus_filter_tag.has_attr('class'))
#新增、刪除、修改
cus_filter_tag['class']='classA'
cus_filter_tag.name='btag'
print(cus_filter_tag)
del cus_filter_tag['class']
print(cus_filter_tag)


''' find(name, attrs)，找出第一個<div>中class屬性值為e7-recommendScore的<div> '''
import requests as req
url='https://www.pttweb.cc/hot/news/today'
res=req.get(url)
res.encoding = 'utf-8'
from bs4 import BeautifulSoup
soup=BeautifulSoup(res.text, 'html.parser')
the_tag=soup.find(name='div', attrs={'class': 'e7-recommendScore'})
print(the_tag)


''' find(name, recursive=False)，只找下一層的<tr> '''
import requests as req
url='https://www.pttweb.cc/hot/news/today'
res=req.get(url)
res.encoding = 'utf-8'
from bs4 import BeautifulSoup
soup=BeautifulSoup(res.text, 'html.parser')
table_tag=soup.find(name='h1', recursive=False)
print('recursive=False:\n', table_tag)
table_tag=soup.find(name='h1')
print('recursive=True:\n', table_tag)


''' find(name, string)，內容為Gossiping的<span> '''
import requests as req
url='https://www.pttweb.cc/hot/news/today'
res=req.get(url)
res.encoding = 'utf-8'
from bs4 import BeautifulSoup
soup=BeautifulSoup(res.text, 'html.parser')
the_span=soup.find(name='span', string='Gossiping')
print(the_span)


''' find_all limit'''
def custom_filter(tag):
    try:
        tag['class'].index('e7-recommendScore')
        return tag.name=='div' and int(tag.text[3:])<0
    except:
        return False
import requests as req
url='https://www.pttweb.cc/hot/news/today'
res=req.get(url)
res.encoding = 'utf-8'
from bs4 import BeautifulSoup
soup=BeautifulSoup(res.text, 'html.parser')
cus_filter_tag=soup.find_all(name=custom_filter, limit=3)
for tag in cus_filter_tag:
    print(tag, end='\n\n')


''' findChildren '''
import requests as req
url='https://www.pttweb.cc/hot/news/today'
res=req.get(url)
res.encoding = 'utf-8'
from bs4 import BeautifulSoup
soup=BeautifulSoup(res.text, 'html.parser')
container=soup.find_all(name='div', attrs={'class': 'mt-4'})
for i in container[1].findChildren(recursive=False):
    print(i.name, i.text, end='\n\n')
    

''' findParents '''
import requests as req
url='https://www.pttweb.cc/hot/news/today'
res=req.get(url)
res.encoding = 'utf-8'
from bs4 import BeautifulSoup
soup=BeautifulSoup(res.text, 'html.parser')
tag=soup.find(name='h1')
parents=tag.findParents()
for i in parents:
    print(i.name)


''' findNextSibling '''
import requests as req
url='https://www.pttweb.cc/hot/news/today'
res=req.get(url)
res.encoding = 'utf-8'
from bs4 import BeautifulSoup
soup=BeautifulSoup(res.text, 'html.parser')
container=soup.find_all(name='div', attrs={'class': 'mt-4'})
container=container[1].findChildren(recursive=False)
print(container[0].text)
print(container[0].findNextSibling().text)

