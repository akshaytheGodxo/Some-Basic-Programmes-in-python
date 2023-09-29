#Checking if a string is a palinderome or not

a = input("Enter the String : ")

start = 0
end = len(a)-1
count = 0
while start <= end:
    if a[start] != a[end]:
        print("Not a Palinderome")
        break
    start +=1 
    end -= 1
    
else:
    print("Palinderome")