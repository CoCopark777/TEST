# coding=utf-8
from selenium import webdriver
import time
from practice.kuangjia import Test
import logging

logging.basicConfig(level=logging.WARNING,  # 控制台打印的日志级别
                    filename="D:\\loginfo\\time.log",
                    filemode='a',  # 模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    # a是追加模式，默认如果不写的话，就是追加模式
                    format=
                    '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    # 日志格式
                    )


class Test002(Test):

    def pre_condition_func(self):
        logging.info("脚本开始，前置步骤")

    def test_guocheng(self):
        driver = webdriver.Chrome()
        driver.get('http://www.weather.com.cn/')
        time.sleep(5)
        driver.quit()
        logging.info("打印信息加入，用于生成log文件")

    def post_condition_func(self):
        logging.info("用例结束")
