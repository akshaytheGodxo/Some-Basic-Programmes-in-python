x = eval(input())

st1 = ""
st2 = ""
count = 0

#Prime Check Block
for i in x:
    for j in range(1 , int(i)+1):
        if int(i) % j == 0:
            count += 1
    if count == 2:
        st2 += i
    else:
        st1 += i
    count = 0
st2 = sorted(st2)

new_String = ""
new_String2 = ""
for i in st2:
    new_String += i
for j in st1:
    new_String2 += j
last_string = new_String + new_String2
print(f'"{last_string}"')