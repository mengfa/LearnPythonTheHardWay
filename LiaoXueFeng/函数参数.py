# _*_ coding: utf-8 _*_
__author__ = 'lv'
__date__ = '2018/1/25 18:02'
# 练习
#
# 以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：

def product(*args):
    if args is None or len(args) <= 0:
        raise TypeError("args not null!")
    sum = 1
    for s in args:
        sum = s* sum

    return sum


# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('1测试失败!')
elif product(5, 6) != 30:
    print('2测试失败!')
elif product(5, 6, 7) != 210:
    print('3测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('4测试失败!')
else:
    try:
        product()
        print('5测试失败!')
    except TypeError:
        print('测试成功!')