#
# ipAddress = input("Please enter an IP address: ")
# print(ipAddress.count("."))

parrot_list = ["non pinin", "no more", "a stiff", "bereft of live"]

for state in parrot_list:
    print("This Parrot is " + state)

parrot_list.append("A Norwegian Blue")

print("\n*******   After adding on more argument: **********\n")

for state in parrot_list:
    print("Parrot is " + state)

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

""" if you use sort in print() i will print 'None'
    Because it will not create new project. It will work on existing object"""
print(even.sort(), odd.sort())

numbers = even + odd

""" 2 Second way of Sorting is : """
number_sorted_order = sorted(numbers)
print(number_sorted_order)

if numbers == number_sorted_order:
    print("The lists are equal")
else:
    print("The lists are not equal")

if number_sorted_order == sorted(numbers):
    print("Numbers are equal")
else:
    print("Numbers are not equal")

list_1 = []
list_2 = list()

print("\nList 1 is : {}".format(list_1))
print("List 2 is : {}".format(list_2))

if list_1 == list_2:
    print("The list are equal:\n")

list3 = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print("\t {}".format(list3))

for char in list3:
    print(char, end=' ')

print("*********   enumerate() built-in function  ***********")

"""
        List Methods
Here are some other common list methods.

list.append(elem) -- adds a single element to the end of the list. Common error: does not return the new list, 
                        just modifies the original.
list.insert(index, elem) -- inserts the element at the given index, shifting elements to the right.
list.extend(list2) adds the elements in list2 to the end of the list. Using + or += on a list is similar 
                    to using extend().
list.index(elem) -- searches for the given element from the start of the list and returns its index. 
                    Throws a ValueError if the element does not appear (use "in" to check without a ValueError).
list.remove(elem) -- searches for the first instance of the given element and removes it
                    (throws ValueError if not present)
list.sort() -- sorts the list in place (does not return it). (The sorted() function shown later is preferred.)
list.reverse() -- reverses the list in place (does not return it)
list.pop(index) -- removes and returns the element at the given index. Returns the rightmost element 
                    if index is omitted (roughly the opposite of append()).
"""

for indx, val in enumerate(list3, start=1):
    print(indx, val, end='\t')

print("\n******** Only one letter *********")

list3.insert(0, 'Mamat')
print(list3)

print(list3.index('X'))

print("Make sure 'is' -is working as '==' ")
even_number = list(even)

if even_number == even:
    print("All your answers are even!!!")

list_4 = [2, 3, 4, 6, 'Memo']

print(list_4)

print("==========  Reversing list and comparing with it  ==============")
print(even_number)
if even_number != sorted(even, reverse=True):
    print("Now your numbers are reversed and not equal each other: ")

even_number = sorted(even, reverse=True)
print(even_number)
print(even_number == even)

''' This is how to print s list which has two lists'''
print("****  This is how to print s list which has two lists ****")

even_1 = [2, 4, 6]
odd_1 = [1, 3, 5]
number_form = [even, odd]

for number_set in number_form:
    print(number_set)

    for value in number_set:
        print(value)
