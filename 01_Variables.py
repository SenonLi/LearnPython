from math import *

### Variables
# name = "John"
# age = "35"
# print("Name == " + name + ", age == " + age)
# isMale = True

### Strings
# phrase = "This is a string."
# print("\nLook at this: " + phrase + "\t Its length is \t" + str(len(phrase)))
# print("Check string Entire Lower: " + str(phrase.islower()))
# print("Lower this string: \t" + phrase.lower())
# print("The 1st character in this string: \t" + phrase[0])
# print("Looking for the index of certain subString : \t \"string\" is at \t" + str(phrase.index("string")))
# print("After replace: " + phrase.replace("string", "String for LearningPython"))
# print("\n")

## Numbers
# print(abs(-5) * 2 + pow(2, 3) + max(int(1000.9), 1))
# print(sqrt(ceil(3.7)))  # ceil is from lib "math"

### Get Input from Users
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print("Hello " + name + "! You are " + age)

### List
# friends = ["Kevin", False, 2, ["Love", True]]
# print(friends)
# friends[1] = True
# print("Last element: " + str(friends[-1]) + "\t Second: " + str(friends[1]))
# print("Range elements starting from Index 1 to the End: " + str(friends[1:]) )
# print("Range elements starting from Index 1 to the previous of Index 3: " + str(friends[1:3]) )

### List Functions
numbers = [1, 3, 2, 0]
numbers.sort() # Cannot sort with mixed array "friends.sort()"
numbers.append(100)
print(numbers)
numbers.reverse()
friends = ["Kevin", "Jim"]
friends.insert(1, "James")
friends.remove("Jim")
friends.extend(numbers)
print(friends)
print("Index of \"James\" == " + str(friends.index("James")) + "\t Count of \"James\" == " + str(friends.count("James")))
friends.pop()
friends22 = friends
print(friends22)
friends.clear()
print(friends)

### Tuples
# Tuple is const, no way to edit after initialization
coordinates = (3, 4, 5)
print(coordinates)
print(coordinates[2])




