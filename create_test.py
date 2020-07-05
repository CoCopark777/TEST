# coding=utf_8
"""
---------
文件名：脚本模板生成
描述： 根据导出的表格name,number,pre_condition,test_step，生成py自动化文本
作者： LGF
创建日期：2020/7/2
---------
"""
import os
import time
import shutil
import xlrd


def get_test():
    """
    自动生成脚本

    """
    # 获取本地时间
    localtime = ('%Y-%m-%d %H:%M%S', time.localtime(time.time()))
    # 如果当前存在testcase文件，删除此文件
    if os.path.isdir("D:\\testcase"):
        shutil.rmtree("D:\\testcase")
    time.sleep(1)
    # 新建testcase
    os.mkdir("D:\\testcase")
    time.sleep(1)
    # 定义表格信息
    testcase_path = "D:\\testcase.xlsx"
    # 打开表格
    data = xlrd.open_workbook(testcase_path)
    # 定义工作薄，以名字查找
    table = data.sheet_by_name('Sheet1')
    # 输入创作者
    creater = input('input your name, like XXX: ')
    # 获取第一行内容
    row_net = table.row_values(0)
    print("row_net:%s" % row_net)
    # 循环当前有效行数，从第二行开始
    for i in range(1, table.nrows):
        print("i:%s,table.nrows:%s" % (i, table.nrows))
        temp = table.row_values(i)
        print("row_net:%s,temp:%s" % (row_net, temp))
        dict_temp = dict(zip(row_net, temp))
        if dict_temp['number'] is None:
            continue
        case_num = dict_temp['number']
        step_pre = dict_temp['pre_condition'].split('\n')
        step_list = dict_temp['test_step'].split('\n')
        test_case_name = format('tc_%s.py' % case_num)
        file = open("D:\\testcase\\'" + test_case_name, 'w+', encoding='UTF-8')
        info = """coding = utf-8
        \"\"\"
        ------------
        文件名:    %s
        描述:
        作者:     %s
        创建日期:   %s
        ------------
        \"\"\"
        """ % (dict_temp['name'], creater, localtime)

        info1 = """
calss Test_%s(Tset):        
        """ % case_num

        info2 = """
    def pre_condition_func(self):
        \"\"\"
        """

        info3 = """
        \"\"\"
    # 用例前置条件
    print("用例前置条件")
    
    def test_procedure(self):
        \"\"\"
        """
        info4 = """
        :return:
        \"\"\"
        """

        info5 = """
    def post_condition_func(self):
        \"\"\"
        后置
        \"\"\"
        print("脚本环境恢复")    
        """

        file.write(info)
        file.write('\n')
        file.write(info1)
        file.write('\n  ')
        file.write('"""\n   ')
        for step in step_list:
            file.write('%s\n' % step)
            file.write('    ')
        file.write('"""\n')
        file.write(info2)
        for step in step_pre:
            file.write(step)
        file.write(info3)

        file.write(info4)
        for step in step_list:
            file.write('self.logger.step("%s")\n    ' % step)
        file.write(info5)
        file.close()


if __name__ == '__main__':
    get_test()
