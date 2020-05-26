"""
Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
(If you don't know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a
divisor of 26 because 26/13 has no reminder.)
"""

"""
I understand a little bit differently, I thought user input number can divide all list
range that given in for loop
"""

number = int(input("Please enter your divisible number: "))

divisors_list = []


def find_divisors(user_number):
    for i in range(1, 14):
        if i % user_number == 0:
            divisors_list.append(i)
    return divisors_list


print(find_divisors(number))
