# Web Zdeňka Matušky — statický export

## Struktura
- index.html                homepage
- <slug>/index.html         17 podstránek
- style.css                 jediný stylopis (fonty + všechny třídy)
- script.js                 stránkování blogu, načítá se s defer
- images/                   obrázky
- fonts/                    fonty (nutno doplnit, viz níže)
- sitemap.xml, robots.txt

## Co je hotové
- vlastní <head> na každé stránce: title, description, canonical (https + www + koncové lomítko), og:*, twitter:card, lang="cs", charset, viewport
- JSON-LD: Person + WebSite na všech stránkách, BreadcrumbList na podstránkách, Article na článcích, FAQPage tam, kde FAQ skutečně je
- přesně jeden H1 na stránku, nadpisy bez přeskakování úrovní
- všechny odkazy absolutní https s www a koncovým lomítkem, nikde http:// ani ../
- nula inline stylů, žádná CDN knihovna, JS s defer
- žádné data-* atributy, žádné base64, žádné prázdné obaly
- lazy loading na všech obrázcích kromě prvního nad ohybem

## Co musíte doplnit

### 1. Fonty (8 souborů)
Stáhněte Poppins z https://gwfh.mranftl.com/fonts/poppins — váhy 400, 500, 600, 700,
podmnožiny latin a latin-ext, formát woff2. Uložte do /fonts/ pod těmito názvy:

  poppins-400-latin.woff2       poppins-400-latin-ext.woff2
  poppins-500-latin.woff2       poppins-500-latin-ext.woff2
  poppins-600-latin.woff2       poppins-600-latin-ext.woff2
  poppins-700-latin.woff2       poppins-700-latin-ext.woff2

Do stránek se nevolá fonts.googleapis.com — vše běží z vaší domény.

### 2. Obrázky (30 souborů)
Ve složce images/ je 10 souborů (loga, fotka, reference). Zbylých 30
je zatím na starém WordPressu — stáhněte je podle seznamu v _obrazky-ke-stazeni.txt
a uložte do images/ pod uvedeným názvem.

Doporučení: převeďte je do WebP a doplňte srcset. Konverzi jsem neprováděl,
originály jsou jpg/png.

### 3. Rozměry obrázků
width a height v HTML nejsou u všech obrázků — nemám skutečné rozměry souborů.
Doplňte je po stažení, jinak bude web skákat při načítání (CLS).

### 4. Placeholdery k doplnění
Na stránkách tvorby webů jsou tři placeholdery pro třetí realizaci:
[ZADANI_REPUTIVE], [RESENI_REPUTIVE], [VYSLEDEK_REPUTIVE].

## Nasazení
Nahrajte obsah této složky do rootu webu. Server musí umět servírovat
adresář jako index.html (Apache i nginx to umí ve výchozím nastavení).
