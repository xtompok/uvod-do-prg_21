from collections import Counter
STRING = "abeceda"

# Varianta 1 - bez specialnich znalosti
cetnosti = {}
for pismeno in STRING:
	if pismeno in cetnosti:
		#cetnosti[pismeno] = cetnosti[pismeno] + 1
		cetnosti[pismeno] += 1
	else:
		cetnosti[pismeno] = 1
print(cetnosti)

# Varianta 2 - vyuziti metody setdefault u slovniku
for pismeno in STRING:
	cetnosti[pismeno] = cetnosti.setdefault(pismeno,0) + 1

# Varianta 3 - vyuziti tridy Counter z modulu collections
cetnosti = Counter(STRING)
print(cetnosti)
