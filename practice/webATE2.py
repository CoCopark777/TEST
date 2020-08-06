# coding=utf-8

# 进行web登录操作
from selenium import webdriver
from practice.kuangjia import Test
import time
from selenium.webdriver.common.action_chains import ActionChains    # 连贯操作需要,如悬浮鼠标才出现选项，单一操作无法达成


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
        self.driver.get("https://www.baidu.com/")
        print("打开练习网址 https://www.baidu.com/")
        self.driver.implicitly_wait(10)
        time.sleep(2)
        # 点击搜索框旁的内容
        move1 = self.driver.find_element_by_id("s-usersetting-top")
        ActionChains(self.driver).move_to_element(move1).perform()  #按顺序操作,鼠标移动到设置
        print("按顺序操作,鼠标移动到设置")
        self.driver.find_element_by_link_text("搜索设置").click()  #点击搜索设置
        print("点击搜索设置")
        time.sleep(5)
        self.driver.find_element_by_id('nr_2').click()  #点击每页20条
        print("点击每页20条")
        time.sleep(5)
        self.driver.find_element_by_link_text('保存设置').click()  #保存设置
        print("保存设置")
        time.sleep(1)
        self.driver.switch_to.alert.accept()

    def post_condition_func(self):
        print("环境恢复")
        self.driver.close()
        print("关闭web")

