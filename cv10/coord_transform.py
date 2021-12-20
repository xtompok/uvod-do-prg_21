#importujeme třídu Transformer z modulu PyProj
from pyproj import Transformer

# objekt pro transformaci z WGS-84 (EPSG:4326) do S-JTSK (EPSG:5514)
# always_xy říká, že vždy bude první osa x a druhá osa y, i když se to u některých systémů používá naopak
wgs2jtsk = Transformer.from_crs(4326,5514,always_xy=True)
jtsk2wgs = Transformer.from_crs(5514,4326,always_xy=True)

# transformace konkrétních souřadnic, funkce vrací dvojici (x,y)
out = wgs2jtsk.transform(15,50)


print(out)
# kontrola, že transformací tam a zpět vyšlo to samé
# ve skutečnosti se čísla liší, protože výpočty s floaty nejsou přesné
print(jtsk2wgs.transform(*out))
