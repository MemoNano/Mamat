class CountHi:
    """
    Return the number of times that the string "hi" appears
    anywhere in the given string:

    """
    count1 = 0
    str1 = "456hello hi me hi yeshihekhi no onlkhi "

    for i in range(len(str1) - 1):
        if str1[i] == 'h' and str1[i + 1] == 'i':
            count1 += 1
    print(str1 + " {0}".format(count1))

    def cat_dog(str):
        return str.count("hi")

    print(cat_dog(str1))

    str2 = ""

    def how_toknow_is_digit(str1):
        return str1.isdigit()

    print(how_toknow_is_digit(str2))

    def is_string_printable(str1):
        return str1.isprintable()

    print(is_string_printable(str2))
