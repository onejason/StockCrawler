#coding:gb2312
from bs4 import BeautifulSoup
import requests
import time
import re

#上交所
url = "http://www.sse.com.cn/market/stockdata/overview/day/"

wb_data=requests.get(url)
wb_data.encoding='utf8'
soup=BeautifulSoup(wb_data.text,'lxml')

# 总市值行： 	var marketValue = '249234.14';
text = wb_data.text
resultList = re.findall('marketValue =',text)
print resultList
# beautifulSoap 使用 unicode 编码
#anchor_tag =  soup.find('td', text=re.compile(u'市价总值'))  # 所以中文前要加u,表示unicode编码 # find('td')找到标签 #find(text=) 找到text only
#print anchor_tag
#volume = anchor_tag.next_sibling.text.replace(',','')
#print volume
