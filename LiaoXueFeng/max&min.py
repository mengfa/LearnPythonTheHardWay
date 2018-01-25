# _*_ coding: utf-8 _*_
__author__ = 'lv'
__date__ = '2018/1/25 18:23'
# -*- coding: utf-8 -*-
def findMinAndMax(L):
    if L is None or len(L) <= 0:
        return (None, None)
    min = L[0]
    max = L[0]
    for s in L:
        print s
        if s>max:
            max=s

        if s<min:
            min=s
        print min
    return (min,max)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')