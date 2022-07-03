#!/usr/bin/python3
# auther@hy
# 2022年07月01日
# 元类的父类实现
class MetaClass(type):
    def __new__(cls,class_name,class_parents,class_attr:dict):
        mapping = dict()
        for key,value in class_attr.items():
            if(isinstance(value,tuple)):
                print('Found mapping: %s ==> %s' % (key, value))
                mapping[key]=value
        for value in mapping.keys():
            class_attr.pop(value)
        class_attr['__mapping__'] = mapping
        class_attr['__table__']=class_name
        return type.__new__(cls,class_name,class_parents,class_attr)
class Model(object,metaclass=MetaClass):
    """
    元类的实现，创建User类时改变
    """
    # 设置类的attr属性
    def __init__(self,**kwargs):
        for value,name in kwargs.items():
            setattr(self,value,name)
    def save(self):
        n = []
        v = []
        for name,value in self.__mapping__.items():
            n.append(value[0])
            # 判断能否拿到User的属性
            v.append(getattr(self,name,None))
            sql = 'insert into %s (%s) values (%s)'%(self.__table__,','.join(n),','.join(["'"+i+"'"if isinstance(i,str) else str(i) for i in v]))
        print(sql)
class User(Model):
    uid = ('uid', "int unsigned")
    name = ('username', "varchar(30)")
    email = ('email', "varchar(30)")
    password = ('password', "varchar(30)")
u = User(uid=12345, name='Michael', email='test@orm.org', password='my-pwd')
u.save()