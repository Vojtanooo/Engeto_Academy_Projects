import csv
import sys
import requests
from bs4 import BeautifulSoup



def main() -> None:
    if "https://volby.cz/pls/ps2017nss/" in sys.argv[1]:
        odkaz = sys.argv[1]
        soubor = sys.argv[2]

        raw_html = web_request(odkaz)
        bs4_text = parsovani_html(raw_html)
        obec_lokace_radky = hledej_obec(bs4_text)
        dicts = {}
        listek = []
        for radek in obec_lokace_radky:
            dict_0 = zpracovani_udaju(radek)
            dicts.update(dict_0)
            if not dict_0 == {'CODE': '-', 'Location': '-'}:
                new_odkaz = adresa(cislo_obce(radek), odkaz)
                new_raw_html = web_request(new_odkaz)
                new_bs4_text = parsovani_html(new_raw_html)
                prvni_tabulka_radky = hledej_prvni_tabulku(new_bs4_text)
                zbyle_tabulky_radky = hledej_zbyle_tabulky(new_bs4_text)
                for radek_tabulky in prvni_tabulka_radky:
                    dict_1 = zpracovani_prvni_tabulka(radek_tabulky)
                    dicts.update(dict_1)
                for index in zbyle_tabulky_radky:
                    dict_2 = zpracovani_zbyle_tabulky(index)
                    dicts.update(dict_2)
                print(f"SAVING....>>> {dict_0['Location']}")
                listek.append(dict(dicts))
                uloz_csv(f"{soubor}.csv", listek)
        print(f">>> DATA SAVED <<< to file: {soubor}" + ".csv")
    else:
        print("Invalid URL!")


def web_request(url: str) -> str:
    with requests.Session() as req:
        return req.get(url).text


def parsovani_html(html: str) -> BeautifulSoup:
    return BeautifulSoup(html, "html.parser")


def hledej_obec(html: BeautifulSoup) -> list:
    obec = []
    tables = html.find_all("table", {"class": "table"})
    for table in tables:
        obec.extend(table.find_all("tr")[2:])
    return obec


def zpracovani_udaju(tr: str) -> dict:
    return {
        "CODE": tr.find_all("td")[0].text,
        "Location": tr.find_all("td")[1].text,
    }


def cislo_obce(tr: str) -> str:
    return tr.find_all("td")[0].text


def adresa(cislo, odkaz):
    return f"https://volby.cz/pls/ps2017nss/ps311?xjazyk" \
           f"=CZ&xkraj=13&xobec={cislo}&xvyber={odkaz[-4:]}"


def hledej_prvni_tabulku(html: BeautifulSoup) -> list:
    table = html.find(id="ps311_t1")
    return table.find_all("tr")[2:]


def zpracovani_prvni_tabulka(tr: str) -> dict:
    return {
        "Registered": tr.find_all("td")[3].text.replace("\xa0", " "),
        "Envelopes": tr.find_all("td")[4].text.replace("\xa0", " "),
        "Valid": tr.find_all("td")[7].text.replace("\xa0", " ")
    }


def hledej_zbyle_tabulky(html: BeautifulSoup) -> list:
    lst = []
    tables = html.find_all("table", summary="Tabulka umožňuje výběr "
                                        "příslušného územního celku "
                                            "na úrovni okresů."
                                        " K výběru případných dalších "
                                            "územních celků "
                                        "použijte odkazy označené "
                                            "symbolem X.")
    for table in tables:
        lst.extend(table.find_all("tr")[2:])
    return lst


def zpracovani_zbyle_tabulky(tr: str) -> dict:
        for i in tr:
            tabulky = {tr.find_all("td")[1].text: tr.find_all("td")[2].text}
            return tabulky


def uloz_csv(jmeno: str, data: list) -> bool:
    with open(f"{jmeno}", "w", newline="") as csv_s:
        zahlavi = data[0].keys()
        dict_writer = csv.DictWriter(csv_s, zahlavi)
        dict_writer.writeheader()
        dict_writer.writerows(data)
        return True


if __name__ == "__main__":
    main()
                      
