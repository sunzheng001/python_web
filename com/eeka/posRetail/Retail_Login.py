# -*- coding: utf-8 -*-
# Author: sunzheng
# Time: 2018/12/26

from com.eeka.posRetail.retail_page_loc import  Retail_Sys as rs
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Retail_Bighuo:
    def __init__(self,driver):
        self.driver=driver
     #POS系统登录
    def input_login(self,username,userpwd):
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(rs.login_username))
        self.driver.find_element(*rs.login_username).clear()
        self.driver.find_element(*rs.login_username).send_keys(username)

        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(rs.login_pwd))
        self.driver.find_element(*rs.login_pwd).clear()
        self.driver.find_element(*rs.login_pwd).send_keys(userpwd)

        self.driver.find_element(*rs.login_submit).click()

    def login_successful(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(rs.login_account))
        account=self.driver.find_element(*rs.login_account).text
        print("POS系统登录的账号为：{}".format(account))





