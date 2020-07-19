'''
1 准备数据
2 格式化输出数据
'''

age = 18
name = 'TOM'
weight = 75.5
stu_id = 123

# 1 今年我的年龄是X岁
print('今年我的年龄是 %d 岁' % age)
# 2 我的名字是X
print('我的名字是%s' % name)
# 3 我的体重是X公斤
print('我的体重是%0.2f公斤' % weight)
# 4 我的学号是X
print('我的学号是%05d' % stu_id)
# 5 我的名字是X ，今年Y 岁，体重是Z公斤，学号是A
print('我的名字是%s ，今年%d岁，体重是%.2f公斤，学号是%06d' % (name, age, weight, stu_id))
# 语法 f'{}'  和表达字符串效果一致
print(f'我的名字是{name} ，今年{age}岁，体重是{weight}公斤，学号是{stu_id}')
