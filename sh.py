#coding:gb2312
from bs4 import BeautifulSoup
import requests
import time
import re

#上交所
url = "http://www.sse.com.cn/market/stockdata/overview/day/"

wb_data=requests.get(url)
wb_data.encoding='utf8'
text = wb_data.text
# 总市值行格式： 	var marketValue = '249234.14';
searchObj = re.search(r'marketValue = \'(\d+\.\d+)\';', text)
if searchObj:
   print "SH total volume: ", searchObj.group(1)

# 另外的方法是先分行: text.split,再正则匹配,可能效率会高一点
