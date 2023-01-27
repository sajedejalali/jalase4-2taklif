import random


while True:
    op = input("c for continue & e for exit ")
    if op == "e" :
        break

    else:
        n = int(input("enter number : "))
        sum = []

        while True:
            num = random.randint(0, 1000)
            if num in sum:
                continue
            else:
                if len(sum) == n :
                    break
                else :
                    sum.append(num)
        print(sum)
    