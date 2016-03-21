import requests

url = "http://www.sse.com.cn/market/stockdata/overview/day/"
r = requests.get(url)
r.encoding = 'utf8'
wb_data = r.text
print (wb_data)