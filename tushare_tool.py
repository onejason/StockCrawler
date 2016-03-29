#coding:utf-8
# http://www.361way.com/python-stock-tushare/4579.html
# http://tushare.org


import tushare as ts

df = ts.get_stock_basics()
# get_stock_basics()并不能得到指数信息
#print df.head(5)

#print df.ix['000001']
#print df.ix['sh']

print ts.get_hist_data('hs300',start='2015-01-05',end='2015-01-09')