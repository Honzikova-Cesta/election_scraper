# election_scraper

Tento skript je určen k automatickému stahování volebních výsledků z roku 2017. Pomocí něj můžete snadno uložit informace o výsledcích voleb pro konkrétní okresy.
**Odkaz:** [zde](https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ)

## Použití
1. **Instalace knihoven**: Nejprve je třeba nainstalovat potřebné knihovny. Doporučuji provádět ve virtuálním prostředí. V terminálu spusťte následující příkaz:
  >pip --version<br>
   pip install -r requirements.txt

2. **Spuštění skriptu**: Skript spustíte z příkazové řádky s následujícím příkazem:
   
>python election_scraper.py URL VYSTUPNI_SOUBOR

Kde `URL` je odkaz na stránku s volebními výsledky a `VYSTUPNI_SOUBOR` je název souboru, do kterého budou výsledky uloženy.

3. **Výsledky**: Po úspěšném provedení skriptu budou výsledky uloženy v zadaném výstupním souboru ve formátu CSV.

## Ukázka
1. **Zadání argumentů**:
   
  >1.argument: "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103"<br>
  2.argument: vysledky.csv

2. **Spuštění scriptu**:

>python election_scraper.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103" vysledky.csv

3. **Průběh stahování**:
>stahuji data z: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103<br>
zpracovávám data po řádcích: 97/97<br>
stahování dokončeno<br>
volební výsledky pro Prostějov byly úspěšně uloženy do souboru: vysledky.csv<br>

4. **Částečný výstup**:
>kód obce,název obce,voliči v seznamu,vydané obálky...<br>
506761,Alojzov,205,145...<br>
589268,Bedihošť,834,527...<br>
...<br>
590240,Želeč,436,278...

## Poznámky
- Tento skript byl vytvořen pro vzdělávací účely a pro osobní použití.

## Autor
Jan Procházka




