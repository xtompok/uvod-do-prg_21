import json

# Nacteni jsonu z retezce
adict = json.loads('{"key":12}')	# adict je obycejny Pythoni slovnik
print(adict['key'])
adict['key2']=None

# Prevod Pythoniho slovniku do json stringu a jeho vypis
print(json.dumps(adict))		

# Zapis JSONu do souboru
with open("output.json","w") as f:
	json.dump(adict,f)
