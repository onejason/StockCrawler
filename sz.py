#coding:gb2312
from bs4 import BeautifulSoup
import requests
import time
import re

# 深交所
url="http://www.szse.cn/main/marketdata/tjsj/jbzb/"

wb_data=requests.get(url)
wb_data.encoding='gb2312'
soup=BeautifulSoup(wb_data.text,'lxml')
# beautifulSoap 使用 unicode 编码
anchor_tag =  soup.find('td', text=re.compile(u'股票总市值'))  # 所以中文前要加u,表示unicode编码 # find('td')找到标签 #find(text=) 找到text only
print anchor_tag
volume = anchor_tag.next_sibling.text.replace(',','')
print volume


