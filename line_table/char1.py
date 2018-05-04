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
'''

#制作节点的类，节点的属性有当前节点元素和下一节点weizhi
class LNode:
    def __init__(self,elem,_next):
        self.elem=elem
        self.next=_next