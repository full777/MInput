# -*- coding:utf-8 -*-
'''
Created on 2019��2��28��

@author: t_ful
'''
import unittest
from pageobject.newEnterPPage import NewEnterPPage
from framework.basepage import BasePage
from framework.browser_engine import Browser
from framework.logger import Logger
from framework.readExcle import ReadExcle
import os
logger = Logger('loginTest页面').getlog()
class NewEnterPTest(unittest.TestCase):
    sheet_dir = os.path.abspath('.').split('src')[0]+'data\\data.xlsx'
    element,list = ReadExcle(sheet_dir).get_Value('newPage')
    #每条case执行的前置条件
    def setUp(self):
        browser = Browser().open_Browser()
        self.bpage = BasePage(browser)
        self.lpage = NewEnterPPage(self.bpage)
    #每条case执行的后置条件   
    def tearDown(self):   
        self.bpage.quit_browser()
    #注册企业成功
    def test_loginSucess(self):
        up_file0 = "D:\\Java\\file\\1.jpg"          
        result = self.lpage.new_enterP(0, '云尖端科技', 'AFC', up_file0,'杨光', up_file0, 
            '2017-01-02', '2017-01-02', 0, '四川省', '008613458923958', 'AFC12', up_file0,
             '云端尖', '私有', '2017-01-02', '2017-01-02', up_file0, up_file0, '李琳',
              '511345200012091146', up_file0, up_file0, up_file0, up_file0, '四川省', 
              0, '汉族', '1990-09-09', '深圳签证办', '2017-02-1', '2117-02-1', '008613458923958',
               '重庆市', '杨丽', '008613458923959')
        print(result)
        self.assertIn("企业注册成功" in result)
#         
#     # 注册企业失败，企业名缺少
#     def test_loginFail_1(self):
        up_file0 = "D:\\Java\\file\\1.jpg"          
        result = self.lpage.new_enterP(0, '', 'AFC', up_file0,'杨光', up_file0, 
            '2017-01-02', '2017-01-02', 0, '四川省', '008613458923958', 'AFC12', up_file0,
             '云端尖', '私有', '2017-01-02', '2017-01-02', up_file0, up_file0, '李琳',
              '511345200012091146', up_file0, up_file0, up_file0, up_file0, '四川省', 
              0, '汉族', '1990-09-09', '深圳签证办', '2017-02-1', '2117-02-1', '008613458923958',
               '重庆市', '杨丽', '008613458923959')
        print(result)
        self.assertIn("企业注册失败" in result)
#     
#  
 
 
     

if __name__ == "__main__":
    unittest.main() # 使用main()直接运行时，将按case的名称顺序执行
    