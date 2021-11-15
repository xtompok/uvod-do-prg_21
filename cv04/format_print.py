jmeno = input("Zadej jmeno\\\n")
vek = int(input(f"{jmeno}, zadej vek: "))
astr = f"Ahoj \"{jmeno}\", {vek} {{}} let stary"
print(astr)
print("\N{SMILING FACE WITH SMILING EYES}")
print("\U0001F60A")

pattern = "{poradi}: Toto je {poradi}. iterace cyklu"
for i in range(10):
	print(pattern.format(poradi=i))

a = 1/3
print(f"1/3 = {a:.3f}")
print(a*3)
