'''
二叉树排序树，将字典的存储和查询功能融合在二叉树结构里，采用二叉树有可能得到较高的检索效率
一棵节点中存储着关键码的二叉树是二叉排序树，当且仅当通过中序遍历这可树得到的关键码递增
'''

#二叉树检索算法
from binary_tree.char4 import   BinTNode
from dic_set.char1 import ASSoc


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
        pass
