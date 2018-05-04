from data_type.char1 import Rational

x = Rational(3, 5)
y = Rational(1, 2)
print(x + y)
print(x > y)

from data_type.char2 import Countable

b = Countable()
c = Countable()
d = Countable()
print(Countable().get_count())

from data_type.char3 import Person
from data_type.char3 import Student

p1 = Person('程琳', '女', (1994, 10, 10), '1212072024')
p2 = Person('王木', '女', (1994, 10, 10), '1212072029')
print(p1)
print(p2)
print(p1.age())
print(p1 < p2)
print(Person.num())
s1 = Student('程月', '女', (1995, 10, 10), '电气')
print(s1.details())



