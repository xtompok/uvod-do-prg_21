# Zdroj dat: https://opendata.praha.eu/dataset/parkoviste
import csv	# Modul pro práci s CSV soubory

# Lze otevřít více souborů najednou, jednotlivé open(...) as <promenna> oddělovat čárkou
# Pokud je třeba zalomit řádek někde, kde se to Pythonu nelíbí, je možné na konec řádku
# jako poslední znak přidat \ a za ním řádek zalomit (viz níže)
with open("parkoviste.csv", encoding="utf-8") as csvinfile,\
	open("parkoviste_out.csv", "w", encoding="utf-8") as csvoutfile:
	# Vytvoříme proměnnou `reader` držící objekt pro čtení z `csvinfile`
	reader = csv.reader(csvinfile, delimiter = ";")
	# Vytvoříme proměnnou `writer` držící objekt pro zápis do `csvoutfile`
	writer = csv.writer(csvoutfile)
	# next(<iterator>) vrátí další položku iterátoru
	# iterátorem je například range, nebo reader objekt z csv. 
	# List a string iterátory nejsou.
	next(reader)
	total = 0			# Celkový součet parkovacích míst na P+R
	for row in reader:		# Čteme jednotlivé řádky z `reader`u, v `row` máme seznam buněk daného řádku
		print(f"{row[0]}: {row[4]}")
		if row[3] == "True": 	# modul `csv` nepřevádí datové typy, obsah každé buňky je string 
			writer.writerow([row[0],row[4]])	# Do výstupního souboru ulož řádek obsahující 2 buňky
			try:
				total += int(row[4])		# Kratší forma zápisu
				#total = total + int(row[4])	# Delší forma zápisu, dělá to samé, co kratší
			except ValueError:
				pass
	print(f"Celkem {total} parkovacich mist na P+R parkovistich")