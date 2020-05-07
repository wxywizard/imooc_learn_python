a_list = [1, 2, 3, 4, 5]
b_list = [1, 4, 7, 9]
# 求两个列表之间的交集
int_list = set(a_list).intersection(set(b_list))
print(int_list)
# 求两个列表之间的并集
uni_list = set(a_list).union(set(b_list))
print(uni_list)
# 求两个列表之间的差集（a_list在b_list中不存在的部分）
dif_list = set(a_list).difference(set(b_list))
print(dif_list)

print(-1 % 2)