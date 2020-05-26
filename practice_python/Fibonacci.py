"""
Write a program that asks the user how many Fibonacci numbers to generate
and then generates them. Take this opportunity to think about how you can use functions.
Make sure to ask the user to enter the number of numbers in the sequences to generate.
(Hint: The Fibonacci sequence is a sequence of numbers where the next number in the sequence is the
sum of the previous two numbers in the sequence. The sequence looks like this: 1,1,2,3,5,8,13  ...)
"""
a = int(input('Please enter first number'))
b = int(input('Please enter second number'))
user_num = int(input("Please enter number that you want to generate Fibonacci number to generate."))

if user_num < 2:
    user_num = int(input("Please enter bigger than 1 ?"))  # 4
""" 1st STEP: When user enters 2 starting and number of terms needed"""
print(a, b, end=" ")
while user_num - 2:  # 6 - 2
    c = a + b  # 6
    a = b  # 4
    b = c  # 6
    print(c, end=" ")
    user_num = user_num - 1


""" 2ND STEP: When user enters 1 starting number and number of terms needed."""
# print(a, end=" ")
# while user_num - 1:  # 6 - 2
#     c = a  # 6
#
#     a = c  # 4
#     print(c, end=" ")
#     user_num = user_num - 1

""" This code from Github to solve above example: """


def fibonacci():
    asked_num = int(input("Please enter how many numbers would you like to in your fibonacci sequence: "))
    i = 1
    if asked_num == 0:
        fib = []
    elif asked_num == 1:
        fib = [1]
    elif asked_num >= 2:
        fib = [1, 1]
        while i < (asked_num - 1):
            fib.append(fib[i] + fib[i - 1])
            i += 1
        return fib
print(fibonacci())
