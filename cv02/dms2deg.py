# Převod DMS na D.D

deg = input("Zadej stupně: ")
deg = int(deg)
if (deg < 0) or (deg >=360):
	print("Stupně musí být v rozsahu <0,360)")
	exit()

amin = input("Zadej minuty: ")
amin = int(amin)
if (amin < 0) or (amin >=60):
	print("Minuty musí být v rozsahu <0,60)")
	exit()

sec = input("Zadej vteřiny: ")
sec = float(sec)
if (sec < 0) or (sec >=60):
	print("Vteřiny musí být v rozsahu <0,60)")
	exit()

deg_float = deg + amin/60 + sec/3600

print("Celkem",deg_float,"stupňů")
