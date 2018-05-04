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
import copy
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

    #链表之间的操作
    def rev(self):
        p=None
        while self._head is not None:
            q=self._head
            self._head=q.next
            q.next=p#书上错误
            p=q
        self._head=p

    #排序
    def sort(self):#参考char2的排序
        if self._head is None:
            return
        crt=self._head.next
        while crt is not None:
            x=crt.elem
            p=self._head
            while p is not crt and p.elem <=x:#跳过小元素
                p=p.next#找到第一个大于等于x的所在位置p
            while p is not crt:#将[p,crt-1]的元素后移
                y=p.elem
                p.elem=x
                x=y
                p=p.next
            crt.elem=x#填上最后一个crt位置
            crt=crt.next

    #下面两个排序为粘贴，有点难
    def sort1(self):
        p = self._head
        if p is None or p.next is None:
            return
        rem = p.next
        p.next = None
        while rem is not None:
            p = self._head
            q = None
            while rem is not None and p.elem <= rem.elem:
                q = p
                p = p.next
            if q is None:
                self._head = rem
            else:
                q.next = rem
            q = rem
            rem = rem.next
            q.next = p

    # 第三种排序算法
    def sort2(self):
        list1 = copy.deepcopy(self)
        if list1._head.next is None:
            return
        list1._head.next.next = None

        if list1._head.next.elem < list1._head.elem:
            a = list1._head
            list1._head = list1._head.next
            list1._head.next = a
            list1._head.next.next = None

        temp = self._head.next.next

        while temp is not None:
            p = list1._head
            q = list1._head.next
            if temp.elem < list1._head.elem:
                a = temp.next
                temp.next = list1._head
                list1._head = temp
                temp = a
                if temp is not None:
                    print(temp.elem)
                    list1.printall()
            elif temp.elem >= list1._head.elem:
                while q is not None:
                    if q.elem >= temp.elem:
                        a = temp.next
                        temp.next = q
                        p.next = temp
                        temp = a
                        break
                    elif q.elem < temp.elem:
                        q = q.next
                        p = p.next
                if q is None:
                    p.next = temp
                    a = temp.next
                    temp.next = None
                    temp = a
        self._head = list1._head










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








