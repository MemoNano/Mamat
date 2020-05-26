class MoreAboutRanges:
    """More about RANGES and Slice:  Basically these two code snippet doing same thing
         Firs one is Slice and second one regular forloop"""
    r = range(0, 100)
    print(r)

    for i in r[::-2]:
        print(i)

    print("*" * 60)
    for i in range(99, 0, -2):
        print(i)

    print("*" * 60)

    print(range(0, 100)[::-2] == range(99, 0, -2))

    for i in range(0, 100, -2):
        print(i)

    print("{}: This is how to reverse whole String in Python: {}".format("* " * 15, "* " * 15))
    name = "Python is very powerfull language and it is pretty fast: "

    backString = name[::-1]
    print(backString)

    print(backString[::-1])

    """
    Experiment with different ranges and slices to get a feel for how they work.
    Remember that you can print the range as well as iterating through it to print
    Its values, to check that your ranges are what you expected.
    You may also want to include things like.
    """
    o = range(0, 100, 4)
    print(o)
    p = o[::5]
    print(p)
    for i in p:
        print(i)

    """"
    And see if you can work out what wil be printed before running the program. If you are unsure,
    use a for loop to print out the value of o to see why p return what it does.
    """

    my_weekdays = ['Monday', "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    for i in my_weekdays:
        print(i, end="\t")

    my_numbers = range(0, 1000, 5)
    for i in my_numbers:
        print(i, end="\t")

    my_iter = iter(my_weekdays)
    print(next(my_iter))
    print(next(my_iter))
    print(next(my_iter))
    print(next(my_iter))
    print(next(my_iter))
    print(next(my_iter))
    print(next(my_iter))

    my_list = ["hello", "world", "Python", "best"]
