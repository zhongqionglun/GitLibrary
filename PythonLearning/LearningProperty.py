# -*-coding:UTF-8-*-

"""
    装饰器-对类属性的访问-使用@property (用于属性读取)and @xxx.setter（用于属性设置）
"""


class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError("the width must integer!")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError("the height must integer!")
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height


if __name__ == "__main__":
    s = Screen()
    s._width = 1024
    s._height = 768
    print('resolution = %s' % s.resolution)
    if s.resolution == 786432:
        print("测试通过！")
    else:
        print("测试不通过！")
