# candies and children
# In this programme , we have to take no. of students and candies as the input 
# If the no of candies assigned to a child is equal to the rank/row value of the children , he/she will be happy
# If all the childrens are satisfied/happy we have to print "Yes" , else print "No" :D Good Luck !!!

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
