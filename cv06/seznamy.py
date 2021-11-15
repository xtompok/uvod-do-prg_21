l = ["a",2,None,True,"asd"]	# Seznam nemusí mít všechny prvky stejného typu
print(f"L:{l}")	
print(l[2:4])			# Vypsání podseznamu (2. prvek tam patří, 4. už ne)
l.append("Posledni")		# Přidání na konec seznamu
print(f"L:{l}")			
print(l.pop())			# Odebrání z konce seznamu
print(f"L:{l}")
del l[3]			# Smazání prvku s indexem 3
print(f"L:{l}")
l[1] = l[1]+4			# Změna prvku s indexem 1
print(f"L:{l}")

# Funkce, která vrací více hodnot, je vrací jako n-tici (tuple)
def f():
	return 1,5,"Ahoj"

print(type(f()))
# N-tici lze rovnou "rozbalit" do proměnných, když známe dopředu její délku
cislo1, cislo2, ret1 = f()	
print(f"Cislo1: {cislo1}, cislo2: {cislo2}, ret: {ret1}")