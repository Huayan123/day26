# !/usr/bin/python3
# auther@hy
# 2022年06月08日
# 通过try进行异常捕捉，确保输入的内容一定是一个整型数，然后判断该整型数是否是对称数，12321就是对称数，123321也是对称数，否则就不是，非整型抛异常，非对称数抛不抛异常自行选择1、	通过try进行异常捕捉，确保输入的内容一定是一个整型数，然后判断该整型数是否是对称数，12321就是对称数，123321也是对称数，否则就不是，非整型抛异常，非对称数抛不抛异常自行选择
def zhengshu():
    try:
        num = int(input("输入一个整型数："))
        return num
    except ValueError:
        print("输入正确的整数!")

def Judge():
    res = zhengshu()
    list1 = []
    t =res
    while(t):
        tem = t%10
        list1.append(tem)
        t //= 10
    n = len(list1)
    for i in range(0,n//2-1):
        j = n-1
        if(list1[i]==list1[j]&j>i):
            j-=1
        else:
            ex = Exception("此数非对称数!")
            raise ex
    return res

try:
    print(Judge())
except Exception as e:
    print(e)
