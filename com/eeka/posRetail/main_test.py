# -*- coding: utf-8 -*-
# Author: sunzheng
# Time: 2018/12/20

from  selenium import webdriver
import unittest
from com.eeka.posRetail.Retail_Login import   Retail_Bighuo
from com.eeka.posRetail.Retail_Index import  POS_Idex
from com.eeka.posRetail.production_sample import Production_Sample
import time

class Pos_Test(unittest.TestCase):
    def setUp(self):

        self.driver=webdriver.Chrome()
        self.driver.get("http://csdrp.szyingjia.org:86/Login/Index")
        self.driver.maximize_window()
        time.sleep(3)
        self.ls = Retail_Bighuo(self.driver)
        self.rtl=POS_Idex(self.driver)
        self.ps = Production_Sample(self.driver)

    # def test_pos_login(self):
    #     '''
    #     1.在登录页面输入账号密码
    #     2.判断用户是否登录成功
    #     '''
    #     self.ls.input_login("00101826","1")
    #     time.sleep(5)
    #     self.ls.login_successful()

    def test_retail_manage(self):
        '''
        1.点击零售管理
        2.点击智化大货
        3.进入智化大货2.0页面
        '''
        # self.test_pos_login()
        self.ls.input_login("00101826", "1")
        time.sleep(5)
        self.ls.login_successful()
        # self.rtl.retail_system()
        # self.rtl.Intelligent_goods("18820941844","N1AHF53490")
        # self.rtl.Code_customization()
        # self.rtl.tocollect_money()
        # time.sleep(3)
        # self.driver.refresh()
        # time.sleep(5)
        self.ps.click_ProductionSample()
        time.sleep(3)
        self.ps.search_dahuo_order()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()
