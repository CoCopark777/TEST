# coding=utf-8
# 进行web下拉框操作
__author__ = 'LGF'

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains    # 连贯操作需要,如悬浮鼠标才出现选项，单一操作无法达成
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
        self.driver.get('http://www.weather.com.cn/')
        print("打开 http://www.weather.com.cn/ ")
        self.driver.implicitly_wait(10)
        move1 = self.driver.find_element_by_class_name("select_li")
        ActionChains(self.driver).move_to_element(move1).perform()   # 鼠标移动到天气
        time.sleep(3)
        self.driver.find_element_by_link_text("资讯").click()
        time.sleep(3)
        # L_list.click()
        print("点击下拉框资讯成功")
        time.sleep(2)

    def post_condition_func(self):
        """

        :return:
        """
        self.driver.close()
        print("关闭练习网站")
