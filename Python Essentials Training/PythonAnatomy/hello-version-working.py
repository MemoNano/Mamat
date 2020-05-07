#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import platform

version = platform.python_version()

print('This is python version {}'.format(version))  # --> A line of code and it's called STATEMENT

n = 5

while n < 12:
    print(n)
    n += 1


def function(n=1):
    print(n)


function(47)


# isPrime function

def isprime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % 2 == 0:
            return False
    else:
        return True


n = 9
if isprime(n):
    print("'{0} is prime'".format(n))
else:
    print("{} is NOT prime".format(n))
    print(type(n))



a = 8
b =9
x = f'seven {a} {b}'
print('x is {}'.format(x))
