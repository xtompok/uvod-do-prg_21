# Poznámky ze 3. cvičení

## For cyklus
Proměnnou ve for cyklu obvykle označujeme `i`, pokud je více zanořených cyklů, pokračujeme dále v abecedě (`j`,`k`,...).

Pokud operujeme s objekty v rovině, je vhodné si proměnné ve for cyklech označovat `x` a `y`, pak víme, ve kterém rozměru se pohybujeme.
Např. `for x in range(nx)`

Pokud iterační proměnnou v cyklu vůbec nepotřebujeme, můžeme ji nahradit podtržítkem `_`. Pak se k její hodnotě nemůžeme nijak dostat a každé použití podtržítka vytvoří jinou "virtuální" proměnnou, tedy pokud dva vnořené cykly používají oba podtržítko, tak se chovají stejně, jako kdyby jeden měl iterační proměnnou `i` a druhý `j`.

## While cyklus
Pokud napíšete cyklus, který nikdy neskončí, dá se program ukončit pomocí Ctrl-C. Pomocí Ctrl-C se dá program ukončit (skoro) vždy.

## `break`
V obou typech cyklů můžete použít příkaz `break`, který způsobí okamžité ukončení aktuálního cyklu. V případě, že je příkaz `break` použit ve vnořeném cyklu, vyskočí jen "o úroveň výš" a vnější cykly se dále vykonávají.

## Želva
Funkce `speed(<rychlost>)` nastaví rychlost želvy
  * 0 - tak rychle, jak váš počítač umí
  * 10 - rychle
  * 9--2 - něco mezi
  * 1 - pomalu

## Příklady

### Příklad 1
Nakreslete želvou čtvereček o straně `a`

### Příklad 2
Nakreslete šestiúhelník o straně `a`

### Příklad 3
Nakreslete 7 šestiúhelníků do "kytičky"

### Příklad 4a
Nakreslete čtvercovou síť o `nx` x `ny` polích, na `nx` a `ny` se zeptejte uřivatele

### Příklad 4b
Nakreslete šestiúhelníkovou síť o `nx` x `ny` polích, na `nx` a `ny` se zeptejte uživatele

### Příklad 5
Napište hru hádání čísla. Program se ptá uživatele, aby zadal svůj tip na číslo. Pokud uživatel číslo uhádne, pak program skončí. Pokud se uživatel netrefí, pak program napíše, zda uživatel tipoval moc velké nebo moc malé číslo.

Příklad:
```
Zadej číslo: 10
Moc velké
Zadej číslo: 3
Moc malé
Zadej číslo: 7
Vyhrál jsi!
```
