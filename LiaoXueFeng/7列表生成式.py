# _*_ coding: utf-8 _*_
__author__ = 'lv'
__date__ = '2018/1/25 18:49'
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x,str)]


# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')