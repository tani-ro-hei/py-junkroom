# クラスデコレータのお勉強


# 1) 継承による方法

class MoneyThrowable():

    def __init__(self, money=0):
        self.money = money

    def throw_money(self, money):
        if type(money) != int:
            raise TypeError("<{}>: 金ではありません！".format(money))
        self.money += money

        import inspect
        caller = inspect.stack()[1].function
        print(f"視聴者の{caller}さんから{money}円いただきました、"
            "どうもありがとうございます！")

    def mymoney(self):
        print(f"所持金は{self.money}円です。")


class TestClass1(MoneyThrowable):

    def __init__(self, money=0):
        super().__init__(money)
        self.money += 300  # 最初の所持金は＋300円になる


t1 = TestClass1(money=1000)
t1.mymoney()         #=> 所持金は1300円です。
t1.throw_money(100)  #=> 視聴者の<module>さんから100円いただきました、どうもありがとうございます！
t1.mymoney()         #=> 所持金は1400円です。


# 2) クラスデコレータによる方法(そんな方法はないが)

def money_throwable(cls):
    # 面倒なので、再利用してそのまま代入した
    cls.throw_money = MoneyThrowable.throw_money
    cls.mymoney     = MoneyThrowable.mymoney

    return cls


@money_throwable
class TestClass2():

    def __init__(self, money):
        self.money = money - 100  # 最初の所持金は－100円になる


t2 = TestClass2(money=10000)
t2.mymoney()         #=> 所持金は9900円です。
t2.throw_money(500)  #=> 視聴者の<module>さんから500円いただきました、どうもありがとうございます！
t2.mymoney()         #=> 所持金は10400円です。

t2.throw_money('x')  #=> ... TypeError: <x>: 金ではありません！
