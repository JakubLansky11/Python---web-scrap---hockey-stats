# Python project - web scrap
# Statistics from czech hockey league. 
# Data from: https://www.hokej.cz/tipsport-extraliga/zapasy

from requests import get
from bs4 import BeautifulSoup as bs
import csv
import sys

# Hlavní odkaz, ze kterého budou stahovány další odkazy, které poskytnou potřebné údaje. 
print("Ahoj. Vítej v programu, který umí stáhnout základní statistiky ze zápasů české hokejové extraligy.")
print("Najeď na stránku https://www.hokej.cz/tipsport-extraliga/zapasy a vyber zápas, jehož statistiky chceš stáhnout.")
print("Statistiky se uloží do souboru hokej-statistiky-zapas.csv v místě, kde máš uložený tento program.")
url_hlavni = input("Zadej link na zápas české hokejové extraligy: ")
tabulka_hokej = get(url_hlavni)
soup1 = bs(tabulka_hokej.text, "html.parser")
souhrn= soup1.find_all("table", {"class": "table-last-right"})
titulek = soup1.find("title").text
tymy = []
souhrn_tymy= soup1.find_all("h2", {"class": "short"})
for tym in souhrn_tymy:
    tymy.append(tym.text)
radek_0 = []
sloupec_cas = []
sloupec_tym = []
sloupec_gol = []
sloupec_asistence = []
sloupec_typ_golu = []
prazdny = []
radek_1 = ["Čas", "Tým", "Střelec gólu", "Asistence", "Typ gólu (přesilovka,..)", "Hráči u vstřeleného gólu", "Hráči u inkasovaného gólu"]

polozky_2 = []
for polozka in souhrn:
    jmeno = polozka.find_all("td")
    polozky_2.append(jmeno)
goly_prvni_tretina = polozky_2[0]
goly_druha_tretina = polozky_2[1]
goly_treti_tretina = polozky_2[2]
goly_cas = []
goly_tym = []
goly_strelci_upravit = []
goly_strelci = []
goly_asistence_upravit = []
goly_asistence = []
goly_typ = []
goly_typ_2 = []
goly_hraci_plus = []
goly_hraci_minus = []
max_index_1 = (len(goly_prvni_tretina))
nasobek_1 = int(max_index_1/7)
max_index_2 = (len(goly_druha_tretina))
nasobek_2 = int(max_index_2/7)
max_index_3 = (len(goly_treti_tretina))
nasobek_3 = int(max_index_3/7)

for x in range(0, nasobek_1):
    goly_cas.append(goly_prvni_tretina[0 + 7*x].text)
for x in range(0, nasobek_2):
    goly_cas.append(goly_druha_tretina[0 + 7*x].text)
for x in range(0, nasobek_3):
    goly_cas.append(goly_treti_tretina[0 + 7*x].text)
for x in range(0, nasobek_1):
    goly_tym.append(goly_prvni_tretina[1 + 7*x].text)
for x in range(0, nasobek_2):
    goly_tym.append(goly_druha_tretina[1 + 7*x].text)
for x in range(0, nasobek_3):
    goly_tym.append(goly_treti_tretina[1 + 7*x].text)
for x in range(0, nasobek_1):
    goly_strelci_upravit.append(goly_prvni_tretina[2 + 7*x].text)
for x in range(0, nasobek_2):
    goly_strelci_upravit.append(goly_druha_tretina[2 + 7*x].text)
for x in range(0, nasobek_3):
    goly_strelci_upravit.append(goly_treti_tretina[2 + 7*x].text)
for strelec in goly_strelci_upravit:
    goly_strelci.append(strelec[1:-1])
for x in range(0, nasobek_1):
    goly_asistence_upravit.append(goly_prvni_tretina[3 + 7*x].text)
for x in range(0, nasobek_2):
    goly_asistence_upravit.append(goly_druha_tretina[3 + 7*x].text)
for x in range(0, nasobek_3):
    goly_asistence_upravit.append(goly_treti_tretina[3 + 7*x].text)
for strelec in goly_strelci_upravit:
    goly_strelci.append(strelec[1:-1])
for asistent in goly_asistence_upravit:
    goly_asistence.append(asistent.strip("\n"))
