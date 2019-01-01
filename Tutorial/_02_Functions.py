### Python Functions
# def helloWorld():
#     print("Hello World!")
#
# helloWorld()

### Return value of a function
# def cubic(num):
#     return num * num * num
#
# print(cubic(3))

### if & comparisons
# def maxNum(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3
#
# print("Max number is : \t" + str(maxNum(3, 4, 10)))



### While Loop
# i = 1
# while i <= 10:
#     print(i)
#     i += 1
#
# print("Done with the loop")

### For Loop
# for myChar in "Hello World!":
#     print(myChar)

# messy = ["Kevin", 100, False]
# for elem in messy:
#     print(elem)

# myRange = range(10)
# print(myRange)
# for num in myRange:
#     print(num)


### Exponent Functions
# print(3**4)
#
# def raiseToPower(base, pow):
#     result = 1
#     for index in range(pow):
#         result *= base
#     return result
#
# print(raiseToPower(3, 4))


### Try Except, for catching errors
try:
    number = int(input("Enter a number: "))
    print(number)
    result = 10 / number
except ZeroDivisionError as err:
    print(err)
except ValueError as err:
    print(err)

