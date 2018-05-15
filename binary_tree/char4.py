'''
哈夫曼树。它能从任意的实数集合构造出与之对应的哈夫曼树
算法：在给出的实数集中挑出最小的两个数构成。将两数相加之和作为父节点，在实数集中去掉两个数并且
加入刚才产生的新节点，重复刚才步骤这样形成的二叉树并不唯一，但是外部路径长度一定相等
'''

from binary_tree.char1 import PrioQueue
from binary_tree.char2 import BinTNode

class HTNode(BinTNode):
    def __lt__(self,othernode):
        return self.data <othernode.data

class HuffmanPrioQ(PrioQueue):
    def number(self):
        return len(self._elems)

def HuffmanTree(weight):
    trees=HuffmanPrioQ()
    for w in weight:
        trees.enqueue(HTNode(w))
    while trees.number() >1:
        t1=trees.dequeue()
        t2=trees.dequeue()
        x=t1.data+t2.data
        trees.enqueue(HTNode(x,t1,t2))
    return trees.dequeue()
