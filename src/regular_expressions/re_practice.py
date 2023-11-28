import re

p = re.compile('ab+')
m = p.search('brab.bbbbbb')

print(m.group())
