# name mangling のお勉強

class Test():
    var1        = "var1!"
    _var2       = "var2!"
    __var3      = "var3!"
    _Test__var3 = "var3(上書き)!"
    __var4_     = "var4!"
    __var5__    = "var5!"
    _Test__var6 = "var6!"
    print(
        'var1        = "var1!"\n'
        '_var2       = "var2!"\n'
        '__var3      = "var3!"\n'
        '_Test__var3 = "var3(上書き)!"\n'
        '__var4_     = "var4!"\n'
        '__var5__    = "var5!"\n'
        '_Test__var6 = "var6!"\n'
    )

    def __init__(self):
        pass

def print_dir_Test():
    print(list(filter(lambda name: "var" in name, dir(Test))), "\n")


t = Test()
print_dir_Test()

print("t.var1:",        t.var1)         #=> var1!
print("t._var2:",       t._var2)        #=> var2!
#print("t.__var3:",     t.__var3)       # (err)
print("t._Test__var3:", t._Test__var3)  #=> var3(上書き)!
#print("t.__var4_:",    t.__var4_)      # (err)
print("t.__var5__:",    t.__var5__)     #=> var5!
print("t._Test__var6:", t._Test__var6)  #=> var6!

t.__var3 = "var3(代入)!"  # インスタンス変数に代入される
print('\n>>> t.__var3 = "var3(代入)!"\n')
print_dir_Test()
print("t.__var3 (インスタンス変数):", t.__var3)      #=> var3(代入)!
print("t._Test__var3 (クラス変数):", t._Test__var3)  #=> var3(上書き)!

t._Test__var3 = "var3(上書き2回目)!"
print('\n>>> t._Test__var3 = "var3(上書き2回目)!"\n')
print("t._Test__var3:", t._Test__var3)  #=> var3(上書き2回目)!
