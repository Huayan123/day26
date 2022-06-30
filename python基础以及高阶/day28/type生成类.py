#!/usr/bin/python3
# auther@hy
# 2022年06月30日
# 生成Test类
Test = type('Test',(),{})
print(Test)
print("-"*50)
Foo = type('Test1',(),{'bar':True})
print(Foo.bar)
print(Foo)
print("-"*50)
def echo_bar(self):
    print(self.bar)
Foo_child = type('Foo_child',(Foo,),{'echo_bar':echo_bar})
print(hasattr(Foo_child,'bar'))
print("-"*50)
f1 = Foo_child()
f1.echo_bar()
print("-"*50)
# 静态变量
@classmethod
def test_static():
    print('static bar.....')
@classmethod
def test_class(cls):
    print("*"*50)
    print(cls.bar)
FooChild = type('FooChild',(Foo,),{'echo_bar':echo_bar,'test_static':test_static,'test_class':test_class})
f2 = FooChild()
f2.test_class()