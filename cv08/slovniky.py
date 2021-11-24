# Vytvoření slovníku
slovnik = {'klic1': 'hodnota1', 'klic2': 'hodnota2'}

print(slovnik['klic1'])
# Vytvoření nového klíče a přiřazení hodnoty
slovnik['klic3'] = 'hodnota3'
print(slovnik)
# Změna hodnoty stávajícího klíče
slovnik['klic1']  = 42
print(slovnik)
# Smazání klíče
del slovnik['klic2']
print(slovnik)

# Implicitně se iteruje přes klíče
for key in slovnik:
	print(f"{key} -> {slovnik[key]}")

# Pomocí .values() můžeme iterovat přes hodnoty
for val in slovnik.values():
	print(f"value: {val}")

# Pomocí .items() můžeme iterovat přes dvojice (klíč, hodnota)
for (key,val) in slovnik.items():
	print(f"{key} -> {val}")

# Můžeme se ptát, zda je klíč ve slovníku
if 'klic1' in slovnik:
	print(slovnik['klic1'])

