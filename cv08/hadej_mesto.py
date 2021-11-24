import random

mesta = ["Praha", "Brno", "Bakov nad Jizerou"]
hledane = random.choice(mesta)				# Vybereme město náhodně

#print(hledane)

# Vytvoříme seznam plný podtržítek o stejné délce, jako hledané město
# Buď pomocí převedení stringu na list
uhadnuto = list("_"*len(hledane))
# Nebo jako list comprehension
uhadnuto = ["_" for pismeno in hledane]


print("".join(uhadnuto))
while True:
	pismeno = input("Zadej pismeno:")
	# Procházíme seznam s podtržítky
	for (idx, hpis) in enumerate(uhadnuto):
		# Pokud je na dané pozici podtržítko a tipnuté písmeno je shodné s písmenem, co na tuto pozici patří
		if hpis == "_" and pismeno.lower() == hledane[idx].lower():
			# Nahradíme podtržítko písmenem z města (aby mělo správnou velikost)
			uhadnuto[idx] = hledane[idx]
	print("".join(uhadnuto))
	# Pokud už nejsou žádná podtržítka k nahrazování, končíme
	if "_" not in uhadnuto:
		break

