# coding=utf-8
#   web弹窗操作
__author__ = 'LGF'

from practice.kuangjia import Test
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains    # 连贯操作需要,如悬浮鼠标才出现选项，单一操作无法达成
import time


class Test004(Test):
    def pre_condition_func(self):
        """

        :return:
        """

    def test_004(self):
        """
        弹窗操作
        :return:
        """
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com/')
        move1 = self.driver.find_element_by_id('s-usersetting-top')
        ActionChains(self.driver).move_to_element(move1).perform()  #鼠标移动到设置
        print('鼠标移动到设置')
        time.sleep(2)
        self.driver.find_element_by_link_text('高级搜索').click()   #点击高级搜索
        print('点击高级搜索')
        time.sleep(2)
        #  使用select方法定位下拉框
        print('使用select方法定位下拉框')
        select = self.driver.find_element_by_class_name('c-select-selection')
        select.click()
        time.sleep(2)
        print('使用下拉框的选项')
        # 使用下拉框的选项
        self.driver.find_element_by_xpath('//*[@id="adv-setting-gpc"]/div/div[2]/div[2]/p[4]').click()
        print('点击最近一月')
        time.sleep(2)
        # 使用索引
        select.click()
        time.sleep(2)
        self.driver.find_element_by_link_text("最近一周").click()
        print('点击最近一周')
        time.sleep(2)



    def post_condition_func(self):
        """

        :return:
        """
        self.driver.close()
        print('关闭网站')
