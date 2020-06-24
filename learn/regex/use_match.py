import re

# 将正则表达式编译
pattern = re.compile(r'hello',re.I)

# 通过match进行匹配
rest = pattern.match('Hello,world!')
print(rest)

def f(sub):
    return sub.group(2)+""+sub.group(1)


# 将正则表达式编译
content = 'aa ! python'
pattern = re.compile(r'(\w+) (\w+)')

# 通过match进行匹配
#rest = pattern.findall(content)
rest = pattern.sub(f,content)
print("==>{}".format(rest))




