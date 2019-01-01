class Person:

    def __init__(self, isMale):
        self.isMale = isMale

    def gender(self):
        if (self.isMale):
            print("I am a Male. \n")
        else:
            print("I am a Female. \n")