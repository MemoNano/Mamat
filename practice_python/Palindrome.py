"""
Ask the user for a string and print out whether this string is a palindrome or not.
( A palindrome is a string that reads the same forwards and backwards.)
"""

# get every character with its index and compare them each other.

#  CIVIC  -->  list(civic) index[0] == index[len(list)-1]


list_input = list(input("Please input your string: ").lower().replace(' ', ''))

length = len(list_input)-1

if list_input[0] == list_input[length]:
    for i in list_input:
        if i == list_input[:length]:
            i = i + 1
            length = length - 1

    print("your string is palindrome {}".format(list_input))
else:
    print("Your string is NOT palindrome {}".format(list_input))

