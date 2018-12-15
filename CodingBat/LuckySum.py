class LuckySum(object):
    pass

    my_list = [12, 35, 12, 100, 13, 56]

    def lucky_sum(a, b, c, d, e):
        sum1 = 0
        list1 = [a, b, c, d, e]
        for i in list1[:list1.index(13)]:
            sum1 += i
        return sum1

    print(lucky_sum(12, 3, 45, 13, 45))

    # def fix_teen(self, num):
    #
    #     list1 = [13, 14, 17, 18, 19]
    #     return self.num if self.num not in list1 else 0
    #
    # def no_teen_sum(self, a, b, c):
    #     return fix_teen(self.a) + fix_teen(self.b) + fix_teen(self.c)
    #
    # print(no_teen_sum(1, 2, 3))

    a = 1
    b = 23
    c = 2

    def close_far(a, b, c):
        return (abs(abs(b) - abs(c)) >= 2) and \
               ((abs(abs(b) - abs(a)) <= 1 and abs(abs(c) - abs(a)) >= 2)
                or (abs(abs(c) - abs(a)) <= 1 and abs(abs(b) - abs(a)) >= 2))

    print(close_far(a, b, c))
