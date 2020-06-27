# break

a = 1
while a <= 3:
    print('当前操作为{0}'.format(a))
    i = 1
    while i <= 5:
        if i == 4:
            print('到达4，退出')
            i += 1
            continue
        print('当前值为{0}'.format(i))
        i += 1
    a += 1
print('结束了')
