#!/usr/bin/python3
# auther@hy
# 2022年06月21日
# 匹配由单个逗号和单个空白符分隔的任何单词和单个字母,如姓氏的首字母，如L,smith，或者L smith（内容自设）
import re
from tld import get_tld
ret = re.match(r'(\w+),(\w+)','L,smith')
print(ret.group(1))
print("-"*50)
# 匹配以“www”起始且以“.com”结尾的简单Web域名:例如,http://www.yahoo.com ，也支持其他域名，如.edu .net等（内容自设）
list_www = ['http://www.yahoo.com','http://www.yahoo.edu','http://www.yahoo.net']
for item in list_www:
        ret = re.match(r'([^/]+)./(.*(com|edu|net))$',item)
        print(ret.group(2))
str = """
dadadad
23422
ddad232425eee2e3edafa@163.com
fa2324
/./984242joj^43%2$^&*
"""
for sub_str in str.splitlines():
        ret = re.sub(r'2\w+@163\.com$',r'huayan_97@163.com',sub_str)
        print(ret)
http_list="""http://www.interoem.com/messageinfo.asp?id=35`
http://3995503.com/class/class09/news_show.asp?id=14
http://lib.wzmc.edu.cn/news/onews.asp?id=769
http://www.zy-ls.com/alfx.asp?newsid=377&id=6
http://www.fincm.com/newslist.asp?id=415
"""
for lines in http_list.splitlines():
        ret =re.split(r'/',lines)
        print(ret[2])
