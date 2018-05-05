'''
ADT BinTree:
    BinTree(self,data,left,right)
    is_empty(self)
    num_nodes(self)
    data(self)
    left(self)
    right(self)
    set_left(self)
    set_right(self)
    traversal(self)#遍历节点形成迭代器
    forall(self,op)#对每个节点进行某操作
'''

class PrioQueueError(ValueError):
    pass

#基于数组，即栈
class PrioQueue:
    def __init__(self,elist=[]):
        self._elems=list(elist)#作用：对实参表进行拷贝，避免共享
        if elist:
            self.buildheap()

    def is_empty(self):
        return not self._elems

    def peek(self):
        if self.is_empty():
            raise PrioQueueError
        return self._elems[0]

    def enqueue(self,e):
        self._elems.append(None)
        self.siftup(e,len(self._elems)-1)

    def siftup(self,e,last):
        elems,i,j=self._elems,last,last//2#父节点这样对吗
        while i>0 and e<elems[j]:
            elems[i]==elems[j]
            i,j=j,(j-1)//2#
        elems[i]=e

    def queue(self):
        if self.is_empty():
            raise PrioQueueError
        elemes=self._elems
        e0=elemes[0]
        e=elemes.pop()
        if len(elemes)>0:
            self.siftdown(e,0,len(elemes))
        return e0

    def siftdown(self,begin,end):
        elems, i, j = self._elems,begin, begin*2+1  # 父节点这样对吗
        while j<end:
            if j+1<end and elems[j+1]<elems[j]
                j+=1
            if e<elems[j]:
                break
            elems[i]=elems[j]
            i,j=j,2*j+1
        elems[i]=e

    def buildheap(self):
        end=len(self._elems)
        for i in range(end//2,-1,-1):
            self.siftdown(self._elems[i],i,end)

