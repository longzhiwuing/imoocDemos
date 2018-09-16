from collections import namedtuple

Student = namedtuple('Student', ['name', 'age', 'gender', 'email'])

s = Student('Jim', 16, 'male', 'jim@test.com')

print(s)

s2 = Student(name='Jim', age=16, gender='male', email='jim@test.com')

print(s2)
print(s2.name)

print(isinstance(s2, tuple))
