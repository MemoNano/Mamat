user_num = int(input("Please enter how many numbers would like in your Fibonacci sequence:"))

count = 1

if user_num == 0:
    fibonacci = []
elif user_num == 1:
    fibonacci = [1]
# elif user_num == 2:
#     fibonacci = [1,1]
elif user_num > 2:
    fibonacci = [1, 1]
    while count < fibonacci[user_num - 1]:
        fibonacci.append[fibonacci[count] + fibonacci[count + 1]]
        count += 1
print(fibonacci)
