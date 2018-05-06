'''
ADT Dict
    Dict(self)
    is_empty(self)
    num(self)
    searvh(self)
    insert(self,key,value)
    delete(self,key)
    value(self)
    entries(self)
字典的检索效率：在一次完整检索过程中比较关键吗的平均次数，通常称为平均检索长度 ASL=P(J)*C(J)叠加求和
'''
#定义一个关联对象
class ASSoc:
    def __init__(self,key,value):
        self.key=key
        self.value=value

    def __lt__(self, other):
        return self.key < other.key

    def __le__(self,other):
        return self.key <= other.key

    def __str__(self):
        return 'Assoc({0},{1})'.format(self.key,self.value)


# 二分法：如果关键吗取自有序的集合，可以按照关键吗的大小顺序排列字典里的项,这时候可以用二分法
def bisearch(lst, key):
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if key == lst[mid].key:
            return lst[mid].value
        if key < lst[mid].key:
            high = mid - 1
        else:
            low = mid + 1

'''
如果关键码连续存储，关键码就是存储地址的下标，但是有一些关键码并不适合作为数据存储的下标，这样可以考虑一种运算将他们映射到一种下标
常用散列函数：除余法 基数转换法
除余法：除以某数的余数，这很好理解
基数转化法：将关键码看成基数为r的r进制，将其转换为是进制或者二进制
冲突的内消解：
开地址技术1.线性探查法：如果遇到映射的位置已经被占据，那么存储到下一位，如果依然被占据，再顺延。
双三列探查：取一个函数如h(key)=key mod 5 +1,如果发生冲突，往后顺延h(key)位，这个顺延只在空位置顺延
删除操作：在被删除位置存入另一个特殊标记，检索时候看做有元素并继续往下探查，插入的时候看做没有元素，插入到此位置

冲突外消解：溢出区方法 发生冲突时将相应数据和关键码一起存入溢出区。相应的检索和删除操作也是先从散列位置开始，如果关键码不匹配转到溢出区
（都是由关键码求出的散列值怎么会不匹配）
桶散列：一片存储区每个位置引出一串单链表
python的标准型dict是基于散列实现的

'''