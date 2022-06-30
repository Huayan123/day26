#!/usr/bin/python3
# auther@hy
# 2022年06月28日
x = 200
def test(num1):
    x = 100
    print(x)
    def test_print_in(num2):
        print(x)
        print("num1+num2=%d"%(num1+num2))
    return test_print_in
if __name__ == '__main__':
    ret = test(100)
    ret(100)
