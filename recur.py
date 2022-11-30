# 再帰関数とクラス内再帰のお勉強

def factorial_A(dmy, x):
    if x == 0:
        return 1
    else:
        return x * factorial_A(dmy, x - 1)

print(factorial_A(..., 25))
r""" => 普通の再帰関数
15511210043330985984000000
"""

class TestClass_B:

    def __init__(self):
        pass

    def factorial_B(self, x):
        if x == 0:
            return 1
        else:
            return x * self.factorial_B(x - 1)

    def print(self, x):
        print(self.factorial_B(x))

tesB = TestClass_B()
tesB.print(25)
r""" => 多分これが正しいクラス内再帰
15511210043330985984000000
"""

class TestClass_C:

    def __init__(self):
        pass

    # 形式は factorial_A とまったく同じだが...
    def factorial_C(self, x):
        if x == 0:
            return 1
        else:
            return x * factorial_C(self, x - 1)

    def print(self, x):
        print(factorial_C(self, x))

tesC = TestClass_C()
tesC.print(25)
r""" => エラー
Traceback (most recent call last):
  File "C:\Users\Taniguchi\recur.py", line 49, in <module>
    tesC.print(25)
  File "C:\Users\Taniguchi\recur.py", line 46, in print
    print(factorial_C(self, x))
          ^^^^^^^^^^^
NameError: name 'factorial_C' is not defined. Did you mean: 'factorial_A'?
"""
