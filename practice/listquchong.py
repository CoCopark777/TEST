# # coding =utf-8
#
# a_list = [1,2,2,3,3,4,5,6,7,7,8]
# b_list = []
#
# for i in a_list:
#     if i not in b_list:
#         b_list.append(i)
# # print(b_list)
#
# q_list =  ['a', 'b', 'c','d']
# q_list.insert(1, 'x')
# print(q_list)
#
# w_list = ['a','b','c']
# s_liat = ['d','e','f']
# for i in s_liat:
#     w_list.append(i)
# print(w_list)


# a = '11 hello ever list cool hello'
# print(a.find('he'))
# print(a.index('hel', 15))
# aa = a.replace('11', 'oh')
# print(a)
# print(aa)

# a_list = ['psu_1', 'psu_2', 'psu_3', 'psu_4']
# b_list = []
# for i in a_list:
#     aa = i.split('_')
#     b_list.append(aa)
# print(b_list)

a_list = ['psu1\npsu2\npsu3']
b_list = []
for i in a_list:
    aa = i.split('\n')
    b_list.append(aa)
print(b_list)
# a_list = ['psu_1', 'psu_2', 'psu_3', 'psu_4']
# b = []
# for i in a_list[::-1]:
#     b.append(i.split('_')[1])
# print(b)

# j = 1
# while j < 10:
#     i = 1
#     while i <= j:
#         print("%s * %s = %s " % (i, j, i*j), end='')
#         i += 1
#     print()
#     j += 1


# from practice import pubilc
#
# pubilc.law_set_value()
# import time
#
# aa = time.localtime(time.time())
# bb = time.strftime('%Y-%m-%d %H:%M:%S ', aa)
# print(aa)
# print(bb)
# print("当前时间： ",time.strftime('%Y-%m-%d %H:%M:%S ',time.localtime(time.time())))