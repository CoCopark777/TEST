# coding=utf-8
import pytest
import logging


logging.basicConfig(level=logging.WARN, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.WARNING,  # 控制台打印的日志级别
                    filename="D:\\loginfo\\time.log",
                    filemode='a',  # 模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    # a是追加模式，默认如果不写的话，就是追加模式
                    format=
                    '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    # 日志格式
                    )

class Test:

    def global_initial(self):
        print("全局初始化，一个批次只调用一次")
        pass

    def global_end(self):
        print("全局退出")
        pass

    @pytest.fixture(scope='session', autouse=True)
    def global_func(self):
        self.global_initial()
        yield
        self.global_end()

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
