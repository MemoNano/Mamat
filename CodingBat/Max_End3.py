"""
Given an arry of ints length 3, figure out which is larger, the first or last element in the array,
and set all the other elements to be that value. Return the changed array.

max_end3([1, 2, 3]) → [3, 3, 3]
max_end3([11, 5, 9]) → [11, 11, 11]
max_end3([2, 11, 3]) → [3, 3, 3]
"""

num = [12, 34, 112, 23, 123, 475]


def max_end3(nums):
    max_value = max(nums)
    print(max_value)

    for i in range(len(nums) - 1):
        nums[i] = max_value
        i + 1
    print(nums)


max_end3(num)

f = [1, 2, 3, 4]
g = [2, 2, 2, 2]
c = [0] * 2


def middle_way(a, b):
    middlea = int(len(a) / 2)
    middleb = int(len(b) / 2)

    c[0] = a[middlea]
    c[1] = b[middleb]

    return c


print(middle_way(f, g))
