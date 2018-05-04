'''
一个实例对象可以像其他对象一样赋值给变量做参考值，或者穿个函数处理，或者作为函数的结果返回等。实例对象也可以作为其他实例对象的属性
静态方法：如char1中的_gcd,定义的时候不用self，调用也直接类名+方法名。不过最后设置成私有变量禁止访问，定义时前加@staticmethod
类方法：cls作参数名，在类方法执行时，调用他的类将自动约束到方法的cls参数
'''


class Countable:
    count = 0

    def __init__(self):
        Countable.count += 1

    @classmethod
    def get_count(self):
        return Countable.count


'''
功能是每次创建一个实例对象加一，易错点是有人用self.count,self代指实例，记录全局用类名字，最后直接用类调用Countable().get_count()
'''
