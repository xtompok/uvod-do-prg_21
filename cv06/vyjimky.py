def podel(a,b):
	return a/b
# Výjimku `ZeroDivisionError` lze odchytit již zde.
# Pokud se tak nestane, propadne výjimka do volající funkce.
#	try:
#		res = a/b
#	except ZeroDivisionError:
#		res = 2000
#	return res

def vydel_nulou(a):
	return podel(a,0)
# Výjimku `ZeroDivisionError` lze odchytit i zde.
# Pokud se tak nestane, propadne výjimka do volající funkce.
#	try:
#		res = podel(a,0)
#	except ZeroDivisionError:
#		res = 1000
#	return res

try:
	# Blok, ve kterém se odchytává případná výjimka
	print(vydel_nulou(int(input("Zadej cislo"))))
# Kdybychom ani tady nechytili výjimku `ZeroDivisionError`, program spadne
except ZeroDivisionError:
	# Blok odchycující `ZeroDivisionError`
	print("Nulou dělit nelze")
except ValueError:
	# Blok odchycující `ValueError`
	print("Nezadal jsi číslo")
else:
	# Blok vykonaný, pokud ve `try` bloku nenastala výjimka
	# Vykoná se před finally
	# Pokud v něm nastane výjimka, neodchycuje se, ale propadne výš
	pass
finally:
	# Blok vykonaný, ať už výjimka nastala nebo ne
	# Vykoná se, i když bylo v `try` nebo jinde `return`
	pass


# Varianta přístupu - pokud uživatel nezadá validní vstup, zvolím výchozí hodnotu
# Potřeba na toto uživatele upozornit
try:
	val = int(input("Zadej cislo: "))
	print("Ahoj")
except ValueError:
	print("Nebylo zadáno číslo, volím 42.")
	val = 42
print(f"Bylo zadáno číslo {val}")