# -*- coding:utf-8 -*-
'''
Created on 2019年2月18日

@author: t_ful
'''

import os
from selenium.common.exceptions import NoSuchElementException
from framework.logger import Logger
from time import sleep
from selenium.webdriver.support.select import Select
logger = Logger('basepage页面').getlog()
class BasePage(object):
    
    def __init__(self,driver):
        self.driver = driver
    # 打开url站点   
    def open_url(self,url):
        self.driver.get(url)
    # 关闭浏览器
    def quit_browser(self):
        self.driver.close()
    # 浏览器前进操作    
    def forward(self):
        self.driver.forward()
        
    # 休眠
    def delay(self, seconds):
        try:
            sleep(seconds)
        except InterruptedError as e:
            logger.error(e)
    
    #隐式等待
    def wait(self,seconds):
        self.driver.implicitly_wait(seconds) 
        
    #获取标题
    def getTitle(self):
        return self.driver.title
    #查找元素
    def find_Element(self,selector):
        element = ''
        if '=>' not in selector:
            element = self.driver.find_element_by_id(selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]  #id_userName
        if selector_by == 'id':
            try :
                element = self.driver.find_element_by_id(selector_value)
                logger.info("Had find the Element \' %s \' successful"
                "by %s via value : %s " % (element.text, selector_by, selector_value) )
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
        elif selector_by =='n' or selector_by =='name':
            try :
                element = self.driver.find_element_by_name(selector_value)
                logger.info("Had find the Element \' %s \' successful"
                "by %s via value : %s " % (element.text, selector_by, selector_value) )
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
        elif  selector_by == 'css_selector':  
            element = self.driver.find_element_by_css_selector(selector_value)  
        elif  selector_by == 'classname':  
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_by == "l" or selector_by == 'link_text':  
            element = self.driver.find_element_by_link_text(selector_value)  
        elif selector_by == "p" or selector_by == 'partial_link_text':  
            element = self.driver.find_element_by_partial_link_text(selector_value)  
        elif selector_by == "t" or selector_by == 'tag_name':  
            element = self.driver.find_element_by_tag_name(selector_value)  
        elif selector_by == "x" or selector_by == 'xpath':  
            try:  
#                 print(selector_value)
                element = self.driver.find_element_by_xpath(selector_value)  
                logger.info("Had find the element \' %s \' successful "  
                                "by %s via value: %s " % (element.text, selector_by, selector_value))  
            except NoSuchElementException as e:  
                logger.error("NoSuchElementException: %s" % e)   
        elif selector_by == "s" or selector_by == 'selector_selector':  
            element = self.driver.find_element_by_css_selector(selector_value)  
        else:
            raise NameError("Please enter a valid type of targeting elements. ")
        return element
         
    #输入内容
    def input_Value(self,selector,text):
        element = self.driver.find_Element(selector)
        try:
            element.clear()
            element.send_keys(text)
            logger.info("Had type \' %s \' in input box." % text)
        except NameError as e:
            logger.error("Failed to type in input box with %s."% e)
    
    #点击元素
    def click_element(self,selector):
        element = self.driver.find_Element(selector)
        try:
            element.click()
            logger.info("The Element %s was clicked." % element)
        except NameError as e:
            logger.error("Failed to click the element with %s ." % e)
    
    #清除输入框元素
    def clear_element(self,selector):
        element = self.driver.find_Element(selector)
        element.clear()
    
    #选择selector(根据index选择)
    def select_index(self,selector,index):
        s = self.driver.find_Element(selector)
        Select(s).select_by_index(index)
    #选择文件上传
    def upload_file(self,selector,file):
        element = self.driver.find_Element(selector)
        try:
            element.send_keys(file)
            logger.info("The file %s was uploaded." % element)
        except FileNotFoundError as e:
            logger.error("Failed to find the file with %s ." % e)
            
    def get_textarea(self,selector):
        element = self.driver.find_Element(selector).get_attribute('value')
        return element
     
            

        