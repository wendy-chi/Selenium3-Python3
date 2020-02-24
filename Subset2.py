#print("以下为集合并集的操作：")

set_1 = set('what')
set_2 = set('whatabout')
set_3 = set('whataboutyou')
#第一种并集方法
#set_a = set_1 | set_2
#for a in set_a:
#    print(a)

#第二种并集方法
#set_a = set_1.union(set_2)
#for a in set_a:
#    print(a)

#print("以下为集合交集的操作：")
#这是第一种交集的方式
#set_b = set_1 & set_2
#这是第二种交集的方式
#set_b = set_1.intersection(set_2)
#打印出交集的集合元素
#for s in set_b:
#    print(s)

print("以下为集合差集的操作：")
#第一种差集的方式
set_c = set_2 - set_1
#第二种差集的方式
#set_c = set_1.difference(set_2)
#打印出差集的集合元素
for b in set_c:
    print(b)