for x in range(0, nasobek_1):
    goly_typ.append(goly_prvni_tretina[4 + 7*x].text)
for x in range(0, nasobek_2):
    goly_typ.append(goly_druha_tretina[4 + 7*x].text)
for x in range(0, nasobek_3):
    goly_typ.append(goly_treti_tretina[4 + 7*x].text)
for x in range(0, nasobek_1):
    goly_hraci_plus.append(goly_prvni_tretina[5 + 7*x].text)
for x in range(0, nasobek_2):
    goly_hraci_plus.append(goly_druha_tretina[5 + 7*x].text)
for x in range(0, nasobek_3):
    goly_hraci_plus.append(goly_treti_tretina[5 + 7*x].text)
for x in range(0, nasobek_1):
    goly_hraci_minus.append(goly_prvni_tretina[6 + 7*x].text)
for x in range(0, nasobek_2):
    goly_hraci_minus.append(goly_druha_tretina[6 + 7*x].text)
for x in range(0, nasobek_3):
    goly_hraci_minus.append(goly_treti_tretina[6 + 7*x].text)

delka_typ = len(goly_typ)
for x in range(0, delka_typ):
    if goly_typ[x] == "5/5":
        goly_typ_2.append("5 na 5")
    elif goly_typ[x] == "5/4":
        goly_typ_2.append("Přesilovka 5 na 4")
    elif goly_typ[x] == "5/3":
        goly_typ_2.append("Přesilovka 5 na 3")
    elif goly_typ[x] == "4/3":
        goly_typ_2.append("Přesilovka 4 na 3")
    elif goly_typ[x] == "4/4":
        goly_typ_2.append("4 na 4")
    elif goly_typ[x] == "3/3":
        goly_typ_2.append("3 na 3")
    elif goly_typ[x] == "3/4":
        goly_typ_2.append("Oslabení 3 proti 4")
    elif goly_typ[x] == "4/5":
        goly_typ_2.append("Oslabení 4 proti 5")
    elif goly_typ[x] == "3/5":
        goly_typ_2.append("Oslabení 3 proti 5")
    else:
        goly_typ_2.append("TS/jiné")

pocet_radku = len(goly_cas) + 1
radek_0.append(titulek)

soubor = open("hokej-statistiky-zapas.csv", mode="w", newline="")
zapisovac = csv.writer(soubor, delimiter =";")
zapisovac_2 = csv.writer(soubor)
zapisovac_2.writerow(radek_0)
zapisovac.writerow(radek_1)

for x in range(2, pocet_radku + 1):
    radek_x = []
    radek_x.append(goly_cas[x - 2])
    radek_x.append(goly_tym[x - 2])
    radek_x.append(goly_strelci[x - 2])
    radek_x.append(goly_asistence[x - 2])
    radek_x.append(goly_typ_2[x - 2])
    radek_x.append(goly_hraci_plus[x - 2])
    radek_x.append(goly_hraci_minus[x - 2])
    zapisovac.writerow(radek_x)

pocet_golu_domaci = goly_tym.count(tymy[0])
pocet_golu_hoste = goly_tym.count(tymy[1])
vysledek_text = (f"Výsledek zápasu {tymy[0]} : {tymy[1]} - {pocet_golu_domaci} : {pocet_golu_hoste} po základní hrací době")
vysledek = []
vysledek.append(vysledek_text)
zapisovac.writerow(prazdny)
zapisovac.writerow(vysledek)
zapisovac.writerow(prazdny)

# Pokud se hrálo prodloužení a/nebo nájezdy, tak i z nich doplníme do souboru údaje.
casti_zapasu = []
casti = soup1.find_all("h3", {"class": "m-t-0"})
for cast in casti:
    casti_zapasu.append(cast.text)
