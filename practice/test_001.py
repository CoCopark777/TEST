# coding=utf-8
import time
from selenium import webdriver
from practice.kuangjia import Test


class Test001(Test):

    def pre_condition_func(self):
        """
        用例前置

        """
        self.driver = webdriver.Chrome()
        # self.driver.get('http://www.weather.com.cn/')
        # print("登录中国天气网成功")
        # time.sleep(2)
        # self.driver.quit()
        # print("退出中国天气网")

    def test_procedure(self):
        """
        具体步骤

        """

        self.driver = webdriver.Chrome()
        self.driver.get('http://www.weather.com.cn/')
        print("再次登录中国天气网成功，准备进入登录界面")
        time.sleep(2)
        # 点击登录
        self.driver.find_element_by_class_name("login-icon").click()
        print("点击登录按钮")
        time.sleep(2)
        self.driver.find_element_by_id("username").send_keys("825510546@qq.com")
        print("输入账号")
        time.sleep(1)
        self.driver.find_element_by_id("password").send_keys("test0925")
        print("输入密码")
        time.sleep(1)
        self.driver.find_element_by_id("loginBtnId").click()
        print("点击登录按钮")
        time.sleep(2)
        print(self.driver.current_url)
        # 预期失败
        assert 'http://www.weather.com.c/' == self.driver.current_url
        print('登陆成功.')
        time.sleep(2)

    def post_condition_func(self):
        """
        环境恢复

        """
        self.driver.quit()

# class Test_002(Test):
#
#     def pre_condition_func(self):
#         print("Test_002的前置步骤")
#         pass
#
#     def test_procedure(self):
#         print("Test_002具体的测试步骤")
#         pass
#
#     def post_condition_func(self):
#         print("Test_002环境恢复")
#         pass
