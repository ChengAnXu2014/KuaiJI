《《类》》
《《class》》
------------------------------------

# 类的定义格式;类名首字母必须大写.
class Students:
    # 类变量在类体中、类方法外定义.
    # 类变量会被类的所有实例继承,也可以被类的所有实例访问.
    stuCount = 0

    # __init__(self)为类构建(初始化)方法,在实例化类时自动调用,不被实例继承.
    # __init__(self)方法也可以省略,缺省时会由默认的,只传递self参数的__init__(self)方法替补.
    def __init__(self, name, score):
        # 实例变量只能在构建(初始化)方法内,用"self参数.实例变量名=值"的格式定义,如下.
        self.name = name
        self.score = score

        # 在类方法中访问类变量时,必须用"类名.类变量名"的格式(如:Students.stuCount).
        Students.stuCount += 1

    # 类的所有方法(包括构建(初始化)方法__init__())定义时,第一个参数都必须保留,惯例为"self",当然也可以用其它名称代替.
    # self参数用于代指调用该方法的类实例,因为类定义时肯定还未实例化,所以在定义中只能用self参数来指代类实例.
    # self参数只在定义方法时需要,调用方法时不能有.
    def display(self):
        print("name:", self.name, "score:", self.score)


# 类实例化的语法为:"实例名=类名(参数列表)"如下.
# 类实例化会自动调用类构建(初始化)方法__init__().
# 类实例化时所带的参数会传给构建(初始化)方法__init__().
# 类实例化时不能有self参数, 类似"ao = Students(self,"Aoi",99)"这样的语句是错误的.
ao = Students("Aoi", 99)
so = Students("Sola", 89)
li = Students("李丽珍", 100)

# 调用类方法时不能有self参数. li.display(self)这样的语句是错误的.
print("li.display():")
li.display()
print("\n")

# 在类外访问类变量时,必须用"类名.类变量名"的格式(如:Students.stuCount).
print("Students.stuCount:", Students.stuCount)

# 在类外访问实例变量时,必须用"实例名.实例变量名"的格式,如下.
print("li.name:", li.name)

# 实例继承自类变量的变量,为实例变量.如下面三个变量为各自实例的实例变量,并不是Students类的类变量.
print("ao.stuCount:", ao.stuCount)
print("so.stuCount:", so.stuCount)
print("li.stuCount:", li.stuCount)
print("\n")

# 类变量的值改变时,所有继承自该类变量的实例变量的值也会眼着改变,如下.
Students.stuCount = 9
print("类变量 Students.stuCount 重新赋值为9后:")
print("ao.stuCount:", ao.stuCount)
print("so.stuCount:", so.stuCount)
print("li.stuCount:", li.stuCount)
print("\n")

# 实例变量的值改变时,不会影响其所继承的类变量或与其继承自同一类变量的其它实例变量的值,如下.
li.stuCount = 5
print("实例变量 li.stuCount 重新赋值为5后:")
print("ao.stuCount:", ao.stuCount)
print("so.stuCount:", so.stuCount)
print("li.stuCount:", li.stuCount)
print("\n")

=======================================================================
可以用 del 关键字删除属性.