class RunnerUp:
    if __name__ == '__main__':
        print("Please  enter how many number do you want to put int? : ")
        n = int(input())
        arr = map(int, input().split(' '))
        runner_up_list = arr
        reversed_num = list(runner_up_list)

        print(reversed_num)

        print(reversed_num.sort(reverse=True))

    n = [2, 3, 4, 5, 6]
    n.sort(reverse=True)
    print(n[1])