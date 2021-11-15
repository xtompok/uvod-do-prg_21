# 7. cvičení

## CSV
Modul [CSV](https://docs.python.org/3/library/csv.html) slouží pro práci se
soubory typu CSV, tedy textovými reprezentacemi tabulek.

Objekt pro čtení vyrobíme pomocí funkce
[`csv.reader`](https://docs.python.org/3/library/csv.html#csv.reader), seznam
jeho metod najdete [v
dokumentaci](https://docs.python.org/3/library/csv.html#reader-objects). Při
vytváření readeru se může hodit nastavit `delimiter` a `quotechar`.

Objekt pro zápis vyrobíme pomocí funkce
[`csv.writer`](https://docs.python.org/3/library/csv.html#csv.writer), seznam
jeho metod najdete [v dokumentaci](https://docs.python.org/3/library/csv.html#reader-objects).
Pokud výsledný soubor obsahuje prázdný řádek mezi každými dvěma řádky dat, pak
je vhodné přidat funkci `open`, která soubor otvírá, pojmenovaný argument
`newline=''`.

## Příklady
### 1) Kapacity parkovišť
Ze souboru, který stáhnete na https://opendata.praha.eu/dataset/parkoviste
vypište pro každé parkoviště jeho jméno a kapacitu

### 2) Celková kapacita parkovišť
Spočtěte celkovou kapacitu parkovišť ze souboru výše

### 2a) Celková kapacita P+R parkovišť
Spočtěte celkovou kapacitu parkovišť P+R ze souboru výše
