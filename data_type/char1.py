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
        if not 