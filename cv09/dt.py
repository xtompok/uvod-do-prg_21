# Modul datetime obsahuje tridy pro praci s datem a casem
# date - umi pracovat s daty (bez casu)
# datetime - umi pracovat s daty a casy
# timedelta - umi pracovat s rozdily casu a dat
from datetime import date, timedelta

# Vypis vsech dat mezi memdate a adate
memdate = date(year=2000, month=12, day=9)	# Vytvorime objekt typu date
adate = date(year=2001, month=1, day=13)
delta = (adate-memdate)				# Odectenim dvou dat nam vyjde timedelta
print(delta.days)
for d in range(delta.days):
	print(memdate + timedelta(days=d))	# Sectenim data a timedelty nam vyjde datum
