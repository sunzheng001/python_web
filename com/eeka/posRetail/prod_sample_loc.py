# -*- coding: utf-8 -*-
# Author: sunzheng
# Time: 2018/12/20
from selenium.webdriver.common.by import By
class Prod_Sa_Loc:
    # 左侧菜单
    click_leftjoin = (By.XPATH, '//div[@class="leftMenu"]')

    # 零售管理
    retail_sys = (By.XPATH, '//span[@class="icon-shopping-cart"]')

    bighuo = (By.XPATH, '//a[text()="大货定做列表"]')

    bighuolist = (By.XPATH,"//div[@id='tabCon']//iframe[2]")
    # 大货列表
    # bighuo_list = (By.XPATH,'//iframe[@src="/Customization/LargeGoodsMade/Index2"]')

    mobile = (By.ID, '//input[@id="TelePhoneNo"]')

    sorder = (By.ID, '//button[@id="btn_Search"]')

    get_bid_order = (By.XPATH, '//tr[@id="1"]//td[2]')