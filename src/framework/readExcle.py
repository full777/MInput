# -*- coding:utf-8 -*-
'''
Created on 2019年2月20日

@author: t_ful
'''
import xlrd
class ReadExcle(object):
    def __init__(self,file,tag='True'):
        self.file = file;
        self.tag = tag;
    '''
    返回某个sheet页中所有的值
    '''   
    def read(self,sheetname,n=1,m=100):
        excelFile = xlrd.open_workbook(self.file)
        table = excelFile.sheet_by_name(sheetname)
        nrows = table.nrows
        ncols = table.ncols
#         print(nrows)
        i = 0
        for row in range(1,nrows):
            i+=1
            line = []
            if self.tag =='True':
                for col in range(0,ncols):
                    line.append(table.cell(row,col).value)
#                     print(table.cell(row,col).value)              
            elif self.tag == 'False':
                if i >= n and i < n + m :
                    for col in range(0,ncols):
                        line.append(table.cell(row,col).value)
        
    '''
    返回excel中某一具体单元格内的值
    '''
    def read_One(self,sheetname,n,m):
        excelFile = xlrd.open_workbook(self.file)
        table = excelFile.sheet_by_name(sheetname)
        print(table.name,table.nrows,table.ncols)
        return table.cell(n,m).value
       
    '''获取sheet页里的页面元素表'''
    def get_Value(self,sheetname):
        excelFile = xlrd.open_workbook(self.file)
        sheet = excelFile.sheet_by_name(sheetname)
        nrows = sheet.nrows
        print(nrows)
        list0 = [] #元素名称列表
        list1 = [] #元素定位列表
        list2 = [] #当元素定位为空时，js列表
        for i in range(1,nrows):
            list0.append(sheet.cell(i,0).value)
            r0 = sheet.cell(i,2).value
            r1 = sheet.cell(i,3).value
            if r0 != 'NULL' :
                list1.append(r0 +'=>'+ r1)
                dict1 = dict(zip(list0,list1))
            else:
                list2.append(r1)
        return dict1,list2
    
                           
# if __name__ == '__main__':
#     sheet_dir = os.path.abspath('.').split('src')[0] + 'PageElements\\'
#     file = sheet_dir + 'elements.xlsx'
#     print(file)
#     file = ReadExcle(file)
# #     print(file.read_One('login',2,3))
# #     file.read('login')  
#     print(file.get_Value('login'))
#                 
                    
                