set_1 = set('what')
set_2 = set('whatabout')
set_3 = set('whataboutyou')

print(set_1 < set_2)
print(set_2 < set_3)
print(set_3 > set_1)

print(set_1.issubset(set_2))
print(set_1.issubset(set_3))