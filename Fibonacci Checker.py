n = int(input("Enter the range : "))

a = 0
b = 1
sum = 0
i = 0
print(a)
print(b)
while i < n-1:
    sum = a+b
    print(sum)
    a = b
    b = sum
    i += 1
