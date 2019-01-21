# -*- coding: utf-8 -*-
# Author: sunzheng
# Time: 2018/12/26
from selenium.webdriver.common.by import By
class Retail_Sys:
    login_username=(By.XPATH,'//input[@id="username"]')

    login_pwd=(By.XPATH,'//input[@id="password"]')

    login_submit=(By.XPATH,'//button[@id="submit_btn"]')
    #登录账号
    login_account=(By.XPATH,'//div[@class="rightUser"]')
    #零售管理
    retail_sys=(By.XPATH,'//span[@class="icon-shopping-cart"]')
    #智化大货定制
    big_huo=(By.XPATH,'//dl[@class="cur"]//dd//a[contains(text(),"智化大货定制")]')
    #大货列表
    bighuo_list=(By.XPATH,'//iframe[@src="/Customization/LargeGoodsMade/Index2"]')
    '''
    下面是大货定制页面对象，应该封装在其他class里面
    '''
    #会员手机号
    mobile_number=(By.XPATH,'//input[@id="SearchKey"]')
    #点击查询按钮
    search=(By.XPATH,'//button[@id="searchphone"]')
    #商品编码
    sp_number=(By.XPATH,'//input[@id="ItemCode"]')
    #点击搜索按钮
    click_serach=(By.XPATH,'//button[@id="sectionnumber"]')

    #选择点击导购框
    daogou=(By.XPATH,'//button[@data-id="SalesRepNames"]')
    #选择导购
    xuanz1=(By.XPATH,'//ul[@role="listbox"]//li[1]')
    xuanze=(By.XPATH,'//button//span[text()="陈文凤"]')
    #选择当前门店
    click_mlist=(By.XPATH,'//input[@placeholder="请选择收货地址"]')
    mendian=(By.XPATH,'//dd[text()="当前门店"]')

    #创建订单，可以增加校验
    caert_order=(By.XPATH,'//button[@id="btn_createCustom"]')
    '''
    订单创建成功，进行订单收银
    2.可以判断是否出现收银，如果出现说明订单创建成功
    '''
    to_collect_money=(By.XPATH,'//button[@id="btn_collectmoney"]')

    #进入收银弹框页面
    # kmoner=(By.XPATH,'//div[@class="layui-layer layui-layer-page OverflowNoContent"]')
    #订单金额
    Amoner=(By.XPATH,'//label[@id="DifferenceAmt"]')

    click_moner=(By.XPATH,'//input[@placeholder="请选择"]')

    moner_type=(By.XPATH,'//dd[text()="现金"]')

    output_moner=(By.XPATH,'//input[@id="CollectionAmount"]')

    add=(By.XPATH,'//a[@id="collectmoneyadd"]')

    gemover=(By.XPATH,'//a[text()="完成"]')

    #取消打印小票
    quit=(By.XPATH,'//a[text()="取消"]')

    #// td[text() = "18820941844"][1]
    line_one=(By.XPATH,'//tr[@id="1"]')