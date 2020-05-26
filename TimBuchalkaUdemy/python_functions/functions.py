def python_food():
    width = 80
    text = "Spam and Eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


def centre_text(*args, sep=' '):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    return " " * left_margin + text


# with open("centred", mode='w') as centred_file:
#     # call the function
#     print(centre_text("spam and eggs",))
#     print(centre_text(12))
#     print(centre_text("spam, spam and eggs"))
#     print(centre_text("spam, spam, and spam"))
#     print(centre_text("first", "second", 3, 4, "spam", sep=":"))
#
#     print("=" + str(12 * 3))
#     print(["b", "d", "c", 'e'])


with open("menu", mode='w') as menu:
    # call the function
    s1 = centre_text("spam and eggs")
    print(s1, file=menu)
    s2 = centre_text(12)
    print(s2, file=menu)
    s3 = centre_text("spam, spam and eggs")
    print(s3, file=menu)
    s4 = centre_text("spam, spam, and spam")
    print(s4, file=menu)
    s5 = centre_text("first", "second", 3, 4, "spam", sep=":")
    print(s5, file=menu)
