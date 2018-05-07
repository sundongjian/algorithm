'''
二叉树排序树，将字典的存储和查询功能融合在二叉树结构里，采用二叉树有可能得到较高的检索效率
一棵节点中存储着关键码的二叉树是二叉排序树，当且仅当通过中序遍历这可树得到的关键码递增
'''

#二叉树检索算法
from binary_tree.char4 import   BinTNode
from dic_set.char1 import ASSoc
from stack.char1 import SStack


def bt_search(btree,key):
    bt=btree
    while bt is not None:
        entry=bt.data
        if key<entry.key:
            bt=bt.left
        elif key>entry.key:
            bt=bt.right
        else:
            return entry.value
    return None

#二叉排序树字典类

class DictBinTree:
    def __init__(self):
        self._root=None

    def is_enpty(self):
        return self._root is None

    def search(self,key):
        bt = self._root
        while bt is not None:
            entry = bt.data#bt的结点data里存了两个数据，一个是key，一个是value
            if key < entry.key:
                bt = bt.left
            elif key > entry.key:
                bt = bt.right
            else:
                return entry.value
        return None

    #这个插入除非有相同关键码更新，否则最后一定是叶节点
    def insert(self,key,value):
        bt=self._root
        if bt is None:
            self._root=BinTNode(ASSoc(key,value))
            return
        while True:
            entry=bt.data
            if key<entry.key:
                if bt.left is None:
                    bt.left=BinTNode(ASSoc(key,value))
                    return
                bt=bt.left
            elif key>entry.key:
                if bt.right is None:
                    bt.right=BinTNode(ASSoc(key,value))
                    return
                bt=bt.right
            else:
                bt.data.value=value#关键码等于被检索码的，更新
                return

    def values(self):
        t,s=self._root,SStack()
        while t is not None or not s.is_empty():
            while t is not None:
                s.push(t)
                t=t.left
            t=s.pop()
            yield t.data.value
            t=t.rignt
    '''
    values如果返回一个键值对，就是Assoc对象，那么我们就可以修改这个键值对的对象属性，这是很危险的行为，修改后很可能导致
    原来的二叉排序树被破坏，如果想要返回键值对，不能整个返回对象而是直接返回属性
    '''

    def entries(self):
        t, s = self._root, SStack()
        while t is not None or not s.is_empty():
            while t is not None:
                s.push(t)
                t = t.left
            t = s.pop()
            yield t.data.key,t.data.value,
            t = t.rignt

    #删除太过于麻烦，有空再写
    def delete(self):
        pass