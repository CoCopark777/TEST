# coding=utf-8

# 进行web登录操作
from selenium import webdriver
from practice.kuangjia import Test
import time


class Test002(Test):
    def pre_condition_func(self):
        """
        前置条件
        :return:
        """
    print("进入前置准备条件")

    def test_ceshibuzhou(self):
        """
        具体测试步骤
        :return:
        """
        self.driver = webdriver.Chrome()
        # 一个不错的练习地址
        self.driver.get("https://liushilive.github.io/html_example/index1.html")
        print("打开练习网址 https://liushilive.github.io/html_example/index1.html ")
        # 登录窗口位置定义
        self.ele_user = self.driver.find_element_by_id("uid")
        self.ele_pwd = self.driver.find_element_by_id("pwd")

        # 先清空登录窗口内容
        self.ele_user.clear()

        # 输入账号密码进行登录
        self.ele_user.send_keys("admin")
        time.sleep(1)
        self.ele_pwd.send_keys("123456")
        time.sleep(1)
        # 点击确认
        self.submit = self.driver.find_element_by_xpath("/html/body/div[5]/div/form/input[1]")
        self.submit.click()
        time.sleep(5)
        print("点击登录成功")

    def post_condition_func(self):
        print("环境恢复")
        self.driver.close()
        print("关闭web")

