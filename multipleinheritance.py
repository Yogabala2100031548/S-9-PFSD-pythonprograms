class Base1:
    def fun1(self):
        print("1")
class Base2:
    def fun2(self):
        print("2")
class Base3:
    def fun3(self):
        print("3")
class Derived(Base1,Base2,Base3):
    def fun4(self):
        print("4")
obj=Derived()
obj.fun4()
obj.fun3()
obj.fun2()
obj.fun1()