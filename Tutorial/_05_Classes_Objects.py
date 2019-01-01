import sys
sys.path.append("Classes_Objects") # need to include as Python.Path for importing

from Classes_Objects.Person import Person
from Classes_Objects.Student import Student
## from file import class


person1 = Person(False)
student1 = Student(True, "Kevin", 22, False)
print(student1.name)
student1.register()
print(student1.isRegistered)

person1.gender()
student1.gender()