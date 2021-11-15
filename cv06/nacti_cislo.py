def read_int(prompt):
	""" Print prompt and return int from user.

	Prints prompt and then repeatedly asks user for input
	until user enters valid int.

	Arguments:
	prompt -- Prompt to be printed before user input

	Return value:
	Integer entered by user
	"""
	while True:
		try:
			astr = input(prompt)
			num = int(astr)
			print("Číslo ok")
			return num
		except ValueError:
			print("Nezadal jsi celé číslo")
		print("Za try blokem")
	
num = read_int("Zadej číslo: ")
print(f"Číslo je {num}")