# _*_ coding: utf-8 _*_
__author__ = 'lv'
__date__ = '2018/1/25 17:03'

# L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
#
# M = L[0:3]
#
# print('M',M)
# print('L',L)

# -*- coding: utf-8 -*-

def trim(s):
    if s[:1] != ' ' and s[-1:] != ' ':
        return s
    elif s[:1] == ' ':
        return trim(s[1:])
    else:
        return trim(s[:-1])




def test():
    if trim('hello  ') != 'hello':
        print('1测试失败!')
    elif trim('  hello') != 'hello':
        print('2测试失败!')
    elif trim('  hello  ') != 'hello':
        print('3测试失败!')
    elif trim('  hello  world  ') != 'hello  world':
        print('4测试失败!')
    elif trim('') != '':
        print('5测试失败!')
    elif trim('    ') != '':
        print('6测试失败!')
    else:
        print('测试成功!')

test()