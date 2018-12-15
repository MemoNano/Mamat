class RangePractice:
    my_string = "abcdefghijklmnoprstuvwxyz"
    print(my_string.index('e'))
    print(my_string[4])

    small_decimals = range(0, 10)
    print(small_decimals)
    print(small_decimals[3])
    print(small_decimals.index(3))

    """
    Getting odd numbers  and getting specific odd number (which is getting 985th odd number)
    """
    odd = range(1, 10000, 2)
    print(odd)

    print(odd[985])

    print("********   This is how to program   **********")
    sevens = range(0, 1000000, 7)
    x = int(input("Please enter a positive number less than one million: "))
    if x in sevens:
        print("{} is divisible by seven(7)".format(x))
    else:
        print("Ops...{} is NOT divisible by seven(7)".format(x))

    print("********  Decimals  ***********")

    decimals = range(0, 100)
    print(decimals)

    my_range = decimals[3:40:3]
    print(my_range)

    for i in my_range:
        print(i)

    print(my_range == range(3, 40, 3))

    print(range(0, 5, 2) == range(0, 6, 2))

    """Printing out both list to see what's happening: That's why they are some and returning True."""
    print(list(range(0, 5, 2)))  # Output [0, 2, 4]

    print(list(range(0, 6, 2)))  # Output [0, 2, 4]
