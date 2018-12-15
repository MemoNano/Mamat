number = "9,223,372,036,854,775,807"
cleanedNumber = ""

for i in range(0, len(number)):
    if number[i] in '0123456789':
        cleanedNumber += number[i]

newNumber = int(cleanedNumber)
print("Cleaned Number is {}: ".format(newNumber))

x = 23
x += 1
print(x)

x -= 4
print(x)

x *= 5
print(x)

x /= 4
print(x)

x **= 2
print("Double time 2 ", x)

x %= 60
print(x)

greeting = "Good"
greeting += " Morning "
print(greeting)

greeting *= 5
print(greeting)

"""
AUGMENTED ASSIGNMENT IN A LOOP:

Early computers could only perform addition. In order to multiply one number by another, they performed
repeated addition.

For example, 5 * 8 was performed by adding 5 eight times.
5 + 5 + 5 + 5 + 5 + 5 + 5 + 5 = 40.
Use a for loop, and augmented assignment, to give answer the result of multiplying number by multiplier

Paste your into your IDE, and make sure it works with different values for number and multiplier.
Note that this exercise checking system will only validate your code with the values 5 and 8, for number and multiplier.
"""

print("************** augmented assignment ************")
number1 = 5
multiplier = 8
answer = 0

# add your loop after this comment

for i in range(multiplier):  # never use already assigned variable
    answer += number1
print(answer)
