# -*- coding:utf-8 -*-
'''
Created on 2019年3月7日

@author: t_ful
'''
import os
from framework.browser_engine import Browser
from framework.basepage import BasePage
from framework.readExcle import ReadExcle
from framework.logger import Logger 
logger = Logger("newEnterPage").getlog() #加日志的
class NewEnterPPage(BasePage):
    global sheet_dir,element0,list0,element1,list1
    sheet_dir = os.path.abspath('.').split('src')[0] + 'PageElements\\elements.xlsx'
    element0,list0 = ReadExcle(sheet_dir).get_Value('newEnterP') #企业注册页
    element1,list1 = ReadExcle(sheet_dir).get_Value('login')  #首页
    '''selector:元素名称（自定义/dict里的key）text：输入框输入的值
            输入内容
    '''  
    def input(self,selector,text):
        self.clear_element(element0[selector])
        self.input_Value(element0[selector], text)
    #登陆正常步骤   
    def new_enterP(self,ismerge,enterPriseName,businessLicenseCode,businessLicenseURL,corporateName,corporateIDURL
                    ,businessStartDate,businessTermStartDate,businessTermEndDate,businessAddress,
                   businessNo,organizationCode,organizationCodeURL,organizationName,organizationType,organizationEffectiveDate,
                   organizationExpirationDate,entrustmentLetterURL,acceptanceURL,agentName,agentPID,agentIDTURL,agentIDURL,
                   agentIDFURL,agentIDHURL,agentIDAddress,agentIDGender,agentIDNation,agentIDBirthDay,agentIDIssuingAuthority,
                   agentIDCertValiddate,agentIDCertExpdate,agentContactNo,agentAddress,contactName,contactNo):
        self.click_element(element1['one'])
        self.delay(2)
        self.click_element(element0['id'])
        self.select_index(element0['ismerge'], ismerge)  #0/1
        self.input('enterPriseName', enterPriseName)
        self.input('businessLicenseCode', businessLicenseCode)
        self.upload_file(element0['businessLicenseURL'], businessLicenseURL)
        self.delay(2)
        self.input('corporateName', corporateName)
        self.upload_file(element0['corporateIDURL-input-file'], corporateIDURL)
        self.input('businessStartDate', businessStartDate)
        self.input('businessTermStartDate', businessTermStartDate)
        self.input('businessTermEndDate', businessTermEndDate)
        self.input('businessAddress', businessAddress)
        self.input('businessNo', businessNo)
        self.input('organizationCode', organizationCode)
        self.upload_file(element0['organizationCodeURL-input-file'], organizationCodeURL)
        self.input('organizationName', organizationName)
        self.input('organizationType', organizationType)
        self.input('organizationEffectiveDate', organizationEffectiveDate)
        self.input('organizationExpirationDate', organizationExpirationDate)
        self.upload_file(element0['entrustmentLetterURL-input-file'], entrustmentLetterURL)
        self.upload_file(element0['acceptanceURL-input-file'], acceptanceURL)
        self.input('agentName', agentName)
        self.input('agentPID', agentPID)
        self.upload_file(element0['agentIDTURL-input-file'], agentIDTURL)
        self.upload_file(element0['agentIDURL-input-file'], agentIDURL)
        self.upload_file(element0['agentIDFURL-input-file'], agentIDFURL)
        self.upload_file(element0['agentIDHURL-input-file'], agentIDHURL)
        self.input('agentIDAddress', agentIDAddress)
        self.select_index(element0['agentIDGender'], agentIDGender) #0/1
        self.input('agentIDNation', agentIDNation)      
        self.input('agentIDBirthDay', agentIDBirthDay)
        self.input('agentIDIssuingAuthority', agentIDIssuingAuthority)
        self.input('agentIDCertValiddate', agentIDCertValiddate)
        self.input('agentIDCertExpdate', agentIDCertExpdate)
        self.input('agentContactNo', agentContactNo)
        self.input('agentAddress', agentAddress)
        self.input('contactName', contactName)
        self.input('contactNo', contactNo)
        self.delay(10)
        self.click_element(element0['submitCrop'])
        print(self.get_textarea(element0['result']))
        return self.get_textarea(element0['result'])
        
