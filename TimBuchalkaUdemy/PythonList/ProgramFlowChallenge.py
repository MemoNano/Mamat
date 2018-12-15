"""
Create a program that takes and IP address entered at the keyboard
and prints out the number of segments it contains, and the length of each segment.

An IP address consists of 4 numbers, separated from each other with a full stop. But your program should just
count however many are entered
Examples of the input you may get are:
    127.0.0.1
    192.168.0.1
    10.0.123456.255
    172.16
    255

So your program should work even with invalid IP addresses. We're just interested in the
number of segments ans how long each one is.

Once you have a working program, here are some more suggestions for invalid input to test:
    .123.45.678.91
    123.4567.8.9.
    123.156.289.10123456
    10.10t.10.10
    12.9.34.6.12.90
    '' - that is, press enter without typing anything

This challenge is intended to practice for loops and if/else statement, so although
you could use other techniques ( such as splitting the string up) , that's not the
approach we're looking for here.
"""

# ipAddress = input("Please enter your IP Address: ")
# segment = 1
# segment_ len = 0
#
# for i in ipAddress:
#     if i.startswith(".") or i.endswith("."):
#         print("Invalid IP Address")
# else:
#     list1 = ipAddress.split(".")
#
# print(len(list1))

input_prompt = "An IP address consists of 4 numbers, separated from each other with a full stop: "
ipAddress = input(input_prompt)
if ipAddress[-1] != '.':
    ipAddress += '.'

segment = 1
segment_len = 0
# character = ""

for character in ipAddress:
    if character == ".":
        print("segment {} contains {} character".format(segment, segment_len))
        segment += 1
        segment_len = 0
    else:
        segment_len += 1

# Unless the final character in the string was a . then we haven't printed the last segment.

# if character != ".":  # Like Java and C++ Programming languages "character" variable is not accessible outside of for
#                         # loop But it is perfectly fine in Python as long as for loop guaranteed to executed once.
#         print("segment {} contains {} character".format(segment, segment_len))


"""
Question 1:
The following program is intended to print out a "times table" for the value 8
"""

value = 8
answer = 0

for x in range(1, 13):
    answer = value * x
    print("{0} times {1} is {2}".format(x, value, answer))

taxi = 4
minivan = 14


def choose_taxi_minivan(people):
    if taxi < people <= minivan:
        print("Take minivan: ")


print(choose_taxi_minivan(5))

for value in range(0, 20, 2):
    print(value)
