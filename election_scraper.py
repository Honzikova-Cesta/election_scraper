"""
election_scraper.py: třetí projekt do Engeto Online Python Akademie
author: Jan Procházka
email: jan.prochazka92@gmail.coms
discord: .honzikovacesta
"""

import argparse
import requests
from bs4 import BeautifulSoup
import csv
import sys

def get_nazev_okresu(url):
    #ziskani obsahu webove stranky
    response = requests.get(url)

    if response.status_code != 200:
        print('nepodařilo se načíst stránku kraje')
        return
    
    soup_kraj = BeautifulSoup(response.text, 'html.parser')

    jmeno_okresu = soup_kraj.find_all('h3')
    nazev_okresu = str(jmeno_okresu[1]).strip('</h3>').replace('\n', '').replace(':', '').strip('Okres: ')

    return nazev_okresu


def scrape_election_results(url, vychozi_soubor):

    #ziskani obsahu webove stranky
    response = requests.get(url)
 
    if response.status_code != 200:
        print('nepodařilo se načíst stránku kraje')
        return

    #soup objekt
    soup_kraj = BeautifulSoup(response.text, 'html.parser')

    #web scraping
    html = soup_kraj.find_all('td', {'class': 'cislo'})
    url_part = []
    
    for element in html:
        tag = element.find('a')
        if tag:
            url_part.append(tag['href'])

    list_url_obce = []
    for url in url_part:
        list_url_obce.append('https://volby.cz/pls/ps2017nss/'+ url)


    #csv
    header_csv_data = ['kód obce', 'název obce', 'voliči v seznamu', 'vydané obálky', 'platné hlasy']
    vsechny_strany = []
    
    #ziskani vsech kandidujicich stran
    link = list_url_obce[1]
    response = requests.get(link)
    if response.status_code != 200:
        print('nepodařilo se načíst stránku obce')
        return
    soup_strany = BeautifulSoup(response.text, 'html.parser')
    seznam_stran = soup_strany.find_all('td', {'class': 'overflow_name'})
    for strana in seznam_stran:
        vsechny_strany.append(strana.get_text())

    header_csv = header_csv_data + vsechny_strany

    csv_file_path = vychozi_soubor
    with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(header_csv)

    steps_done = 1
    total_steps = len(list_url_obce)

    #ocisteni a ulozeni jednotlivych dat do tabulky
    for link_obce in list_url_obce:
        response = requests.get(link_obce)
        if response.status_code != 200:
            print('nepodařilo se načíst stránku obce')
            return
        
        soup_obce = BeautifulSoup(response.text, 'html.parser')
        
        row_csv = []

        #kod obce
        parameters = link_obce.split('&')
        row_csv.append(parameters[2][6:])

        #nazev obce
        nazev_obce = soup_obce.find_all('h3')
        nazev_obce_ocisteny = str(nazev_obce[2]).strip('</h3>').replace('\n', '')
        row_csv.append(nazev_obce_ocisteny[6:])

        #volici v seznamu
        volici_v_seznamu = soup_obce.find('td', {'class': 'cislo', 'data-rel': 'L1'})
        volici_v_seznamu_rozdeleni = str(volici_v_seznamu).split('>')
        volici_v_seznamu_oprava = volici_v_seznamu_rozdeleni[1]
        pocet_volicu = []
        for char in volici_v_seznamu_oprava:
            if char.isdigit():
                pocet_volicu.append(char)
        pocet_volicu_ocisteno = ''.join(pocet_volicu)
        row_csv.append(pocet_volicu_ocisteno)

        #vydane obalky
        vydane_obalky = soup_obce.find('td', {'class': 'cislo', 'headers': 'sa3', 'data-rel': 'L1'})
        vydane_obalky_rozdeleni = str(vydane_obalky).split('>')
        vydane_obalky_oprava = vydane_obalky_rozdeleni[1]
        pocet_vydanych_obalek = []
        for char in vydane_obalky_oprava:
            if char.isdigit():
                pocet_vydanych_obalek.append(char)
        pocet_vydanych_obalek_ocisteno = ''.join(pocet_vydanych_obalek)
        row_csv.append(pocet_vydanych_obalek_ocisteno)

        #platne_hlasy
        platne_hlasy = soup_obce.find('td', {'class': 'cislo', 'headers': 'sa6', 'data-rel': 'L1'})
        platne_hlasy_rozdeleni = str(platne_hlasy).split('>')
        platne_hlasy_oprava = platne_hlasy_rozdeleni[1]
        pocet_platne_hlasy = []
        for char in platne_hlasy_oprava:
            if char.isdigit():
                pocet_platne_hlasy.append(char)
        pocet_platne_hlasy_ocisteno = ''.join(pocet_platne_hlasy)
        row_csv.append(pocet_platne_hlasy_ocisteno)

        #vysledky kandidujicich stran
        kandidujici_strany_part_one = soup_obce.find_all('td', {'class': 'cislo', 'headers': 't1sa2 t1sb3'})
        kandidujici_strany_part_two = soup_obce.find_all('td', {'class': 'cislo', 'headers': 't2sa2 t2sb3'})
        kandidujici_strany = kandidujici_strany_part_one + kandidujici_strany_part_two
        for strana in kandidujici_strany:
            strana_rozdeleni = str(strana).split('>')
            strana_oprava = strana_rozdeleni[1]
            pocet_stran = []
            for char in strana_oprava:
                if char.isdigit():
                    pocet_stran.append(char)
            pocet_stran_ocisteno = ''.join(pocet_stran)
            row_csv.append(pocet_stran_ocisteno)

        #zapsani radku (row_csv) do tabulky
        with open(csv_file_path, mode='a', newline='', encoding='utf-8') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(row_csv)

        sys.stdout.write('\r' + f'zpracovávám data po řádcích: {steps_done}/{total_steps}' )
        steps_done += 1 

    print('\nstahování dokončeno')

    return vychozi_soubor


if __name__ == "__main__":

    #definice argumentu prikazove radky
    parser = argparse.ArgumentParser(description='skript pro scraping volebních výsledků')
    parser.add_argument('url', help='odkaz na stránku s volebními výsledky (např. "https://volby.cz/...")')
    parser.add_argument('vystupni_soubor', help='název výstupního souboru (např. data.csv)')

    #zpracovani argumentu
    args = parser.parse_args()
    
    #nazev okresu podle zadane url
    nazev_okresu = get_nazev_okresu(args.url)

    #spusteni scrapingu
    print(f'stahuji data z: {args.url}')
    scrape_election_results(args.url, args.vystupni_soubor)
    print(f'volební výsledky pro {nazev_okresu} byly úspěšně uloženy do souboru: {args.vystupni_soubor}')
    #zpracování argumentů
    args = parser.parse_args()

    #spuštění scrapingu
    scrape_election_results(args.link, args.output_file)'''
