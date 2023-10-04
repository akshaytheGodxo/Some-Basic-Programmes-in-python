n = int(input("Enter the number : "))
factor = 1
count = 0
con1 = False
con2 = False
st = ""
l = []
ultimate_condition= False

for i in range(1 , n+1):
    if n%i == 0:
        l.append(i)
print(l)
for i in range(1, len(l)-1):
    for j in range(1 , i+1):
        if l[i] % j == 0:
            count += 1
    if count == 1:
        con1 = True

    else:
        ultimate_condition = False
        con1 = False
        print("Not Strange !")
        break
    count = 0
if n**0.5 < l[-1]:
    con2 = True
if con1 == True and con2 == True:
    ultimate_condition = True

if ultimate_condition == True:
    print("Strange")