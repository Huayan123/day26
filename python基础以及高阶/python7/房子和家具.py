#!/usr/bin/python3
# auther@hy
# 2022年06月08日

class Jiaju():
    """
    家具类
    """
    def __init__(self,name,area):
        self.name = name
        self.area = area
    def __str__(self):
        return "[%s] 占地 is %.02f"%(self.name,self.area)
bed = Jiaju("床",4)
chest = Jiaju("衣柜",1.5)
table = Jiaju("桌子",1.0)
print(bed)
print(chest)
print(table)
print("-"*50)

class House(Jiaju):
    def __init__(self,house_type,area):
        # 家的类型
        self.house_type = house_type
        # 房间面积
        self.area = area
        # 房间剩余面积
        self.free_area = area
        # 家具列表
        self.item_list = []
        # 对类的说明，可以通过print打印，必须有个返回类型
    def __str__(self):
        return ("户型:%s\n [总面积:%.2f][剩余：%.2f]\n家具：%s\n" %(self.house_type,self.area,self.free_area,self.item_list))
    def add(self,jiaju:Jiaju):
        print("添加%s"%jiaju)
        if(self.free_area < jiaju.area):
            print("房间面积不够!")
        self.item_list.append(jiaju.name)
        self.free_area -= jiaju.area

my_home = House("两室一厅",60)
my_home.add(bed)
my_home.add(chest)
my_home.add(table)
print(my_home)