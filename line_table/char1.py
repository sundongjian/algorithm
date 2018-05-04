'''
在程序里，经常需要一组数据元素作为整体管理和使用，需要创建这种原数组用变量记录他们
从实现角度来讲，要把结构里面的数据组织好，提供一套有用且有效实现这些操作
从使用者来讲，提供了哪些操作
构造，解析（属性），改变表内容，操作，两个表之间操作，
ADT List:
    List(self)
    is_empty(self)
    len(self)
    prepend(self,elem)首元素加
    append(self,elem)尾元素加
    insert(self,elem,i)加入具体位置
    del_first(self)删除
    del_last(self)删除尾
    del(self,i)
    search(self,elem)查找
    forall(self.op)对表中元素进行op操作
以下是单链表
注意head永远存在，如果是空表，那么head=None，如果不是，那么就是第一个元素
'''

#制作节点的类，节点的属性有当前节点元素和下一节点位置
#单链表
class LNode:
    def __init__(self,elem,_next=None):
        self.elem=elem
        self.next=_next

class LinkedListUnderflow(ValueError):
    pass

class LList:
    def __init__(self):
        self._head=None

    def is_empty(self):
        return self._head is None

    def prepend(self,elem):
        self._head=LNode(elem,self._head)

    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow
        e=self._head.elem
        self._head=self._head.next
        return e

    def append(self,elem):
        if self._head is None:
            self.head=LNode(elem)
            return
        p=self._head
        while p.next is not None:
            p=p.next
        p.next=LNode(elem)

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow
        p=self._head
        while p.next is None:
            e=p.elem
            self.head=None
            return e
        while p.next.next is None:
            p=p.next
        e=p.next.elem
        p.next=None
        return e

    def find(self,pred):#找到第一个满足pred谓词方法的元素
        p=self._head
        while p is not None:
            if pred(p.elem):
                return p.elem
            p.next
        return -1 #找不到返回-1

    def printall(self):
        p=self._head
        while p is not None:
            print(p.elem,end='')#不加end就会换行，最后一个元素后面不加，
            if p.next is not None:
                print(',',end='')
            p=p.next
        print('')

    def for_each(self,proc):
        p=self._head
        while p is not None:
            proc(p.elem)
            p=p.next

    def elements(self):
        p=self._head
        while p is not None:
            yield p.elem
            p=p.next

    def filter(self,pred):
        p=self._head
        while p is not None:
            if pred(p.elem):
                yield
            p=p.next


#增加尾节点
class LRist(LList):
    def __init__(self):
        self._rear=None

    def is_empty(self):
        return self._head is None

    def prepend(self,elem):
        if self._head is None:
            self._head=LNode(elem)
            self._rear=self._head
        else:
            self._head=LNode(elem,self._head)

    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow
        e=self._head.elem
        self._head=self._head.next
        return e

    def append(self,elem):
        if self._head is None:
            self._head=LNode(elem)
            self._rear=self._head
            return
        else:
            self._rear.next=LNode(elem)
            self._rear=self.rear.next

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow
        p=self._head
        while p.next is None:
            e=p.elem
            self.head=None
            return e
        while p.next.next is None:
            p=p.next
        e=p.next.elem
        p.next=None
        self._rear=p
        return e

#循环单链表
class LCList():

    def __init__(self):
        self._rear=None

    def is_empty(self):
        return self._rear is None

    def prepend(self,elem):
        p=LNode(elem)
        if self._rear is None:
            p.next=p#建立一个节点的换
        else:
            p.next=self.rear.next
            self._rear.next=p

    def append(self,elem):
        self.prepend(elem)
        self._rear=self._rear.next.next

    def pop(self):
        if self._rear is None:
            raise LinkedListUnderflow
        p=self._rear.next
        if self.rear is p:
            self.rear=None
        else:
            self._rear=p.next
        return p.elem

    def printall(self):
        if self._rear is None:
            return
        p=self._rear.next
        while p is not None:
            print(p,end='')
            if p is self.rear:
                break
            p=p.next


#双链表
class DLNode(LNode):
    def __init__(self,elem,pre=None,next_=None):
        LNode.__init__(self,elem,next_)
        self.prev=prev








