import re

content = 'hello,world!'

p = re.compile(r'world')

# 使用search
rest = p.search(content)
print(rest)

# 使用match
rest_match = p.match(content)
print(rest_match)

# match vs search
