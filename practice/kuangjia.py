# coding=utf-8
import pytest


class Test:

    # def global_initial(self):
    #     print("全局初始化，一个批次只调用一次")
    #     pass
    #
    # def global_end(self):
    #     print("全局退出")
    #     pass

    # @pytest.fixture(scope='session', autouse=True)
    # def global_func(self):
    #     self.global_initial()
    #     yield
    #     self.global_end()

    def setup_method(self):
        print("脚本执行入口")
        self.pre_condition_func()

    def teardown_method(self):
        print("脚本结束后执行")
        self.post_condition_func()

    def pre_condition_func(self):
        print("脚本前置条件")
        pass

    def post_condition_func(self):
        print("环境恢复步骤")
        pass
