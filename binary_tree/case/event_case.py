from random import randint

from binary_tree.framework.event_defi import Event
from binary_tree.case.car_case import Car


def event_log(time, name):
    print('Event:%s happends at %s' % (name, str(time)))


class Arrive(Event):
    def __init__(self, arrive_time, customs):
        Event.__init__(self, arrive_time, customs)  # 时间对象只有两个属性，到达时间和宿主系统，有用的只是到达时间
        # 车先来先加入，后来后加入，放队列就行。但是事件时间不是这么规律，我们把事件放到二叉树之后每次都能抛出最早的时间，自动排序功能
        customs.add_event(self)  # 疑惑为什么要加入二叉树，加到普通队列不行吗。

    def run(self):
        time, customs = self.time(), self.host()
        event_log(time, 'car arrvie')
        Arrive(time + randint(*customs.arrvie_interval), customs)  # 生成一个到达事件
        car = Car(time)
        if customs.has_queue_car():
            customs.enqueue(car)
            return
        i = customs.find_gate()
        if i is not None:
            event_log(time, 'car check')
            Leave(time + randint(*customs.check_interval), i, car, customs)
        else:
            customs.enqueue(car)


class Leave(Event):
    def __init__(self, leavel_time, gate_num, car, customs):
        Event.__init__(self, leavel_time, customs)
        self.car = car
        self.gate_num = gate_num
        customs.add_event(self)

    def run(self):
        time, customs = self.time(), self.host()
        event_log(time, 'car leavel')
        customs.free_gate(self.gate_num)
        customs.car_count_1()
        customs.total_time_acc(time - self.car.arrive_time())
        if customs.has_queue_car():
            car = customs.next_car()
            i = customs.find_gate
            event_log(time, 'car check')
            customs.wait_time_acc(time - car.arrive_time())
            Leave(time + randint(*customs.check_interval), self.gate_num, car, customs)
