# -*- coding: utf-8 -*-
# Author: sunzheng
# Time: 2018/12/26

from com.eeka.posRetail.retail_page_loc import  Retail_Sys as rs

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class POS_Idex:
    def __init__(self,driver):
        self.driver=driver
    '''
    1.点击零售管理菜单
    1.点击智化大货菜单
    '''
    def retail_system(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(rs.retail_sys))
        self.driver.find_element(*rs.retail_sys).click()

        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(rs.big_huo))
        self.driver.execute_script("window.scrollTo(200,document.body.scrollHeight)")
        huohuo=self.driver.find_element(*rs.big_huo).text
        print("找到:{},菜单".format(huohuo))
        self.driver.find_element(*rs.big_huo).click()
    '''
    1.进入智化大货list页面
    2.输入会员手机号码查询
    3.输入商品编码查询
    '''
    def Intelligent_goods(self,mobile,spnumber):
        WebDriverWait(self.driver, 30).until(EC.frame_to_be_available_and_switch_to_it(rs.bighuo_list))

        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(rs.mobile_number))
        self.driver.find_element(*rs.mobile_number).send_keys(mobile)
        self.driver.find_element(*rs.search).click()

        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(rs.sp_number))
        self.driver.find_element(*rs.sp_number).send_keys(spnumber)
        self.driver.find_element(*rs.click_serach).click()
    '''
    1.选择默认靠码定制
    2.可以选择靠码尺寸（这里选择默认的码数）
    '''
    def Code_customization(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(rs.daogou))
        self.driver.find_element(*rs.daogou).click()
        time.sleep(3)
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(rs.xuanz1))
        self.driver.find_element(*rs.xuanz1).click()

        time.sleep(3)
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(rs.click_mlist))
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.driver.find_element(*rs.click_mlist).click()
        time.sleep(3)
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(rs.mendian))
        self.driver.find_element(*rs.mendian).click()
        time.sleep(3)
        self.driver.find_element(*rs.caert_order).click()

    #获取订单金额
    def get_orderAmoner(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(rs.Amoner))
        order_moner = self.driver.find_element(*rs.Amoner).text
        print("你的订单金额为：{}".format(order_moner))
        return order_moner

    '''
    1.点击收银按钮
    2.选择现金收银方式
    3.输入订单金额
    4.添加，完成付款
    '''
    def tocollect_money(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(rs.to_collect_money))
        self.driver.find_element(*rs.to_collect_money).click()
        time.sleep(3)
        ######################
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(rs.click_moner))
        self.driver.find_element(*rs.click_moner).click()

        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(rs.moner_type))
        self.driver.find_element(*rs.moner_type).click()

        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(rs.output_moner))
        self.driver.find_element(*rs.output_moner).send_keys(self.get_orderAmoner())
        time.sleep(3)
        self.driver.find_element(*rs.add).click()
        time.sleep(3)
        self.driver.find_element(*rs.gemover).click()
        time.sleep(3)
        self.driver.find_element(*rs.quit)
        time.sleep(5)



