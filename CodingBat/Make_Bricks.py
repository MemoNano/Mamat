"""
We want to make a row of bricks that is goal inches long. We have a number of small
bricks (1 inch each) and big bricks (5 inches each). Return True if it is possible to
make the goal by choosing from the given bricks. This is a little harder than it looks and
can be done without any loops. See also: Introduction to MakeBricks
"""

sentence = "Hello. World. my name is.Mamat. and my sister's. name is Janara. Second sister's name is Jypargul."

big = 1
goal = 9
small = 3
resto = goal
resto -= 5 * min(big, goal / 5)
print(resto - small)

dot_count = 0

for char in sentence:
    if char == ".":
        dot_count += 1

print(dot_count)

"""Question 8:
            In the code snippet below, what input would you have to provide, to see the message
            'Thank you for playing, please call back soon' """

choice = None

while choice != '0':
    choice = input("Please enter your choice. Press enter to quite:   ")
    if choice == '':
        break

    print("You have selected {}".format(choice))
else:
    print("Thank you for playing, please call back soon.")
