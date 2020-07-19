# coding=utf-8
#   web弹窗操作
__author__ = 'LGF'

from practice.kuangjia import Test
from selenium import webdriver
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
        self.driver.get('https://liushilive.github.io/html_example/index1.html')

        window1 = self.driver.find_element_by_id('b1')
        window2 = self.driver.find_element_by_id('b2')
        window1.click()
        print("点击告警窗口1")

        self.driver.switch_to.alert.accept()
        print("点击接受")
        time.sleep(5)
        window1.click()
        self.driver.switch_to.alert.dismiss()
        print("点击取消")
        time.sleep(5)

        window2.click()
        print("点击弹窗2")
        self.driver.switch_to.alert.send_keys("hello")
        time.sleep(5)
        self.driver.switch_to.alert.accept()
        print("点击接受")
        time.sleep(2)

    def post_condition_func(self):
        """

        :return:
        """
        self.driver.close()
        print('关闭网站')
