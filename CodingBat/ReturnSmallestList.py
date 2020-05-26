lst = [1, 67, 0, -78, -990, 34, 15, 88, 2, -1000, -200, 1]


def smallest_num_from_list(number_list=None):
    if number_list is None:
        number_list = []
    min_index = 0
    smallest = None
    for i in range(1, len(number_list)):
        if number_list[i] <= number_list[min_index]:
            smallest = number_list[i]
            min_index = i

    return smallest


lst3 = []
print(smallest_num_from_list(lst))

# lst = [34, 15, 88, -100, 0, 1000, 4, 2]
#
#
# def minmax1(x):
#     minimum = maximum = x[0]
#     b = x[1:]
#     for i in x[1:]:
#         if i < minimum:
#             minimum = i
#         else:
#             if i > maximum: maximum = i
#     return (minimum, maximum)
#
# lst2 = []
#
# print(minmax1(lst2))
