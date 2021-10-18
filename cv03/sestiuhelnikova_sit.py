from turtle import forward,left, exitonclick, penup, pendown, speed, right

x = int(input("Zadej počet řádků: "))
y = int(input("Zadej počet sloupců: "))

for _ in range(x):
	# Nakresli řádek šestiúhelníků
	for _ in range(y):
		# Nakresli šestiúhelník a rovnou se posuň na začátek dalšího
		for _ in range(8):
			forward(30)
			left(60)
		# Natoč se, aby další správně navazoval
		right(120)

	# Otoč se čelem vzad
	right(120)
	# Vrať se na začátek sloupce
	for _ in range(y):
		forward(30)
		right(60)
		forward(30)
		left(60)
	# Posuň se na další sloupec
	right(120)
	forward(30)
	right(60)
	forward(30)
	right(60)

exitonclick()
