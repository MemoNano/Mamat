meal = ["egg", "bacon", "span", "sausages"]

nasty_food_item = ""
for item in meal:
    if item == 'spam':
        nasty_food_item = item
        break
else:
    print("I'll have a plate of that, then, please")

if nasty_food_item:
    print("Cant't I have anything without spam it: " + nasty_food_item)

"""
BREAK: Modify the code so that it stops printing when it reaches a number that's exactly divisible by 11. That 
number should be the last value printed. 
Reminder: If avalue, x , is divisible by 11 then x % 11 will be zero.
Hint: 0 is exactly divisible by every number, so your solution will need to allow for that.
"""

for i in range(0, 100, 7):
    print(i)
    if (i > 0) and (i % 11 == 0):
        break

print("************* Continue ************* ")

"""
CONTINUE: 
Write a program to print out all the numbers from 0 to 20 that aren't divisible by 3 or 5.
Zero is considered divisible by everything(zero should not appear in the output)
The aim is to use the continue statement, but it's also possible to do this without continue. 
"""
for i in range(20):
    if i % 3 == 0 or i % 5 == 0:
        continue
    print(i)

print("********* without using CONTINUE *********")

for i in range(20):
    if (i % 3 != 0) and (i % 5 != 0):
        print(i)
