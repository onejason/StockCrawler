#coding:gb2312
from bs4 import BeautifulSoup
import requests
import time
import re

# ���
url="http://www.szse.cn/main/marketdata/tjsj/jbzb/"

wb_data=requests.get(url)
wb_data.encoding='gb2312'
soup=BeautifulSoup(wb_data.text,'lxml')
# beautifulSoap ʹ�� unicode ����
anchor_tag =  soup.find('td', text=re.compile(u'��Ʊ����ֵ'))  # ��������ǰҪ��u,��ʾunicode���� # find('td')�ҵ���ǩ #find(text=) �ҵ�text only
print anchor_tag
volume = anchor_tag.next_sibling.text.replace(',','')
print volume


