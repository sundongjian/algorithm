'''
前面是是使用数组来进行完全二叉树实现的，现在自己定义基于结点的二叉树
'''


# 二叉树节点类
class BinTNode:
    def __init__(self, dat, right=None, left=None):  # 左右也是BinTree对象
        self.data = dat
        self.left = left
        self.right = right


t = BinTNode(1, BinTNode(2), BinTNode(3))


def count_BinTNodes(t):
    if t is None:
        return 0
    else:
        return 1 + count_BinTNodes(t.ringt) + count_BinTNodes(t.left)


# 假设节点中保存数值，求这种二叉树的所有数值之和
def sum_BinTNodes(t):
    if t is None:
        return 0
    else:
        return t.data + sum_BinTNodes(t.left) + sum_BinTNodes(t.right)


def preorder(t, proc):
    if t is None:
        return
    proc(t.data)
    preorder(t.left, proc)
    preorder(t.right, proc)


def print_BinTNode(t):
    if t is None:
        print('^', end=' ')  # 空树输出
    print('(' + str(t.data), end=' ')
    print_BinTNode(t.left)
    print_BinTNode(t.right)


# 宽度优先遍历
from stack.char5 import SQueue


def levelorder(t, proc):
    qu = SQueue()
    qu.enqueue(t)
    while not qu.is_empty():
        t = qu.dequeue()
        if t is None:
            continue
        qu.enqueue(t.left)
        qu.enqueue(t.right)
        proc(t.data)


# 先根遍历
from stack.char1 import SStack


def preorder_nonrec(t, proc):
    s = SStack()
    while t is not None or not s.is_empty():
        while t is not None:  # 直到左枝为空
            proc(t.data)
            s.push(t.right)
            t = t.left
        t = s.pop()


def preorder_elements(t):
    s = SStack()
    while t is not None or not s.is_empty():
        while t is not None:
            s.push(t.right)
            yield t.data
            t = t.left
        t = s.pop()


# 后根序遍历
def postorder_nonrec(t, proc):
    s = SStack()
    while t is not None or not s.is_empty():
        while t is not None:  # 下行，直到找到栈顶的两子数为空
            s.push(t)
            t = t.left if t.left is not None else t.ringt  # 这里不用 try，如果t下面没有子树不会报错，而是None
            # 看结点定义def __init__(self,dat,right=None,left=None)

        t = s.pop()
        proc(t.data)
        if not s.is_empty() and s.top.left == t:  # 如果t是现在栈顶的左子树
            t = s.top().right
        else:
            t = None  #
