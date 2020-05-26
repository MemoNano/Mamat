class IteratorPractice:
    string = "1234567890"
    """for loop using iterable object it automatically stop the iter"""
    for char in string:
        print(char, end=" ")

    """
        How to print using iter() and right way to use it.
    """
    my_iterator = iter(string)
    print("\n{}".format(my_iterator))
    print(next(my_iterator))
    print(next(my_iterator))
    print(next(my_iterator))
    print(next(my_iterator))
    print(next(my_iterator))
    print(next(my_iterator))
    print(next(my_iterator))
    print(next(my_iterator))
    print(next(my_iterator))
    print(next(my_iterator) + "\n ***********   next loop is starting   ***************")

    """
    Create a list of items (you may use either strings or numbers in the list), 
    Then create an iterator using the iter() functions.
    
    Use a for loop to loo "n" times, where n is the number of items in your list.
    Each time round the loop, use next() on your list to print the next item.
    
    Hint: Use the len() function rather than counting the number of items in the list.
    """

    my_list = ["boots", 1, "coat", "T-Shirt", "Laptop", "Desktop", "Desk", "CellPhone", "HeadPhone"]

    my_iterator2 = iter(my_list)
    for item in range(0, len(my_list)):
        next_item = next(my_iterator2)
        print(next_item)

    print("\n\n Regular for loop result is same :")
    for i in my_list:
        print(i)
