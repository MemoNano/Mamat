import random

list1 = [111, 134, 112, 111, 114, 115, 167, 188, 185, 110]
list2 = [12, 234, 2, 1, 4, 5, 67, 88, 325, 0]
list3 = [2312, 234, 2, 1, 4, 5, 67, 889, 325, 0]
list4 = [2312, 234, 4442, 1, 4, 5, 67, 889, 325, 0]
list5 = [5555, 234, 4442, 1, 4, 5, 67, 889, 325, 0]
list6 = [6666, 234, 4442, 1, 4, 5, 67, 889, 325, 0]
list7 = [7777, 234, 4442, 1, 4, 5, 67, 8889, 325, 0]

print(max(list1, list2, list3, list4, list5, list6, list7))
maxValue = list1[0]

# for i in range(len(list1)):
#     if maxValue < list1[i]:
#         maxValue = list1[i]
# print("The max value is {} \n".format(maxValue))
#
#

maxValue = max(list7)
print(maxValue)

# highest = 10
# answer = random.randint(1, highest)


# print("Please guess a number between 1 and {}: ".format(highest))
# guess = int(input())
# i = 0

# if guess != answer:
#     if guess < answer:
#         print("Please guess higher")
#     else:
#         print("Please guess smaller")
#     guess = int(input())
#     if guess == answer:
#         print("You got it")
#     else:
#         print("Wrong answer:")
#
# else:
#     print("You got it in first time:")


"""This is my first script to solve random number to guess
Modify the program below to use a while loop to allow as many guesses as necessary.

The program should let the player know whether to guess higher or lower, and should print a message
When the guess is correct. A correct guess will terminate the program.

As an optional extra, allow the player to quite by entering 0 (zero) for their guess. 
"""

"""This my while loop to determine random number in given range: """
highest = 50
answer = random.randint(1, highest)
print("Please guess a number between 1 and {}: ".format(highest))
guess = int(input())
i = 0

while guess != answer:
    if guess == 0:
        break
    if guess < answer:
        print("Please guess higher: ")
    else:
        print("Please guess smaller: ")
    guess = int(input())
    i += 1

print("You got it {}'s try  !!!".format(i + 1))

print("Tim Buchalka's while loop solution: ")

highest = 1000
answer = random.randint(1, highest)
print(answer)
print("Please guess a number between 1 and {}: ".format(highest))
guess = 0
i = 0

while guess != answer:
    guess = int(input())
    if guess > highest or guess == 0:
        print("Invalid guess. Check your guess number range")
    if guess > answer:
        print("Please guess smaller: ")
    elif guess < answer:
        print("Please guess higher: ")
    else:
        print("You got it !!! ")

    i += 1
    if i == 10:
        print("You tried maximum number your guess: ")
        break

""" This is about for loop to guess random number in given range. """

for i in range(highest):
    if guess < answer:
        print("Please guess higher: ")
    else:
        print("Please guess smaller")
    guess = int(input())
    if guess == answer:
        print("You got in fist time!!! ")
    break
