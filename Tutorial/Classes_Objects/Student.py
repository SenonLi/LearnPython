from Person import Person

class Student(Person):

    def __init__(self, isMale, name, age, isRegistered):
        Person.isMale = isMale
        self.name = name
        self.age = age
        self.isRegistered = isRegistered

    def gender(self):
        if (self.isMale):
            print("I am a Male Student! \n")
        else:
            print("I am a Female Student! \n")

    def register(self):
        self.isRegistered = True