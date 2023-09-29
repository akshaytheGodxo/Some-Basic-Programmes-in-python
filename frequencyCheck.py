a = input("Enter the sentence : ")
b = input("Enter the character : ")
count = 0
for i in a:
    if i == b:
        count += 1
    else:
        pass
print("This character occured : ", count , " times")