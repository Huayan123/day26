#!/usr/bin/python3
# auther@hy
# 2022年06月08日
class A():
    def test(self):
        print("A test")
    def demo(self):
        print("A demo")
class B():
    def test(self):
        print("B test")
    def demo(self):
        print('B demo')
    def test2(self):
        print('B test2')
class C(A,B):
    """
    父类重写
    """
    def demo(self):
        print("C demo")
c = C()
c.test2()
# 先找自己的，再找顺序第一个父类的
c.demo()