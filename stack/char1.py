'''
栈抽象数据类型
ADT Stack
    Stack(self)
    is_empty(self)
    push(self,elem)
    pop(self)
    top(self)#取出栈里最后压入的元素，不删除
'''
class StackUnderflow(ValueError):
    pass

#连续实现
class SStack:

    def __init__(self):
        self._elems=[]

    def is_empty(self):
        return self._elems is None

    def top(self):
        if self._elems==[]:
            raise StackUnderflow
        return self._elems[-1]

    def push(self,elem):
        self._elems.append(elem)

    def pop(self):
        if self._elems==[]:
            return StackUnderflow('IN sstack.pop() ')
        return self._elems.pop()

    def depth(self):
        return len(self._elems)

#链接实现,表头作栈顶
from line_table.char1 import LNode


class LStack():
    def __init__(self):
        self._top = None

    def is_empty(self):
        return self._top is None

    def prepend(self, elem):
        self._top = LNode(elem, self._top)

    def pop(self):
        if self._top is None:
            raise StackUnderflow
        e = self._top.elem
        self._top = self._top.next
        return e

    def top(self):#不删除
        if self._top is None:
            raise StackUnderflow
        return self._top.elem



