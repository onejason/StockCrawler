#coding:gb2312
from bs4 import BeautifulSoup
import requests
import time
import re

#�Ͻ���
url = "http://www.sse.com.cn/market/stockdata/overview/day/"

wb_data=requests.get(url)
wb_data.encoding='utf8'
soup=BeautifulSoup(wb_data.text,'lxml')

# ����ֵ�У� 	var marketValue = '249234.14';
text = wb_data.text
resultList = re.findall('marketValue =',text)
print resultList
# beautifulSoap ʹ�� unicode ����
#anchor_tag =  soup.find('td', text=re.compile(u'�м���ֵ'))  # ��������ǰҪ��u,��ʾunicode���� # find('td')�ҵ���ǩ #find(text=) �ҵ�text only
#print anchor_tag
#volume = anchor_tag.next_sibling.text.replace(',','')
#print volume
