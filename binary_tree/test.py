from binary_tree.char1 import PrioQueue

pr = PrioQueue()
print(pr.is_empty())
pe = PrioQueue([1, 2, 5, 7, 8, 9])
print(pe.peek())
print(pe.enqueue(10))
for i in range(0, 7):
    print(pe.dequeue())
