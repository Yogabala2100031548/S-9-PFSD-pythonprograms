class Base:
    def fun1(self):
        print("hello")
class derived1(Base):
    def fun2(self):
        print("This is pfsd")
class derived2(derived1):
    def fun3(self):
        print("class")
obj=derived2()
obj.fun1()
obj.fun2()
obj.fun3()