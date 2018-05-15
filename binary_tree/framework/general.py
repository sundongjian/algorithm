'''
做这种模拟，基本思想是按照事情发生的顺序处理，在模拟系统里用一个优先队列保存已知在特定时刻发生的时间，
系统的运行就是不断的从有限队列取出等待的时间挨个处理
在一些事件的处理中可能会引发新的时间，将这些时间放入优先队列
系统始终维持着一个当前时间，也就是正在发生哪个事件的时间
'''
from binary_tree.char1 import PrioQueue



class Simulation:
    def __init__(self, duration):  # duration是模拟的总时间
        self._eventq = PrioQueue()
        self._time = 0
        self._duration = duration

    def run(self):
        while not self._eventq.is_empty():
            event = self._eventq.dequeue()  # 注意event只是在二叉树里存储的对象
            self._time = event.time()  # 事件的时间就是当前的时间
            if self._time > self._duration:
                break
            event.run()

    def add_event(self, event):
        self._eventq.enqueue(event)

    def cur_time(self):
        return self._time
