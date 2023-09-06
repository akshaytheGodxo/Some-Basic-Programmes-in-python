#Complete this question somehow to achieve the GOAT status 
#In this programme , we have to take no. of heads and legs from the user as input and return the amount 
#of goats and chickens that could fit in :D


legs = int(input("Enter no. of legs : "))
heads = int(input("Enter no. of heads : "))

chicks = legs // 2
legs = legs - chicks

h1 = abs(heads - chicks)
print("Chicks are , ",h1)

check = abs(heads - h1) < legs

goats = check * abs(heads - h1)
print("Goats are , ",goats)
