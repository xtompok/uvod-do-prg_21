def read_int(prompt):
	"""
	Function prints prompt and reads integer.

	No exceptions are catched.

	Arguments:
	prompt -- Text to be printed before input from user

	Return value:
	Integer entered by user
	"""
	astr = input(prompt)
	return int(astr)

def print_float3(num):
	print(f"{num:.3f}")

def square_area(side):
	return side*side

side = 371
area = square_area(side)
print(f"Plocha ctverce o strane {side} je {area}")
print_float3(12.345566778)
num = read_int("Zadej cislo: ")
print(f"Zadal jsi {num}")
