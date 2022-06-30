#!/usr/bin/python3
# auther@hy
# 2022年06月24日
class Open_File(object):
    """
    自定义实现open
    """
    def __init__(self,filename,mode):
        self.filename = filename
        self.mode = mode
    def __enter__(self):
        # 上下文进入
        self.f = open(self.filename,mode=self.mode,encoding='utf8')
        return self.f
    def __exit__(self, exc_type, exc_val, exc_tb):
        # 退出
        print("exit")
        self.f.close()
with Open_File('file','w') as f:
    f.write('hello python')