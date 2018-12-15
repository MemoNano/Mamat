class TwoDoubleChars:
    """Given a string, return a string where for every char in the original, there two chars.
    """

    string1 = "The"
    count = 0
    ch = list

    newString = ""

    for char in string1:
        newString += char * 2

    print(newString)
