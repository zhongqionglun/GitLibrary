# -*-coding:UTF-8-*-

"""
auth:zhongqionglun
time:
description:该段代码演示了斐波拉契生成器
"""


def fib(n):
    a, b = 0, 1
    while b < n:
        yield a
        a, b = b, a + b


for n in fib(200):
    print(n, end=' ')
