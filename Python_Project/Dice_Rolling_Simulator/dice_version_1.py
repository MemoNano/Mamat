# Module name Dice Rolling Simulator
import random


class DiceRolling():
    def __init__(self, min, max, user_num, dic_num):
        self.min = min
        self.max = max
        self.user_num = user_num
        self.dice_num = dic_num
    min = 1
    max = 7
    user_num = int(input('Please enter between 1 to 6 to play dice'))
    dice_num = [1, 2, 3, 4, 5, 6]

    while user_num < max:
        for i in range(1):
            print(random.randint(min, max))
            user_answer_yes_no()

        break

    def user_answer_yes_no(self):
        while True:
            user_ans = input('Do you want to roll again? Y(yes) or N(no)')
            if user_ans == '' or not user_ans[0].lower() in ['y', 'n']:
                print('Please answer with yes or no!')
                if user_ans == 'y':
                    print(random.randint(min, max))
                else:
                    break
