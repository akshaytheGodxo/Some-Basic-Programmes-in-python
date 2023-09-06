#As the name suggests , we have to take a decimal number as an input and convert it to its binary form :D

n = int(input("Please Enter the number : "))

ans = 0
i = 0

while n != 0:
    bit = n&1
    n = n//2
    ans = (bit * (10 ** i)) + ans
    i = i+1

print("Binary value is  :   " ,ans)