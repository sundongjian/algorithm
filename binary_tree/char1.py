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


# 基于数组，即栈
class PrioQueue:
    def __init__(self, elist=[]):
        self._elems = list(elist)  # 作用：对实参表进行拷贝，避免共享
        if elist:
            self.buildheap()

    def is_empty(self):
        return not self._elems

    def peek(self):
        if self.is_empty():
            raise PrioQueueError
        return self._elems[0]

    def enqueue(self, e):
        self._elems.append(None)
        self.siftup(e, len(self._elems) - 1)

    def siftup(self, e, last):
        elems, i, j = self._elems, last, last // 2  # 父节点这样对吗
        while i > 0 and e < elems[j]:
            elems[i] = elems[j]
            i, j = j, (j - 1) // 2  #
        elems[i] = e

    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError
        elemes = self._elems
        e0 = elemes[0]
        e = elemes.pop()
        if len(elemes) > 0:
            self.siftdown(e, 0, len(elemes))
        return e0

    def siftdown(self, e, begin, end):
        elems, i, j = self._elems, begin, begin * 2 + 1  # 父节点这样对吗
        while j < end:
            if j + 1 < end and elems[j + 1] < elems[j]:
                j += 1
            if e < elems[j]:
                break
            elems[i] = elems[j]
            i, j = j, 2 * j + 1
        elems[i] = e

    def buildheap(self):
        end = len(self._elems)
        for i in range(end // 2, -1, -1):  # 这个没有错，end=len(self._elems)而不是end=len(self._elems)-1,不存在漏排情况
            self.siftdown(self._elems[i], i, end)


# 堆排序，从大到小
def heap_sort(elems):
    def siftdown(elems, e, begin, end):
        i, j = begin, begin * 2 + 1
        while j < end:
            if j + 1 < end and elems[j + 1] < elems[j]:
                j += 1
            if e < elems[j]:
                break
            elems[i] = elems[j]
            i, j = j, 2 * j + 1
        elems[i] = e

    end = len(elems)
    for i in range(end // 2, -1, -1):
        siftdown(elems, elems[i], i, end)  # 和上面一样，循环建堆，每个节点和父节点都能形成大小关系
    for i in range((end - 1), 0, -1):
        e = elems[i]
        elems[i] = elems[0]
        siftdown(elems, e, 0, i)  # 取出最小元素，将其积累在表的最后，放一个退一个，最后形成从大到小的堆排序
