import string

"""

The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.

"""


def is_leap_year(year):
    leap = False

    # Write your logic here:
    if year % 4 == 0:

        if year % 100 != 0:
            leap = True
        elif year % 400 == 0:
            leap = True
    return leap


alpha = string.ascii_lowercase

n = int(input())
L = []

for i in range(n):
    s = "-".join(alpha[i:n])
    L.append(s[::-1] + s[1:])

width = len(L[0])

for i in range(n - 1, 0, -1):
    print(L[i].center(width, "-"))

for i in range(n):
    print(L[i].center(width, "-"))


def make_chocolate(small, big, goal):
    if goal > big * 5 + small or small < goal % 5:
        return -1

    remaining = goal – big * 5

    while remaining < 0:
        remaining += 5
    return remaining
