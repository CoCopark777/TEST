# coding=utf-8
# 获取搜索框内容

__author__ = 'LGF'

from practice.kuangjia import Test
from selenium import webdriver
import time


class Test005(Test):
    def pre_condition_func(self):
        """

        :return:
        """

    def test_005(self):
        """

        :return:
        """
        self.driver = webdriver.Chrome()
        url = "http://www.sogou.com"
        # 访问sogou首页
        self.driver.get(url)
        # 找到搜索输入框元素
        searchBox = self.driver.find_element_by_id("query")
        # 获取搜索输入框页面元素的name属性值
        print(searchBox.get_attribute("name"))
        time.sleep(5)
        # 向搜索输入框中输入“测试工程师指定的输入内容”内容
        searchBox.send_keys("测试工程师指定的输入内容")
        # 获取页面搜索框的value属性值（即搜索输入框的文字内容）
        print(searchBox.get_attribute("value"))
        time.sleep(5)

    def post_condition_func(self):
        """

        :return:
        """
        self.driver.close()
        print("关闭浏览器")
