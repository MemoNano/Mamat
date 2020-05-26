"""
Take two lists, say for example these two:
a = [1,1,2,3,5,8,13,21,34,55,89]
b = [1,2,3,4,5,6,7,8,9,10,11,12,13]
and write a program that returns a list that contains only the elements
that are common between the lists (without duplicates). Make sure
your program works on two lists of different sizes.
"""
a1 = [1, 1, 2, 1,1,-1,3, 5, 8, 13, 21, 34, 55, 89]
b1 = [1, 2, 3, 1,1,4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

common_list = []


def common_numbers_from_two_lists(a, b):
    for index in a:
        if index in b:
            common_list.append(index)
        for j in range(len(common_list)-1):
            if j == common_list[j]:
                common_list.remove(j)

    return common_list


print(common_numbers_from_two_lists(a1, b1))
