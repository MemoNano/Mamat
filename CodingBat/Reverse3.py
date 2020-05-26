import unittest


class Reverse3(unittest.TestCase):
    """Given an array of ints length 3, return a new array with the elements in reverse order, so
    {1,2,3} becomes {3,2,1}.
    reverse3([1, 2, 3]) → [3, 2, 1]
    reverse3([5, 11, 9]) → [9, 11, 5]
    reverse3([7, 0, 0]) → [0, 0, 7]
    """


def reverse(nums):
    nums1 = [1, 2, 3]
    return [nums[2], nums[1], nums[0]]


nums1 = [1, 2, 3]

print(reverse(nums1))

"""
Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.

middle_way([1, 2, 3], [4, 5, 6]) → [2, 5]
middle_way([7, 7, 7], [3, 8, 0]) → [7, 8]
middle_way([5, 2, 9], [1, 4, 5]) → [2, 4]

"""

a1 = [1, 2, 3]
b1 = [7, 7, 7]
num = [0] * 2


def middle_way(a, b):
    a1 = [1, 2, 3]
    b1 = [7, 7, 7]
    num = [0] * 2
    num[0] = a[1]
    num[1] = b[1]
    return num


print(middle_way(a1, b1))

"""
Given an array pf omts, return a new array lenth 2 containing the dirst and last elements from the original array. 
The original array will belength 1 or more.

make_ends([1,2,3,]) --> [1,3]
make_ends([1,2,3]) --> [1,4]

"""
nums2 = [0, 1, 23, 3, 4, 5, 6]


def make_ends(nums):
    array = [0] * 2
    array[0] = nums[0]
    array[1] = nums[-1]
    return array


print("Last 2 digits of original array is: ", make_ends(nums2))
