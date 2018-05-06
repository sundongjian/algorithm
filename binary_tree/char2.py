'''
前面是是使用数组来进行二叉树实现的，现在自己定义二叉树结点,以便实现二叉树的各种操作
'''

class BinTNode:
    def __init__(self,dat,right=None,left=None):#左右也是BinTree对象
        self.data=dat
        self.left=left
        self.right=right

t=BinTNode(1,BinTNode(2), BinTNode(3))
def count_BinTNodes(t):
    if t is None:
        return 0
    else:
        return 1+count_BinTNodes(t.ringt)+count_BinTNodes(t.left)

#假设节点中保存数值，求这种二叉树的所有数值之和
def sum_BinTNodes(t):
    if t is None:
        return 0
    else:
        return t.data+sum_BinTNodes(t.left)+sum_BinTNodes(t.right)

def preorder(t,proc):
    if t is None:
        return
    proc(t.data)
    preorder(t.left,proc)
    preorder(t.right,proc)

def print_BinTNode(t):
    if t is None:
        print('^',end=' ')#空树输出
    print('('+str(t.data),end=' ')
    print_BinTNode(t.left)
    print_BinTNode(t.right)

    






