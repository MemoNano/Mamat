"""
Hello World , my name is Memo and I live in Russia since I was born.
"""
for i in range(0,100,5):
    print(i)

String = "example"
for c in String:
    print("One letter at time: " + c)

a = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
print(a[1:4])
print(a[2:])

"""

Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.


rotate_left3([1, 2, 3]) → [2, 3, 1]
rotate_left3([5, 11, 9]) → [11, 9, 5]
rotate_left3([7, 0, 0]) → [0, 0, 7]
"""
nums = [1, 2, 3]  # --> [2, 3, 1]


def rotate_left(nums):
    nums = [1, 2, 3]
    return [nums[1], nums[2], nums[0]]


print(rotate_left(nums), end="\n *************** This is good ************")


def defArgFunc(empName, emprole="Manager"):
    print("Emp Name: ", empName)
    print("Emp Role ", emprole)
    return;


print(" \n Using default value ")
defArgFunc(empName="Nick")

print("******************************************")
print("Overwriting default value: ")
defArgFunc(empName="Tom", emprole="CEO")


def reqArgFunc(empname):
    print("Emp Name: " + empname)
    return


print("Not passing required arg value")
reqArgFunc("Mamat")

"""
Keyword is and example of keyword argumentcode snippeet. We have written the code  in a script file named keyArg.py
"""


def keyArgFunc(empname, emprole):
    print("Employer Name: ", empname)
    print("Employer role: ", emprole)
    return;


print("\n Calling in proper sequence")
keyArgFunc(empname="Nelson", emprole="Manager")

print("Calling in opposite sequence ")
keyArgFunc(emprole="CEO & Manager", empname="Mamytov")


def keyArgFunc(empname, empID):
    print("Employer Name: ", empname)
    print("Employer empID: ", empID)
    return;


print(keyArgFunc("Mamat", 23))
print(keyArgFunc(56, "Janara"))


def varLenArgFuch(*varvallist):
    print("The Output is: ")
    for varval in varvallist:
        print(varval)
    return;


print("\n Calling with single value")
varLenArgFuch(55)

print("\n Calling with multiple values: ")
varLenArgFuch(50, 60, 70, 80)
