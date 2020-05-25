import re

# 将正则表达式编译
pattern = re.compile(r'hello',re.I)

# 通过match进行匹配
rest = pattern.match('Hello,world!')
print(rest)