# candies and children

s = int(input("Enter no. of childrens : "))
c = int(input("Enter no. of candies : "))


count = 1
for i in range(1,s+1):
    if c >= s:
        count = count + 1
    c = c//i
if count >= s:
    print("Yes")
else:
    print("No")
