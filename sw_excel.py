import xlrd
data = xlrd.open_workbook('/Users/Jason/Downloads/801001_hq.xls')
#data = xlrd.open_workbook('/Users/Jason/Downloads/2.xls')



'''
# pyexcel-xls
from pyexcel_xls import XLBook
book = XLBook("/Users/Jason/Downloads/801001_hq.xls")
xls_data = dict(book.sheets())
print xls_data
'''