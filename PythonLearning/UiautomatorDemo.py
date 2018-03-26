# -*-coding:UTF-8-*-

from uiautomator import device as d
import time, random
import unittest


class My_Test_Suite(unittest.TestCase):
    def setUp(self):
        try:
            d.press.home()
            d(text="***").click()
            time.sleep(2)
            if d(text="我的").exists:
                d(text="我的").click()
                d(text="注销").click()
                d(text="确定").click()
            if d(text="登录").exists:
                d(resourceId="com.isentech.attendance:id/title_back").click()
            else:
                time.sleep(3)
            print(u"打开APP")
        except Exception as e:
            print(u"Error: 打开APP失败！\n", e)

    def test_reg(self):
        pass

    def tearDown(self):
        try:
            d.press.home()
            d.press.recent()
            time.sleep(3)
            d.swipe(200, 500, 200, 0, steps=10)
            d.press.home()
            print(u"关闭APP")
        except Exception as e:
            print(u"Error: 关闭APP失败！ \n", e)


if __name__ == "__main__":
    phone_number = random.choice(['139', '188', '185', '136', '158', '151']) + "".join(
        random.choice("0123456789") for i in range(8))
    unittest.main()
