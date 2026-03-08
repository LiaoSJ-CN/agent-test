"""
理解变量和类型

Version: 1.0
Author: LiaoSJ-CN
"""
print(0b100)  # 二进制整数
print(0o100)  # 八进制整数
print(100)    # 十进制整数
print(0x100)  # 十六进制整数
print(123.456)    # 数学写法
print(1.23456e2)  # 科学计数法

"""
使用变量保存数据并进行加减乘除运算

Version: 1.0
Author: LiaoSJ-CN
"""
a = 45        # 定义变量a，赋值45
b = 12        # 定义变量b，赋值12
print(a, b)   # 45 12
print(a + b)  # 57
print(a - b)  # 33
print(a * b)  # 540
print(a / b)  # 3.75

"""
使用type函数检查变量的类型

Version: 1.0
Author: LiaoSJ-CN
"""
c = 100
d = 123.45
e = 'hello, world'
f = True
print(type(c))  # <class 'int'>
print(type(d))  # <class 'float'>
print(type(e))  # <class 'str'>
print(type(f))  # <class 'bool'>

"""
变量的类型转换操作

Version: 1.0
Author: LiaoSJ-CN
"""
a1 = 100
a2 = 123.45
a3 = '123'
a4= '100'
a5 = '123.45'
a6 = 'hello, world'
a7 = True
print(float(a1))         # int类型的100转成float，输出100.0
print(int(a2))           # float类型的123.45转成int，输出123
print(int(a3))           # str类型的'123'转成int，输出123
print(int(a3, base=16))  # str类型的'123'按十六进制转成int，输出291
print(int(a4, base=2))   # str类型的'100'按二进制转成int，输出4
print(float(a5))         # str类型的'123.45'转成float，输出123.45
print(bool(a6))          # str类型的'hello, world'转成bool，输出True
print(int(a7))           # bool类型的True转成int，输出1
print(chr(a1))           # int类型的100转成str，输出'd'