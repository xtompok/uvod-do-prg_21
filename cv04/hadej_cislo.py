from random import randrange

#for _ in range(100):
print(randrange(10),end=" ")

# Hadej cislo
# Program na zcatku zvoli nahodne cislo a pak se uzivatele pta na tip
# Pokud tip sedi, program skonci, jinak rekne, 
# jestli je hledane cislo vetsi nebo mensi nez tip 

hledane = randrange(10)
tip = -1

while tip != hledane:
	tip = int(input("Zadej cislo: "))
	if tip < hledane:
		print("male")
	elif tip > hledane:
		print("velke")
print("hotovo")

