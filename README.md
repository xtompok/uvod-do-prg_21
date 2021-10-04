# Úvod do programování (2021 edition)
Zdrojové kódy a poznámky ke cvičení z Úvodu do programování.

[Stránky](https://web.natur.cuni.cz/~bayertom/index.php/9-teaching/10-uvod-do-programovani) přednášky.

Věci probírané na jednotlivých cvičeních najdete na [samostatné stránce](prubeh.md).
Cvičení probíhá rámcově podle kurzu [Nauč se Python!](https://naucse.python.cz/course/pyladies/).
[Dokumentace](https://docs.python.org/3/) k Pythonu 3.

Cvičení probíhá v jazyku Python 3. Možná jste se setkali, například na Programování pro GIS, s Pythonem 2, pak pozor, jazyky jsou podobné, ale ne stejné, například `print` v Pythonu 3 se vždy volá se závorkami.

## Požadavky na zápočet
Celkem budou zadány 4 domácí úkoly po 5, 5, 10 a 10 bodech, na zápočet je třeba získat alespoň 23 bodů. Každý domácí úkol bude mít i bonusové části, za které je možné získat body navíc. 

Účast na cvičení je dobrovolná, ale v případě přetlaku na konzultace budou mít přednost ti, kteří se cvičení účastní. 

[Bodování úkolů](./vysledky.md)

## Programové vybavení
### Interpret Pythonu
Ať už budeme používat jakékoli vývojové prostředí, je potřeba si nanistalovat interpret Pythonu 3 - program, který vezme váš zdrojový kód, přeloží ho do instrukcí srozumitelných vašemu počítači a postupně ho provádí. Interpret stáhnete například ze [stránek Pythonu](https://www.python.org/downloads/windows/)(zde `Latest Python 3 Release` a tam dole `Windows x86-64 executable installer`). Pokud používáte Linux nebo Mac OS a nevíte si rady, napište mi prosím. Při instalaci pak na úplně první obrazovce dole zaškrtněte `Add Python 3.9 to PATH`, což vám následně umožní Python snadno spouštět.
![instalator](https://docs.python.org/3/_images/win_installer.png)

### Vývojové prostředí
Vývojové prostředí je program, který nám umožní jednoduše editovat a spouštět zdrojové kódy a dívat se, co naše programy dělají. Jedno vývojové prostředí může být určeno pro více jazyků (Visual Studio Code), nebo jen pro jeden (PyCharm).

Na cvičení budeme programovat v Pythonu 3 v prostředí [Visual Studio Code](https://code.visualstudio.com/)(dále VSCode), stáhněte si ho a následně si ho nastavte pro Python dle [návodu](https://code.visualstudio.com/docs/languages/python). Pro nastavení je potřeba již mít nainstalovaný Python 3. Pro konzultace a rady bude používán [Visual Studio Code Live Share](https://visualstudio.microsoft.com/cs/services/live-share/), doporučuji si tedy nainstalovat [Live Share Extension Pack](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare-pack), lze to přímo z VSCode kliknutím na kostičky v levém sloupci. 

Další vhodné prostředí pro Python je [PyCharm](https://www.jetbrains.com/pycharm/), můžete si stáhnout zdarma dostupnou Community Edition. Můžete samozřejmě použít i jiná prostředí, pokud jsou vám bližší.

Pokud si potřebujete jen něco menšího vyzkoušet, tak není potřeba instalovat Python a vývojové prostředí, ale můžete si to vyzkoušet online na [Programiz online compileru](https://www.programiz.com/python-programming/online-compiler/). 

### Komunikace
Cvičení jsou (zatím) prezenční, konzultace jsou možné po cvičení nebo online, v takovém případě mi prosím napište [email](mailto:xtompok@gmail.com).   

## Tipy a rady pro čitelný kód
### Magické konstanty
Pokud ve svém kódu používáte nějaké konstanty, ať už matematické (např. pi),
fyzikální nebo jste si jen pevně zvolili délku seznamu či např. rozestup
rovnoběžek, je vhodné tyto konstanty na začátku programu pojmenovat a pak
používat toto pojmenování místo jejich číselné hodnoty. Je pak jasné, co je v
daném místě sémanticky myšleno a pokud se nějakou z konstant později rozhodntete
změnit, lze to udělat snadno na jednom dobře definovaném místě.

Konstanty se obvykle pojmenovávají velkými písmeny, víceslovné se oddělují
podtržítkem. Např. `LIST_LEN` pro délku seznamu (pokud v programu je více
seznamů různých délek, je vhodné přidat do jména jednoznačný identifikátor, ke
kterému seznamu se konstanta vztahuje), `F_G = 9.81` pro gravitační zrychlení na
Zemi, `REC_DEPTH` pro hloubku rekurze. Pokud konstantu importujete z nějakého
modulu, nechte ji takové jméno, jaké má v daném modulu (např. `from math import
pi)`.

