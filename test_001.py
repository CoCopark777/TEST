# coding=utf-8

from kuangjia import Test


class Test_001(Test):

    def pre_condition_func(self):
        print("Test_001的前置步骤")
        pass

    def test_procedure(self):
        print("Test_001具体的测试步骤")
        pass

    def post_condition_func(self):
        print("Test_001环境恢复")
        pass


class Test_002(Test):

    def pre_condition_func(self):
        print("Test_002的前置步骤")
        pass

    def test_procedure(self):
        print("Test_002具体的测试步骤")
        pass

    def post_condition_func(self):
        print("Test_002环境恢复")
        pass
