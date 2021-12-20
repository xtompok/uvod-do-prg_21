# importujeme funkci read_int z našeho modulu ui.py
# pro snadne vyuziti by mely byt moduly ve stejne slozce jako hlavni kod
from ui import read_int

a = read_int("Zadej celé číslo")

print(a)

# import konstanty z modulu
from ui import PI

print(PI)
