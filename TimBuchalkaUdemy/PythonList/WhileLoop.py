for i in range(10):
    print("For loop is executed :{}".format(i))

print("\n After For loop \n While loop is starting: \n")

i = 0
while i < 10:
    print("While loop is executed :{}".format(i))
    i = i + 1

available_exits = ["east", "north east", "south"]

chosen_exit = ""
chosen_exit_try = 0

while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction: ")
    if chosen_exit == "quite":
        print("Game Over !!! ")
        break

    if chosen_exit in available_exits:
        print("Aren't you glad you got out of there {}")
