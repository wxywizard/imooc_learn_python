import re

"""
使用正则进行替换
"""
content = 'one1two2three33333four4five5six6'
# 使用正则替换
p = re.compile(r'\d+')
rest = p.sub('@',content)
print(rest)

# 使用字符串原始的替换方式
rest_origin = content.replace('1','@').replace('2','@').replace('33333','@')
print(rest_origin)


# 使用正则表达式
s2 = 'hello world'
p2 = re.compile(r'(\w+) (\w+)')
rest_pos = p2.sub(r'\2 \1',s2)
print(rest_pos)

# 在原有的内容基础上，替换并改变内容
def f(m):
    """ 使用函数进行替换规则改变 """
    return m.group(2).upper()+ ' ' + m.group(1)
rest_change = p2.sub(f,s2)
print(rest_change)

# 使用匿名函数进行替换 lambda
rest_lamb = p2.sub(lambda m:m.group(2).upper()+ ' ' + m.group(1),s2)
print(rest_lamb)