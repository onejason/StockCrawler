#coding:utf-8
# http://www.361way.com/python-stock-tushare/4579.html
# http://tushare.org

import tushare as ts

#print ts.get_hist_data('600848') #一次性获取全部日k线数据


print ts.get_stock_basics()

