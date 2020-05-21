import re


"""
使用split正则分割字符串
"""
s = 'one1two2three33333four4five5six6'
p = re.compile(r'\d+')
rest = p.split(s)
print(rest)