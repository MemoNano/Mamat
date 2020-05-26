"""
Given an int array length 2 , return True if it contains a 2 or a 3.
has23([2, 5]) → True
has23([4, 3]) → True
has23([4, 5]) → False

"""
nums = [2, 5]


def has23(nums):
    for i in nums:
        if i == 2 or i == 3:
            return True
        else:
            return False


print(has23(nums))

print("**********  List-1 > max_end3  ******************")

"""
Given an array of ints length 3, figure out which is larger, the first or laast element in the 
array, and set all the other elements to be that value. Return the changed array.

max_end3([1, 2, 3]) → [3, 3, 3]
max_end3([11, 5, 9]) → [11, 11, 11]
max_end3([2, 11, 3]) → [3, 3, 3]

"""
nums = [1, 3, 4, 5, 12, 6, 7, 8, 9]
array = [0] * len(nums)
k = 0


def max_end3(nums):
    for i in range(len(nums)):
        return nums[i] * len(nums) if nums[i] >= nums[i + 1] else [nums[i + 1]] * len(nums)


print(max_end3(nums))

print([nums[0]] * len(nums))  # Basically this will override first index with given number
print([nums[-1]])

# def max_end5(nums):
#     for i in range(len(nums)-1):
#         if(nums[i] >= nums[i+1]):
#             n = nums[i]
#
#     for j in nums:
#         array[j]= n
#         j+1
#     return array
#
# print(max_end5(nums))


print("Please use *********   Thank you ********")

a = [1, 3, 5]
b = a
a[:] = [x + 2 for x in a]
print(b)
