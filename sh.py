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
start_time = time.clock()
# 总市值行格式： 	var marketValue = '249234.14';
# 市价总值(亿元)
searchObj = re.search(r'marketValue = \'(\d+\.\d+)\';', text)

end_time = time.clock()
duration = end_time - start_time
print ("%f sec" % duration)

if searchObj:
   volume_yi = int(float(searchObj.group(1)))
   print u"SH total volume(亿元): ", volume_yi

