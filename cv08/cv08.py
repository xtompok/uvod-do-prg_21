"aha".split()) # převede string na seznam písmen
# Pokud split dostane jako argument řetězec, rozdělí string na seznam podřetězců podle argumentu jako oddělovače
"ah,a".split(',') == ['ah', 'a']

l = ["a","h","o","j"]

# Enumerate pro každou položku seznamu, který dostane jako argument, vrátí dvojici (index, hodnota položky)
for (idx, val) in enumerate(l):
	print(f"idx: {idx}, val: {val}")

# Ekvivalentní zápis bez použití enumerate
for idx in range(len(l)):
	val = l[idx]
	print(f"idx: {idx}, val: {val}")

