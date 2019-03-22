# -*- coding:utf-8 -*-
'''
Created on 2019��2��18��

@author: t_ful
'''

import logging
import os
import time
class Logger(object):
    def __init__(self,logger):
        #创建一个logger，输出到文件
        self.logger = logging.getLogger(logger)
        self.logger.setLevel('WARNING') 
        #time，设置时间格式
        '''
        time.time() 从1970纪元开始至今的秒数，时间戳
        time.localtime() 将时间戳转换为人类能读懂的时间，若括号内没有指定时间，则默认为当前时间
        eg:
           time.struct_time(tm_year=2016, tm_mon=11, tm_mday=27, tm_hour=10, tm_min=26, tm_sec=5, tm_wday=6, tm_yday=332, tm_isdst=0) 
        '''
        nt = time.strftime('%Y%m%d',time.localtime(time.time())) 
#         LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
#         DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
        log_dir = os.path.abspath('.').split('src')[0] + '/logs/'
        log_name = log_dir + nt + '.log'   
        filehander = logging.FileHandler(log_name) 
#         logging.basicConfig(filename=log_name, level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)    
#         filehander.setLevel('DEBUG')        
        #创建一个logger，输出到控制台
        streamhander = logging.StreamHandler()
#         streamhander.setLevel("DEBUG")
        #定义handle的格式输出
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') 
        filehander.setFormatter(formatter)
        streamhander.setFormatter(formatter)
        self.logger.addHandler(filehander)
        self.logger.addHandler(streamhander)
        
    def getlog(self):
        return self.logger
    

    

        





    
        
        