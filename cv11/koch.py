from turtle import forward,left,right,exitonclick,speed

def koch(level, size):
	''' Vykresli kochovu vlocku urovne `level` s delkou strany `size` '''
	# pro pochopeni rekurzivnich volani se muze hodit vypisovat si stav pri kazdem vstupu do funkce
	# pro pozastaveni lze pouzit input()
	# a nebo lze program krokovat vyuzitim nastroju VS Code
	# print(f"Level: {level}, size: {size}")
	# input()

	# koncova podminka - vzdy by mela byt prvni a nikdy nesmi chybet
	if level == 0:
		forward(size)
		return

	# rekurzivni volani sebe sama
	koch(level-1,size/3)
	left(60)
	koch(level-1,size/3)
	right(120)
	koch(level-1,size/3)
	left(60)
	koch(level-1,size/3)

speed(0)
koch(3,500)
exitonclick()
