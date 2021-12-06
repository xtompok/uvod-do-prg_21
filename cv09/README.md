# Poznámky z 9. cvičení
## Užitečné moduly
Modul [json](https://docs.python.org/3/library/json.html) slouží pro snadné načítání dat ve formátu JSON ze souborů nebo řetězců a jejich opětovné ukládání zpět do souborů nebo řetězců. Pro zápis (ať už do souboru nebo do řetězce) jsou vhodné následující argumenty:
    - `ensure_ascii=False` - řetězce s háčky a čárkami budou vypadat normálně a nebudou v nich sekvence
se zpětným lomítkem
    - `indent=2` - soubor bude dobře čitelný i pro člověka, nejen pro program


Modul [requests](https://docs.python-requests.org/en/latest/) slouží pro snadné stahování dat z webu. Je potřeba ho nainstalovat pomocí `python -m pip install requests`, protože není ve standarních modulech Pythonu. 

## Příklady
### Počet písmen ve slově
Viz [minulé cvičení](../cv08/README.md).

### Počet vozidel na linkách PID
Program si stáhne [aktuální pozice vozidel PID](https://mapa.pid.cz/getData.php) a pro každou linku spočítá, kolik na ní jede aktuálně vozidel. 
