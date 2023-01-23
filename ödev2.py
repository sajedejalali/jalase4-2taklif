n = int(input("enter number : "))

a = 1
b = 1
sh = 1
sum = 2

print(" fib = ", end=" ")

while(sh <= n):
    sh += 1
    print(a , end=" , ")
    a = b
    b = sum
    sum = a + b