# _*_ coding: utf-8 _*_
__author__ = 'lv'
__date__ = '2018/1/25 17:34'

# -*- coding: utf-8 -*-

import math

def quadratic(a, b, c):
    t = b*b-4.0*a*c
    if t < 0:
        return None
    elif t == 0:
        return -b/2*a
    elif t > 0:
        x1 = (-b -math.sqrt(t)) / (2.0*a)
        x2 = (-b + math.sqrt(t)) / (2.0 * a)
        return x2,x1

# def quadratic(a,b,c):
#     if not isinstance(a,(int,float)):
#         raise TypeError('a is not a number')
#     if not isinstance(b,(int,float)):
#         raise TypeError('b is not a number')
#     if not isinstance(c,(int,float)):
#         raise TypeError('c is not a number')
#     d=b*b-4*a*c
#     if a==0:
#         if b==0:
#             if c==0:
#                 return '方程根为全体实数'
#             else:
#                 return '方程无根'
#         else:
#             x1=-c/b
#             x2=x1
#             return x1,x2
#     else:
#         if d<0:
#             return '方程无根'
#         else:
#             x1 = (-b + math.sqrt(d))/2/a
#             x2 = (-b - math.sqrt(d))/2/a
#             return x1,x2
# print(quadratic(2,3,1))
# print(quadratic(1,3,-4))


print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')