if ("Prodloužení" in casti_zapasu and not "Nájezdy" in casti_zapasu):
    prodlouzeni = []
    gol_prodlouzeni = polozky_2[3]
    radek_prodlouzeni = []
    prodlouzeni.append("Prodloužení - vítězný gól: ")
    zapisovac.writerow(prodlouzeni)
    gol_prodlouzeni_cas = (gol_prodlouzeni[0].text)
    gol_prodlouzeni_tym = (gol_prodlouzeni[1].text)
    gol_prodlouzeni_strelec_upravit = (gol_prodlouzeni[2].text)
    gol_prodlouzeni_strelec = gol_prodlouzeni_strelec_upravit[1:-1]
    gol_prodlouzeni_asistence = (gol_prodlouzeni[3].text)
    gol_prodlouzeni_typ = (gol_prodlouzeni[4].text)
    gol_prodlouzeni_plus = (gol_prodlouzeni[5].text)
    gol_prodlouzeni_minus = (gol_prodlouzeni[6].text)
    radek_prodlouzeni.append(gol_prodlouzeni_cas)
    radek_prodlouzeni.append(gol_prodlouzeni_tym)
    radek_prodlouzeni.append(gol_prodlouzeni_strelec)
    radek_prodlouzeni.append(gol_prodlouzeni_asistence)
    if gol_prodlouzeni_typ == "5/5":
        radek_prodlouzeni.append("5 na 5")
    elif gol_prodlouzeni_typ == "5/4":
        radek_prodlouzeni.append("Přesilovka 5 na 4")
    elif gol_prodlouzeni_typ == "5/3":
        radek_prodlouzeni.append("Přesilovka 5 na 3")
    elif gol_prodlouzeni_typ == "4/3":
        radek_prodlouzeni.append("Přesilovka 4 na 3")
    elif gol_prodlouzeni_typ == "4/4":
        radek_prodlouzeni.append("4 na 4")
    elif gol_prodlouzeni_typ == "3/3":
        radek_prodlouzeni.append("3 na 3")
    elif gol_prodlouzeni_typ == "3/4":
        radek_prodlouzeni.append("Oslabení 3 proti 4")
    elif gol_prodlouzeni_typ == "4/5":
        radek_prodlouzeni.append("Oslabení 4 proti 5")
    elif gol_prodlouzeni_typ == "3/5":
        radek_prodlouzeni.append("Oslabení 3 proti 5")
    else:
        radek_prodlouzeni.append("TS/jiné")
    radek_prodlouzeni.append(gol_prodlouzeni_plus)
    radek_prodlouzeni.append(gol_prodlouzeni_minus)
    zapisovac.writerow(radek_prodlouzeni)
if "Nájezdy" in casti_zapasu:
    najezdy_byly = []
    najezdy_byly.append("Nájezdy - vítězný nájezd: ")
    zapisovac.writerow(najezdy_byly)
    radek_vitezny_najezd = []
    najezdy_hraci = []
    vitezny_najezd = polozky_2[4]
    vitezny_najezd_strelec = vitezny_najezd[2].text
    radek_vitezny_najezd.append(vitezny_najezd[0].text)
    radek_vitezny_najezd.append(vitezny_najezd[1].text)
    radek_vitezny_najezd.append(vitezny_najezd_strelec[1:-8])
    zapisovac.writerow(radek_vitezny_najezd)
    zapisovac.writerow(prazdny)
    souhrn_najezdy = soup1.find_all("table", {"class": ""})
    vsechny_najezdy = souhrn_najezdy[-5].find_all("td")
    delka_najezdu = int(len(vsechny_najezdy)/4)
    najezdy_poradi = []
    najezdy_tym = []
    najezdy_vysledek = []
    najezdy_hrac_upravit = []
    najezdy_hrac = []
    for x in range(0, delka_najezdu):
        najezdy_poradi.append(vsechny_najezdy[0 + 4*x].text)
    for x in range(0, delka_najezdu):
        najezdy_tym.append(vsechny_najezdy[1 + 4*x].text)
    for x in range(0, delka_najezdu):
        najezdy_vysledek.append(vsechny_najezdy[2 + 4*x].text)
    for x in range(0, delka_najezdu):
        najezdy_hrac_upravit.append(vsechny_najezdy[3 + 4*x].text)
    for hrac in najezdy_hrac_upravit:
        najezdy_hrac.append(hrac[1:-6])
    zapisovac.writerow(najezdy_poradi)
    zapisovac.writerow(najezdy_tym)
    zapisovac.writerow(najezdy_vysledek)
    zapisovac.writerow(najezdy_hrac)
soubor.close()