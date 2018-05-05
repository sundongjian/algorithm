# from stack.char1 import LStack
# st1=LStack()
# for i in range(0,18):
#     st1.prepend(i)
# print(st1.pop())
# print(st1.pop())
# print(st1.pop())
# print(st1.pop())
#
#
# from stack.char2 import check_parens
# text='([]{}{()})'
# check_parens(text)



# from stack.char3 import suf_exp_evaluator
# e='3 5 - 6 17 4 * + * 3 /'
# exp=e.split(' ')
# print(exp)
# print(suf_exp_evaluator(exp))

# from stack.char4 import norec_fact
# print(norec_fact(10))

from stack.char5 import SQueue

sq = SQueue()
print(sq.is_empty())

sq.enqueue(4)
print(sq.peek())
sq.dequeue()
for i in range(0, 19):
    sq.enqueue(i)
for i in range(0, 19):
    print(sq.dequeue())
