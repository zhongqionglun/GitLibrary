# -*-coding:UTF-8-*

"""
def MyFilter(x): filter the prime :NOT odd NOT even   非奇非偶
def MyCube(x): x*x*x
def MyAdd(x): addition
"""


def MyFilter(x): return x % 2 != 0 and x % 3 != 0


def MyCube(x): return x * x * x


def MyAdd(x, y): return x + y


# 列表函数
print(filter(MyFilter, range(2, 25)))
print(map(MyCube, range(1, 11)))
print(reduce(MyAdd, range(1, 11)))
print(__doc__)
