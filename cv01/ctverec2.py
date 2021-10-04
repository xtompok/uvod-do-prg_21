from math import sqrt

strana_ctverce = -3

# Osetreni zaporne delky strany
if strana_ctverce < 0:
	print("Strana čtverce má být nezáporná")
	quit()

# Osetreni moc velke delky strany
if strana_ctverce > 10:
	print("Strana čtverce je moc velká")
	quit()

# Samotny vypocet
print("Čtverec o straně",strana_ctverce,"má obsah",strana_ctverce**2,
	"a obvod",strana_ctverce*4)

print("Pokračuji dál")