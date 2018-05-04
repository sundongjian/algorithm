'''
抽象数据类型:设计和实现程序模块的技术
定义一个抽象数据目的是定义一类计算对昂
抽象数据的基本思想是把数据定义为抽象数据的集合，一个数据类型通常有三种操作，构造，解析，变动
构造：
解析：从一个对象取得有用的信息,如属性，或者创造方法
改变：修改操作对象的内部状态
抽象数据访问两个对象并进行运算，最后将运算结果传入，再构造对象返回
'''


class Rational:
    @staticmethod
    def _gcd(m, n):  # 求最大公约数
        if n == 0:
            m, n = n, m
        while m != 0:
            m, n = n % m, m
        return n

    def __init__(self, num, den=1):
        if not isinstance(num, int) or not isinstance(den, int):  # 所有输入的函数都要有判断类型，判空操作
            raise TypeError
        if den == 0:
            raise ZeroDivisionError
        sign = 1
        if num < 0:
            num, sign = -num, -sign
        if den < 0:
            den, sign = -den, -sign
        g = Rational._gcd(num, den)
        self.num = sign * (num // g)
        self.den = den // g

    def __add__(self, another):
        den = self.den * another.den
        num = (self.num * another.den + self.den * another.num)
        return Rational(den, num)

    def __mul__(self, another):
        return Rational(self.num * another.num, self.den * another.den)

    def __floordiv__(self, another):
        if another.num == 0:
            raise ZeroDivisionError
        return Rational(self.num * another.den, self.den * another.num)

    def __eq__(self, another):
        return self.num * another.den == self.den * another.num

    def __lt__(self, another):
        return self.num * another.den < self.den * another.num

    def __gt__(self, another):
        return self.num * another.den > self.den * another.num

    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    def print(self):
        print(str(self.num) + '/' + str(self.den))


'''
书中将den，num设置为私有变量，然而使用了another.den()，这意味着还要加一个无意义的den（）方法，
所以这里统一用属性，但是要记住设置为私有变量思想是没错的，能不暴露就不暴露内部数据，这样外部就不能直接通过属性赋值改变值
'''
