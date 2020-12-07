你可以使用issubclass()或者isinstance()方法来检测。
issubclass() - 布尔函数判断一个类是另一个类的子类或者子孙类，语法：issubclass(sub,sup)
-----------------------------------------------------------------------------------
# 定义父类
class Parent:
    pass


# 定义子类
class Child(Parent):
    pass


# 判断
vr = issubclass(Child, Parent)
print("\n\nissubclass(Child, Parent):", vr)

=================================================================================
isinstance(obj, Class) 布尔函数如果obj是Class类的实例对象或者是一个Class子类的实例对象则返回true。
----------------------------------------------------------------------------------
# 定义类
class MyClass:
    pass


# 定义类实例
myIns = MyClass()
# 判断
vr = isinstance(myIns, MyClass)
print("\n\nisinstance(myIns, MyClass):", vr)
