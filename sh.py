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
# ����ֵ�и�ʽ�� 	var marketValue = '249234.14';
searchObj = re.search(r'marketValue = \'(\d+\.\d+)\';', text)
if searchObj:
   print "SH total volume: ", searchObj.group(1)

# ����ķ������ȷ���: text.split,������ƥ��,����Ч�ʻ��һ��
