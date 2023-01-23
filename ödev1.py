import random

n = int(input("enter number : "))
sum = []

for i in range(n):
    num = random.randint(0, 1000)
    sum.append(num)

print(sum)