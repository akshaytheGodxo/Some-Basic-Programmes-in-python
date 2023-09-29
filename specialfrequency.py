n = input("Enter the sentence : ")
vowels = 0
spaces = 0
consonant = 0
numbers = 0

for i in n:
    if i in ('a' , 'e' , 'i' , 'o' , 'u') or i in ("A","E","I","O","U"):
        vowels += 1
    elif i == ' ':
        spaces += 1
    elif i in ('1' , '2' , '3' , '4' , '5' ,'6','7','8','9','0'):
        numbers += 1
    else:
        consonant += 1

print("Consonants are : " , consonant)
print("Numbers are : ", numbers)
print("Vowels are  : ", vowels)
print("Spaces are : ",spaces)