import re

content = 'oen1two12three33four444five5six698'

#p = re.compile(r'\d+')
p = re.compile(r'[a-z]+',re.I)
rest = p.findall(content)
print(rest)