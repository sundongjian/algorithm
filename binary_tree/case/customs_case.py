'''
模拟类，海关
首先分析完成这种模拟所需要记录的各种信息，为了运行customs，需要一个实际驱动模拟的
simulation的对象。由于车辆到达可能排队，还需要一个队列对象，记录正在排队的车辆。
属性waitline的值是这个等待队列，几个检查通道是海关的内部资源，用gates表示各个通道的状态
'''
from binary_tree.case.event_case import Arrive
from binary_tree.framework.general import Simulation
from stack.char5 import SQueue


class Customs:
    def __init__(self, gate_num, duration, arrive_interval, check_interval):
        self.simulation = Simulation(duration)
        self.waitline = SQueue()

        self.duration = duration
        self.gates = [0] * gate_num
        self.total_wait_time = 0
        self.total_used_time = 0
        self.car_num = 0
        self.arrvie_interval = arrive_interval
        self.check_interval = check_interval

    def wait_time_acc(self, n):
        self.total_wait_time += n

    def total_time_acc(self, n):
        self.total_used_time += n

    def car_count_1(self):
        self.car_num += 1

    def add_event(self, event):
        self.simulation.add_event(event)

    def cur_time(self):
        return self.simulation.cur_time()

    def enqueue(self, car):
        self.waitline.enqueue(car)

    def has_queue_car(self):
        return not self.waitline.is_empty()

    def next_car(self):
        return self.waitline.dequeue()

    def find_gate(self):
        for i in range(0, len(self.gates)):
            if self.gates[i] == 0:
                self.gates[i] = 1
                return i
        return None

    def free_gate(self, i):  # 车过去后将该通道设置成0
        if self.gates[i] == 1:
            self.gates[i] = 0
        else:
            raise ValueError('clear gate error')

    def simulate(self):
        Arrive(0, self)
        self.simulation.run()
        self.statistics()

    def statistics(self):
        print('simulation%sminutes%sgates' % (str(self.duration), str(len(self.gates))))
        print(self.car_num, 'car pass the gates')
        print('average waitting time:', self.total_wait_time / self.car_num)
        i = 0
        while not self.waitline.is_empty():
            self.waitline.dequeue()
            i += 1
        print(i, 'cars are in wating line')
