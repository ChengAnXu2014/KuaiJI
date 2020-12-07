算术；比较；赋值；位；逻辑；成员；身份；优先级
================================================================================
《算术运算符》
----------------
以下假设变量： a=20，b=10：
-------------------------------------------------------------------------
运算符____描述____________________________________________实例

+_________两个对象相加____________________________________a + b 输出结果 30

-_________减 - 得到负数或是一个数减去另一个数______________a - b 输出结果 -10

*_________乘 - 两个数相乘或是返回一个被重复若干次的字符串___a * b 输出结果 200

/_________除 - x除以y______________________________________a / b 输出结果 2

%_________取模 - 返回除法的余数_____________________________a % b 输出结果 0

**________幂 - 返回x的y次幂_____________________________a**b=10240000000000

//________取整除 - 返回商的整数部分（向下取整）______________9//2=4  -9//2=-5
--------------------------------------------------------------------------
a, b = 10, 3
print(a % b, a // b, a ** b, )

================================================================================



================================================================================
《比较运算符》
-------------------
以下假设变量a为10，变量b为20：
--------------------------------
运算符__描述______________________________实例
------------------------------------------------------------
==______等于 - 比较对象是否相等____________(a == b) 返回 False
------------------------------------------------------------
!=______不等于 - 比较两个对象是否不相等_____(a != b) 返回 true
------------------------------------------------------------
>_______大于 - 返回x是否大于y______________(a > b) 返回 False
------------------------------------------------------------
<_______小于 - 返回x是否小于y。所有比较
________运算符返回1表示真，返回0表示假。
________这分别与特殊的变量True和False等价.__(a < b) 返回 true
------------------------------------------------------------
>=______大于等于 - 返回x是否大于等于y。______(a >= b) 返回 False
------------------------------------------------------------
<=______小于等于 - 返回x是否小于等于y。______(a <= b) 返回 true

================================================================================



================================================================================
《赋值运算符》
-------------------
以下假设变量a为10，变量b为20：
---------------------------------------
运算符__描述____________________________________ 实例
------------------------------------------------------------
=_______简单的赋值运算符____c = a + b 将 a + b 的运算结果赋值给c
------------------------------------------------------------
+=______加法赋值运算符______c += a 等效于 c = c + a
------------------------------------------------------------
-=______减法赋值运算符______c -= a 等效于 c = c - a
------------------------------------------------------------
*=______乘法赋值运算符______c *= a 等效于 c = c * a
------------------------------------------------------------
/=______除法赋值运算符______c /= a 等效于 c = c / a
------------------------------------------------------------
%=______取模赋值运算符______c %= a 等效于 c = c % a
------------------------------------------------------------
//=_____取整除赋值运算符____c //= a 等效于 c = c // a
------------------------------------------------------------
**=_____幂赋值运算符________c **= a 等效于 c = c ** a
------------------------------------------------------------
a, b = 10, 20
a += b
print(a)
a = 10
a -= b
print(a)
a = 10
a *= b
print(a)
a = 10
a /= b
print(a)
a = 10
a %= b
print(a)
a = 10
a //= b
print(a)
a = 10
a **= b
print(a)

================================================================================



================================================================================
《位运算符》
--------------------------
a = 0b10101
b = 0b01010
c = 0b11111
d = 0b00000
print(a, b, c, d)
print("&:", a & c, a & d)
print("|:", a | c, a | d)
print("^:", a ^ c, a ^ d)
print("~:", ~a, ~b)
print("0b1111100:", 0b1111100)
print("c<<2:", c << 2)
print("0b111:", 0b111)
print("c>>2:", c >> 2)

================================================================================



================================================================================
《逻辑运算符》
--------------
a=10,b=20
--------------------------------------
运算符
逻辑表达式
描述
实例
-----------------------------------------------------------------------------
and
x and y
布尔"与";如果 x 为 False,x and y 返回 False;否则它返回 y 的值。
(a and b) 返回 20
------------------------------------------------------------------------------
or
x or y
布尔"或";如果 x 是非 0，它返回 x 的值;否则它返回 y 的计算值。
(a or b) 返回 10
------------------------------------------------------------------------------
not
not x
布尔"非" - 如果 x 为 True，返回 False; 如果 x 为 False，它返回 True。
not(a and b) 返回 False
---------------------------------------------------------------
if True and False:
    print("if True and False")
else:
    print("else True and False")

if True and True:
    print("if True and True")
else:
    print("else True and True")

if True or False:
    print("if True or False")
else:
    print("else True or False")

if False or False:
    print("if False or False")
else:
    print("else False or False")

if not True:
    print("if not True")
else:
    print("else not True")

if not False:
    print("if not False")
else:
    print("else not False")

================================================================================



================================================================================
《成员运算符》
----------------------------------------------------------
运算符__描述_________________________________________________实例
------------------------------------------------------------
in______如果在指定的序列中找到值返回 True，否则返回 False。______x in y

------------------------------------------------------------
not in__如果在指定的序列中没有找到值返回 True，否则返回 False。__x not in

--------------------------------------------------------------------
students = ("小明", "李华", "小强", "婷婷", "兰兰")
if "小明" in students:
    print("if 小明 in students")
else:
    print("else 小明 in students")

if "小明" not in students:
    print("if 小明 not in students")
else:
    print("else 小明 not in students")

if "刘玥" in students:
    print("if 刘玥 in students")
else:
    print("else 刘玥 in students")

if "刘玥" not in students:
    print("if 刘玥 not in students")
else:
    print("else 刘玥 not in students")

================================================================================



================================================================================
《身份运算符》
--------------------------------------------------------------------------
运算符
描述
实例
--------------------------------------------------------------------------------
is
判断两个标识符是不是引用自一个对象;是同一个对象则返回 True,否则返回 False
x is y, 类似 id(x) == id(y)
---------------------------------------------------------------------------------
is not
判断两个标识符是不是引用自不同对象;不是同一个对象则返回 True，否则返回 False。
x is not y, 类似 id(a) != id(b)。
---------------------------------------------------------------------------------
PS：有些内存管理优化得比较好的解释器，会把初始化值相同的多个变量标识符指向同一个对象。
    如果后续有些变量标识符被重新赋予不同的值，则会重新为其分配新的对象。
    同样的，如果某些原本值不同的变量被重新赋予相同的值，它们就会被重定向到相同的对象——如果已经存在值与它们的新值相同的对象，就会把它们重定向到该对象；如果没有，则为它们重新分配对象——原先的对象则会被销毁。
    因此身份运算符在大多数情况下，表现得和比较运算符没什么不同。
    然而，仍会有某些特殊情况会导致出现多个值相同的对象。所以不要想当然的以为：值相同的变量标识符就一定会指向相同的对象。一定要用身份运算符进行确认。
-----------------------------
a = 99
b = 99
print("初始化：a=99;b=99")
if a is b:
    print("if a is b")
else:
    print("else a is b")

if a is not b:
    print("if a is not b")
else:
    print("else a is not b")

a = 9
print("重新赋值：a=9")
if a is b:
    print("if a is b")
else:
    print("else a is b")

if a is not b:
    print("if a is not b")
else:
    print("else a is not b")

a = 99
print("又重新赋值：a=99")
if a is b:
    print("if a is b")
else:
    print("else a is b")

if a is not b:
    print("if a is not b")
else:
    print("else a is not b")

================================================================================
c = "aaa"
d = "aaa"
print("初始化：c=\"aaa\";d=\"aaa\"")
if c is d:
    print("if c is d")
else:
    print("else c is d")

if c is not d:
    print("if c is not d")
else:
    print("else c is not d")

c = "bbbaaa"
print("重新赋值：c=\"bbbaaa\"")
if c is d:
    print("if c is d")
else:
    print("else c is d")

if c is not d:
    print("if c is not d")
else:
    print("else c is not d")

c = "aaa"
print("又重新赋值：c=\"aaa\"")
if c is d:
    print("if c is d")
else:
    print("else c is d")

if c is not d:
    print("if c is not d")
else:
    print("else c is not d")

================================================================================



================================================================================
《运算符优先级》
-------------------------------
**(最高优先级)
-------------------------------
~   +(正号)   -(负号)
-------------------------------
*   /   %   //
-------------------------------
+(加)   -(减)
-------------------------------
>>   <<
-------------------------------
&
-------------------------------
^   |
-------------------------------
<=   <   >   >=
-------------------------------
==   !=
-------------------------------
=   %=   /=   //=   -=   +=   *=   **=
-------------------------------
is   is not
-------------------------------
in   not in
-------------------------------
not   and   or
-------------------------------

================================================================================



================================================================================