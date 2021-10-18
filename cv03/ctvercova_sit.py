from turtle import forward, left, right, exitonclick

nx = int(input("Zadej počet sloupců: "))
ny = int(input("Zadej počet řádků: "))
a = 30

for _ in range(ny):
	for _ in range(nx):
		# Nakresli čtverec
		for _ in range(4):
			forward(a)
			left(90)
		# Posuň se na další
		forward(a)
	# Vrať se na začátek řádku
	left(180)
	forward(nx*a)
	right(90)
	# Posuň se na další sloupec
	forward(a)
	right(90)

exitonclick()
