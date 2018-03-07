# -*-coding:UTF-8-*-

from abc import ABCMeta, abstractmethod

class Super(metaclass=ABCMeta):
    def delegate(self):
        self.action()
    @abstractmethod
    def action(self):
        pass

if __name__ == "__main__":
    try:
        x = Super()
    except TypeError:
        print("catch the \"TypeError\" exception!")

    class Sub1(Super): pass
    try:
        x = Sub1()
    except TypeError:
        print("catch the \"TypeError\" exception!")

    class Sub2(Super):
        def action(self): print('abstract method have defined!')
    ax = Sub2()
    ax.delegate()
