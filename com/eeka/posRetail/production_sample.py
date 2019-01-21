# -*- coding: utf-8 -*-
# Author: sunzheng
# Time: 2018/12/20

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from com.eeka.posRetail.prod_sample_loc import Prod_Sa_Loc as ps
import time

class Production_Sample:

    def __init__(self,driver):
        self.driver=driver

    def click_ProductionSample(self):
        # js = "var q=document.getElementById('id').scrollTop=0"
        # self.driver.execute_script(js)
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(ps.retail_sys))
        self.driver.find_element(*ps.retail_sys).click()
        time.sleep(3)
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(ps.bighuo))
        self.driver.find_element(*ps.bighuo).click()
        time.sleep(5)
    '''
       *********进入大货列表，查询订单（这里方法调用错了）*********
       1.查询新增订单验证
       2.取出第一条订单数据（订单新建后，默认显示在第一条）
       '''
    def search_dahuo_order(self):
        WebDriverWait(self.driver, 30).until(EC.frame_to_be_available_and_switch_to_it(ps.bighuolist))

        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(ps.mobile))
        self.driver.find_element(ps.mobile).send_keys("18820941844")

        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(ps.sorder))
        self.driver.find_element(*ps.sorder).click()


        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(ps.get_bid_order))
        order_search = self.driver.find_element(*ps.get_bid_order).text
        print("新创建的智化大货订单为：{}".format(order_search))
        return order_search