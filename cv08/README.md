# Poznámky z 8. cvičení

## Užitečné funkce a moduly
Slovník má metodu [`setdefault(key,default)`](https://docs.python.org/3/library/stdtypes.html#dict.setdefault), která v případě, že klíč `key` ve slovníku je, tak vrátí jeho hodnotu a v opačném případě tento klíč vytvoří s hodnotou `default` a náledně tuto hodnotu také vrátí.

Pokud potřebujeme spočítat četnosti prvků v nějaké *iterable* (seznam, řetězec, ...), můžeme s výhodou využít třídu [`Counter`](https://docs.python.org/3/library/collections.html#collections.Counter) z modulu `collections`. `Counter(iterable)` vrátí slovníku podobný objekt, který pro klíče, které se v iterable vyskytovaly, vrátí jejich četnost a pro libovolný jiný klíč vrátí 0. 

## Příklady
### Hádej město
Program vybere ze seznamu měst jedno, které nechá uživateli hádat. Zobrazí
uživateli tolik podtržítek, jako má město počet písmen a nechá ho hádat písmeno.
Pokud se dané písmeno ve jméně města vyskytuje, program nahradí odpovídající
podtržítka za dané písmeno a znovu se ptá a to tak dlouho, dokud nejsou všechna
písmena ve jménu města uhádnuta. 

 - bonus 1 - zařiďte, aby nezáleželo na velikosti písmen
 - bonus 2 - seznam měst načítejte z CSV souboru

### Počet písmen ve slově (rozpracované)
Pro zadaný řetězec vypište, které znaky kolikrát obsahuje.

Doporučený postup:
- mám prázdný slovník
- pro písmeno ze slova:
  - je už ve slovníku?
    - ano -> zvyš jeho četnost (hodnotu) o 1
    - ne -> přidej ho do slovníku s četností (hodnotou) 1
- vypiš slovník
