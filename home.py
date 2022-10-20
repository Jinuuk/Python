import sys

from pkg.pkg1 import a as d
from pkg.pkg2 import c as e
from pkg.pkg1 import b

print(sys.path)

d.func1()
print(d.name)

d.func3()
e.func3()

# p1 = b.Person()
# p1.study()
# p1.eat()

p2 = b.Person('홍길동',30)
p2.study()
p2.eat()
print(p2.national)

p3 = b.Person('홍길순',25)
p3.study()
p3.eat()
print(p3.national)

print(b.Person.national)

p2.print_info()
p3.print_info()

p4 = b.Student('홍길남',19,'1234')
p4.study()
p4.eat()
p4.sleep()
p4.print_info()
