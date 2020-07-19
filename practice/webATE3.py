# coding=utf-8
# 进行web下拉框操作
__author__ = 'LGF'

from selenium import webdriver
from selenium.webdriver.support.select import Select    # 鼠标选择 选择下拉框
import time
from practice.kuangjia import Test


class Test003(Test):
    def pre_condition_func(self):
        """

        :return:
        """

    def test_003(self):
        """

        :return:
        """
        self.driver = webdriver.Chrome()
        self.driver.get('https://liushilive.github.io/html_example/index1.html')
        print("打开练习网址 https://liushilive.github.io/html_example/index1.html ")

        L_list = self.driver.find_element_by_id("s1Id")
        # 实例化select
        L_list_select = Select(L_list)
        # L_list.click()
        # print("点击下拉框成功")
        time.sleep(2)
        L_list_select.select_by_index(1)
        print("选择第二个内容")
        time.sleep(2)
        L_list_select.select_by_value('sh')
        print("选择上海")
        time.sleep(2)

    def post_condition_func(self):
        """

        :return:
        """
        self.driver.close()
        print("关闭练习网站")
