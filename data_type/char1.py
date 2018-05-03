'''
抽象数据的基本思想是把数据定义为抽象数据的集合，一个数据类型通常有三种操作，构造，解析，变动
构造：
解析：从一个对象取得有用的信息
改变：修改操作对象的内部状态
'''

class Rational:
    @staticmethod
    def _gcd(m,n):
        if n==0:
            m,n=n,m
        while m !=0:
            m,n=n%m,m
        return n

    def __init__(self,num,den=1):
        if not isinstance(num,int) or not isinstance(den,int)
            raise TypeError
        if den==0:
            raise ZeroDivisionError
        sign=1
        if num <0:
            num,sign=-num,-sign
        if den<0:
            den,sign=-den,-sign
        g=Rational._gcd(num,den)
        self.num=sign*(num//g)
        self.den=den//g

    def __add__(self,anthoer):