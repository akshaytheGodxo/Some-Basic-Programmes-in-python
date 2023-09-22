n = int(input("Enter the number : "))
m = n
ans = 0
i = 0

while n != 0:
    s = n%10
    ans = ans*10 + s
    n = n//10
if m==ans:
    print("Palinderome")
else:
    print("Not a Palinderome")