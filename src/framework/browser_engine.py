# -*- coding:utf-8 -*-
import configparser
import sys,os
from asyncio.log import logger
from selenium import webdriver
class Browser():
    
    def open_Browser(self):
        config = configparser.ConfigParser()
        dir = os.path.abspath('.').split('src')[0]   #os.path.abspath：获取当前模块的绝对路径
        config.read(dir+"config\\config.ini")
        browser = config.get("browserType","browserName")
        logger.info("you have select "+browser+" browser." )
        url = config.get("testServer","URL")
        print(url)
        if browser == "Chrome":
            self.driver = webdriver.Chrome()
        elif browser == "Firefox" :
            self.driver = webdriver.Firefox()
        elif browser == "IE":
            self.driver = webdriver.Ie()
        #self.open_browser(browser)
        self.driver.get(url)  #跳转到指定页面
        return self.driver

# if __name__ =='__main__':
#     b = Browser()
#     b.open_Browser()
    
    
    
    
    
    
    
      
        