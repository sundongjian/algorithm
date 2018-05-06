'''
基于结点的二叉树具有递归结构，很方便进行递归处理。但是这样的二叉树也有不统一之处。其中None表示空树
但是None并不是BinTNode，此外，二叉树并不是并不是一种良好的封装的数据类型 。现在重新定义一个二叉树类
'''
from stack.char1 import SStack

class BinTree:
    def __init__(self):
        self._root=None

    def is_empty(self):
        return self._root is None

    def root(self):
        return self._root

    def leftchild(self):
        return self._root.left

    def rightchild(self):
        return self._root.right

    def set_root(self,rootnode):
        self._root=rootnode

    def set_left(self,leftchild):
        self._root.left=leftchild

    def set_right(self,rightchild):
        self._root.left=rightchild

    def preorder(self):
        t,s=self._root,SStack()
        while t is not None or not s.is_empty():
            while t is not None:
                s.push(t.right)
                yield t.data #此处应该有错误，没有定义过t的data属性   self._root=rootnode 作者
                             # 应该是认为rootnode是使用前面结点类创建的节点，那么这样就有data属性了
                t=t.left
            t=s.pop()



