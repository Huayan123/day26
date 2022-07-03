#!/usr/bin/python3
# auther@hy
# 2022年07月01日
class Alipay:
    def paying(self,money):
        print('支付宝支付了')
class Apppay:
    def pay(self,money):
        print('苹果支付了')
class Weicht:
    def pay(self,money):
        print('微信支付了')
def Pay(payment,money):
    payment.pay(money)
# p中未实现pay方法
p = Alipay()
pay(p,200)


