# coding = utf-8
"""
------------
文件名:    用例1
描述:
作者:     123
创建日期:   2020-08-04 21:50:43
------------
"""

from practice.kuangjia import *
import logging

class Test_20200702(Test):

    def pre_condition_func(self):
        """
        前置1:1111
        前置2:1112
        前置3:1113
        
        """
        # 用例前置条件
        print("用例前置条件")
    
    def test_procedure(self):
        """
        
        :return:
        """
        logging.info("步骤1:11111")
        logging.info("步骤2:2222222")
        logging.info("步骤3:3333333")
        
    def post_condition_func(self):
        """
        后置
        """
        print("脚本环境恢复")    
        