n = input("Enter the String : ")
count = 0
ncount = 0
for i in n:
    temp = i
    for j in n:
        if temp == j:
            count += 1
            
    if count >= 2:
        ncount +=1
    if ncount == 1:
        print(i , ":",count)
        continue
    else:
        print(i , ":" , count)
        ncount = 0
    count = 0
