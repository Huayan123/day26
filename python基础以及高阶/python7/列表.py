#!/usr/bin/python3
# auther@hy
# 2022年06月06日
list1 = [1,2,3,4,5]
name_list = ["zhangsan", "lisi", "wangwu"]
name_list.append('liuneng')
# name_list.remove('zhangsan')
# name_list.pop(2)
# name_list.clear()
# print(name_list.index('lisi'))
# print(len(name_list))
# # print(name_list.sort())
# print(name_list)
# for i in name_list:
#     print(i)
# set1=(1,2,3,5,6,1)
# print(set1.index(5))
# print(set1.count(1))
#
# info_tuple = ('xiaoming',20,1.81)
# str = "%s 的年龄是 %d，身高是%.2f米" %(info_tuple)
# print(str)
# print(type(set1))
# a = [x if x%2==0 else x**2 for x in range(10)]
# print(a)
# b = [x for x in range(0,10) if x%2==0]
# print(b)
xiaoming = {"name": "小明",
"age": 18,
"gender": True,
"height": 1.75}
# print(xiaoming['age'])
xiaoming.pop('gender')
dict2 = {'name':'王五',
         'age':'20',
         'gender':'男',
         'height':'140'}
# print(xiaoming.get('name'))
# xiaoming.update(dict2)
# for i in xiaoming.items():
#     print(i)
# xiaoming.fromkeys()
#
string = ' Hello python\r\n' \
          ' Hello world! '
# print(string.strip(" "))
# print("-"*50)
# print(string.splitlines())
# string.replace('Hello python ','hello python')
# print(string)
#
#
# print("-"*50)
# fruits = {"apple", "banana", "cherry"}
# fruits.add("orange")
# print(fruits)
# print('-'*50)
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# x.update(y)
# print(x)
# print(string.find(" Hello"))
# print("-"*50)
# poem = ["\t\n 登鹳雀楼",
# "王之涣",
# "白日依山尽\t\n",
# "黄河入海流",
# "欲穷千里目",
# "更上一层楼"]
# for item in poem:
#     print(item.strip().center(6," "))
# print("-"*60)
# poem_list = "登鹳雀楼\t 王之涣 \t 白日依山尽 \t \n 黄河入海流 \t\t 欲穷千里目 \t\t\n 更上一层楼"
# poem_list.split()
# set =[0]*20
# print(set)
def measure():
    """返回当前的温度"""
    print("开始测量...")
    temp = 39
    wetness = 10
    print("测量结束...")
    return temp,wetness
res = temp,wetmess = measure()
print(res)