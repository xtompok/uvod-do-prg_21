import requests

# URL zdroje dat
URL="https://mapa.pid.cz/getData.php"

# Stazeni dat ze serveru metodou GET (nejcasteji pouzivana)
r = requests.get(URL)
# Vypis status kodu (viz https://http.cat/)
print(r.status_code)
# Vypis kodovani (zpusobu prevodu textu do jednicek a nul)
print(r.encoding)
# Pokud server vraci JSON, muzeme ho dostat rovnou naparsovany
data = r.json()

# Prozkoumavani dat - zjistujeme, jaka je jejich struktura a co by nas z nich
# mohlo zajimat. Je to navod, jak postupovat, kdyz dostanete neznama data a
# zajima vas, co obsahuji. Pro dalsi cast programu tato cast neni nutna. 
print(type(data))
print(data.keys())
print(type(data['trips']))
print(data['trips'].keys())
print(data['trips']['389/2'])

# Ziskame seznam vozidel (klice pro nas nejsou zajimave)
vehicles = data['trips'].values()
#print(vehicles)
lines = {}
# Prochazime vozidla a jejich linkam pripocitavame pocty
for v in vehicles:
	key = v['route']
	lines[key] = lines.setdefault(key,0) + 1
# Vytiskneme linky a pocty vozidel na nich
print(lines)
