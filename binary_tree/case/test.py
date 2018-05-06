# class Customs:
#     def __init__(self,gate_num,duration,arrive_interval,check_interval):
from binary_tree.case.customs_case import Customs

arrive_interval = (1, 2)
check_interval = (3, 5)

cus = Customs(3, 480, arrive_interval, check_interval)
cus.simulate()
