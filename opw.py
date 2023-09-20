n = int(input("Enter the num " ))

sum = 0
while n >= 0:
    if n%2 == 0:
        sum += n
    n -= 1
print("Sum of all even values is ",sum)
