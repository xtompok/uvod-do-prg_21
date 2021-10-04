from math import sqrt

strana_ctverce = -3
if strana_ctverce < 0:
	print("Strana čtverce má být nezáporná")
elif strana_ctverce > 10:
	print("Strana čtverce je moc velká")
else:
	print("Čtverec o straně",strana_ctverce,"má obsah",strana_ctverce**2,
	"a obvod",strana_ctverce*4)

print("Pokračuji dál")