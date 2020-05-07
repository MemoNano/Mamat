""" Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate
 to the message. Hint: How does an even / odd number react different when divided by 2? """

user = int(input("Please enter your number1 to check it is Odd or Even?: "))
user2 = int(input("Please enter your number2 to check it is Odd or Even?: "))


def check_even_odd_number(user_num, user_num2):
    if user_num % 2 == 0 and user_num % 4 == 0:
        return "Hoorey You are Lucky guy and your number is: {}".format(user_num)
    elif user_num % user_num2 == 0:
        return "Your first number is evenly divisible by second number: {}/{}".format(user_num, user_num2)
    elif user_num % 2 == 0:
        return "Your number is even: {}".format(user_num)
    if user_num % 2 != 0:
        return "Your number is odd: {}".format(user_num)


print(check_even_odd_number(user, user2))
