#coding:gb2312
from bs4 import BeautifulSoup
import requests
import time
import re

#�Ͻ���
url = "http://www.sse.com.cn/market/stockdata/overview/day/"

wb_data=requests.get(url)
wb_data.encoding='utf8'
text = wb_data.text
start_time = time.clock()
# ����ֵ�и�ʽ�� 	var marketValue = '249234.14';
# �м���ֵ(��Ԫ)
searchObj = re.search(r'marketValue = \'(\d+\.\d+)\';', text)

end_time = time.clock()
duration = end_time - start_time
print ("%f sec" % duration)

if searchObj:
   volume_yi = int(float(searchObj.group(1)))
   print u"SH total volume(��Ԫ): ", volume_yi

