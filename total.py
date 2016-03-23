#coding:utf-8
from bs4 import BeautifulSoup
import requests
import time
import datetime
import re


def sh_volume():
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
    #print ("%f sec" % duration)

    if searchObj:
        volume_yi = int(float(searchObj.group(1)))
        print u"SH total volume(亿元):", volume_yi
        return volume_yi

def sz_volume():
    # 深交所
    url="http://www.szse.cn/main/marketdata/tjsj/jbzb/"

    wb_data=requests.get(url)
    wb_data.encoding='gb2312'
    soup=BeautifulSoup(wb_data.text,'lxml')
    # beautifulSoap 使用 unicode 编码
    # 股票总市值（元）
    anchor_tag =  soup.find('td', text=re.compile(u'股票总市值'))  # 所以中文前要加u,表示unicode编码 # find('td')找到标签 #find(text=) 找到text only
    #print anchor_tag.text
    volume = anchor_tag.next_sibling.text.replace(',','')
    volume_yi = int(float(volume)/100000000)
    print "SZ total volume(亿元):" , volume_yi
    return volume_yi


shsz = sh_volume()+sz_volume()
print datetime.date.today(), "沪深两市总市值(亿元):",shsz

# 2015年GDP
gdp2015 = 676708
growth_rate = 0.069
today_day = int(datetime.date.today().strftime('%j'))
gdp_today = (gdp2015*growth_rate*today_day/365) + gdp2015
print "今日GDP估算(亿元):",gdp_today
percent = shsz / gdp_today
print "A股总市值占GDP比重: ", format(percent, '.2%')
