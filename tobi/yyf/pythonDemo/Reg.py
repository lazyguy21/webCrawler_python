import re

__author__ = 'ye'
str='http://css57.cnc.cdndm.com/blue/img/logo.png'
str3="http://www.youmtu.com/uploads/allimg/c150821/14401334S630-13228_lit.jpg"
str2=str[::-1]
re_compile = re.compile("[^/]+")
re_match = re.search('_lit', str3)
print(re_match)
match = re_compile.match(str2)

group = match.group()
resultName=group[::-1]
print(resultName)
