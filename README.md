# election_scraper

Tento skript je určen k automatickému stahování volebních výsledků z roku 2017. Pomocí něj můžete snadno uložit informace o výsledcích voleb pro konkrétní okresy.
**Odkaz:** [zde](https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ)

## Použití
1. **Instalace knihoven**: Nejprve je třeba nainstalovat potřebné knihovny. Doporučuji provádět ve virtuálním prostředí. V terminálu spusťte následující příkaz:
  >pip --version                      
   pip install -r requirements.txt'''

2. **Spuštění skriptu**: Skript spustíte z příkazové řádky s následujícím příkazem:
'''bash
python election_scraper.py URL VYSTUPNI_SOUBOR'''
Kde `URL` je odkaz na stránku s volebními výsledky a `VYSTUPNI_SOUBOR` je název souboru, do kterého budou výsledky uloženy.

3. **Výsledky**: Po úspěšném provedení skriptu budou výsledky uloženy v zadaném výstupním souboru ve formátu CSV.

## Ukázka
Výsledky hlasování okresu Prostějov:
  1.argument: '''bash"https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103"'''
  2.argument: '''bash vysledky.csv'''

2. **Spuštění scriptu**:
'''bash
python election_scraper.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103" vysledky.csv
'''
3. **Průběh stahování**:
'''bash stahuji data z: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103
zpracovávám data po řádcích: 97/97
stahování dokončeno
volební výsledky pro Prostějov byly úspěšně uloženy do souboru: vysledky.csv '''

**Částečný výstup**:
'''bash kód obce,název obce,voliči v seznamu,vydané obálky...
506761,Alojzov,205,145...
589268,Bedihošť,834,527...
...
590240,Želeč,436,278...'''

## Poznámky
- Tento skript byl vytvořen pro vzdělávací účely a pro osobní použití.

## Autor
Jan Procházka




