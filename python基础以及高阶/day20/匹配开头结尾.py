#!/usr/bin/python3
# auther@hy
# 2022年06月21日
import re
# 分组起别名，通过别名来引用分组
# email_list = ["xiaoWang@163.com","xiao.Wang@163.com", "xiaoWang@163.comheihei", ".com.xiaowang@qq.com"]
# for email in email_list:
#     ret = re.match('\w{4,20}@163\.com$',email)
#     if ret:
#         print(ret.group())
#     else: print("不符合.....")
#
# # 匹配数字100
# print("-"*50)
# ret = re.match(r'[1-9]?\d$|100$','100')
# print(ret.group())
#
# # 提取区号和电话号码
# print("-"*50)
# ret = re.match(r'([^-]+)-(\d+)','010-8776374')
# if ret:
#     print(ret.group(1))

print("-" * 50)
s="This is a number 234-235-22-423"
ret = re.match(r'.+?(\d+-\d+-\d+-\d+)',s)
print(ret.group())
print("-" * 50)

# 贪婪和非贪婪
ret = re.match(r'aa(\d+)','aa2343ddd')
print(ret.group())
ret = re.match(r'aa(\d+?)','aa2343ddd')
print("-" * 50)
print(ret.group())
ret1 = re.match('aa(\d+?)ddd','aa2343ddd')
ret2 = re.match('aa(\d+)ddd','aa2343ddd')
print(ret1.group())
print(ret2.group())

print("-" * 50)

s = """
dadad
dadda
4353545
"""
for item in s.splitlines():
    ret = re.match('(\w|\d)*',item)
    print(ret.group())