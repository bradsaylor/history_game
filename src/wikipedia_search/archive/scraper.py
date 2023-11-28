import requests
from bs4 import BeautifulSoup
import re
import helper_funcs_v3 as hf


def run_scraper(search_str):
    r = requests.get("https://en.wikipedia.org/wiki/" + search_str)
    soup = BeautifulSoup(r.content, "html.parser")
    bs_table = soup.find_all("table")
    born_data = died_data = []

    for table in bs_table:
        for item in table.find_all("tr"):
            if item.th:
                if item.th.string == "Born" or item.th.string == "Baptised":
                    born_data = [*item.td.strings]
                if item.th.string == "Died":
                    died_data = [*item.td.strings]

    born_data = [hf.remove_non_ascii(item) for item in born_data]
    died_data = [hf.remove_non_ascii(item) for item in died_data]

    born = hf.scrape_data()
    died = hf.scrape_data()

    # print("born->", born_data, "\ndied->", died_data)

    born.reset_scrape_data()
    for item in born_data:
        hf.dmy_re(item, born)
        hf.dm_re(item, born)
        hf.y_re(item, born)
    born.clean_data()

    died.reset_scrape_data()
    for item in died_data:
        hf.dmy_re(item, died)
        hf.dm_re(item, died)
        hf.y_re(item, died)
    died.clean_data()

    return (born, died)
