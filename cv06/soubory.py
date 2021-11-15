# Čtení ze souboru
# Použití operátoru `with open(...) as` zařídí, že na konci bloku se soubor korektně uzavře 
with open("/home/jethro/Dokumenty/prifuk/uvod-do-prg_21/cv06/soubor.txt", encoding="utf-8") as f:
#	obsah = f.read()	# Přečtení celého souboru naráz
#	print(obsah)
	for radek in f:		# Čtení souboru po řádcích
		print(f"Řádek: {radek.rstrip()}")

# Zápis do souboru
# mode="w" otevře soubor pro zápis, případný existující soubor stejného jména smaže
with open("/home/jethro/Dokumenty/prifuk/uvod-do-prg_21/cv06/soubor_out.txt", 
	mode="w", encoding="utf-8") as f:
	f.write("Ahoj")		# Zápis řetězce do souboru, nevkládá se automaticky nový řádek
