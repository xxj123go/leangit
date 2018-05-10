# -*- coding: utf-8 -*-

#---------------------------------------------------
#条件 循环
#--------------------------------------------------

n1 = 'xie'
n2 = 'xiao'
n3 = 'jie'
print n1, n2, n3
print n1 + n2 + n3

import  math as mymath
print mymath.pi

from math import  sqrt as mysqrt
print mysqrt(4)

print  True + False +42
# 43

# is 同一性判断 是否是同一个对象
x = y = [1,2,3]
z = [1,2,3]
print  x is y #True
print x is z  #False x 和 z 值相同，但是指向的是不同的对象

# 类三木运算符
# a if b else c 如果b为真，返回a，否则返回c
print 1 if (1 == 1) else 2 #1
print 1 if (1 == 2) else 2 #2

age = 10
assert 0<age<100
age = -1

# 翻转和排序迭代
# sorted 可作用于任何序列或对象，非原地修改，返回列表
print sorted([2,6,4,8,1]) #[1, 2, 4, 6, 8]
print sorted('hello') #['e', 'h', 'l', 'l', 'o']

print list(reversed('hello')) #['o', 'l', 'l', 'e', 'h']

print '-------列表推导式----------'
# 列表推导式
print  [x*x for x in range(0,10)]
# 打印范围内能被三整除的数
print [x for x in range(0,10) if x%3 == 0] #[0, 3, 6, 9]

# 多for的情况
print  [(x,y) for x in range(0,3) for y in range(0,3)]
# [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
# 传统方式实现如下
result =[]
for x in range(0,3):
    for y in range(0,3):
        result.append((x,y))
print result
# [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

# pass
# 占位
a = 10
if a >0:
    pass
else:
    print "not > 0"


# del 删除变量，但是python没有办法删除值，值是GC处理的
x = {'x':1}
y = x
del x
print  y #{'x': 1} 删除 x 之后，只是删除了变量x，值还被y引用着

# exec
# 将定义的命令放到特定的命名空间执行
from math import sqrt
scope = {}
exec "sqrt = 100" in scope
print  sqrt(4) #2.0
print scope['sqrt'] #100

