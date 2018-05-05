'''
队列，先进后出
ADT Queue:
    Queue(self)
    is_empty(self)
    enqueue(self,elem)
    dequeue(self)#删除最早
    peek(self)#查看最早
'''
#循环顺序表
class QueueUnderflow(ValueError):
    pass

class SQueue:
    def __init__(self,init_len=8):
        self._len=init_len
        self._elems=[0]*init_len
        self._head=0
        self._num=0

    def is_empty(self):
        return self._num==0

    def peek(self):
        if self._num==0:
            raise  QueueUnderflow
        return self._elems[self._head]

    def dequeue(self):
        if self._num==0:
            raise QueueUnderflow
        e=self._elems[self._head]
        self._head=(self._head+1)%self._len
        self._num-=1
        return e

    def enqueue(self,elem):
        if self._num==self._len:
            self._extend()
        self._elems[(self._head+self._num)%self._len]=elem
        self._num+=1

    def _extend(self):
        old_len=self._len
        self._len=old_len*2
        new_elems=[0]*self._len
        for i in range(old_len):
            new_elems[i]=self._elems[(self._head+i)%old_len]
        self._elems,self._head=new_elems,0
