# クラスデコレータのお勉強


# 1) 継承による方法

class MoneyThrowable():

    def __init__(self):
        self.money = 1000  # 最初の所持金

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

    def __init__(self):
        super().__init__()
        self.money += 300  # 最初の所持金は1300円になる

t1 = TestClass1()
t1.throw_money(100)  #=> 視聴者の<module>さんから100円いただきました、どうもありがとうございます！
t1.mymoney()         #=> 所持金は1400円です。


# 2) クラスデコレータによる方法

def money_throwable(cls):
    # 面倒なので再利用してそのまま代入した
    cls.throw_money = MoneyThrowable.throw_money
    cls.mymoney     = MoneyThrowable.mymoney

    return cls

@money_throwable
class TestClass2():

    def __init__(self):
        self.money = 10000

t2 = TestClass2()
t2.throw_money(500)  #=> 視聴者の<module>さんから500円いただきました、どうもありがとうございます！
t2.mymoney()         #=> 所持金は10500円です。
