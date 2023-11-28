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
                    born_data = " ".join(born_data)

                if item.th.string == "Died":
                    died_data = [*item.td.strings]
                    died_data = " ".join(died_data)

    born_data = hf.remove_non_ascii(born_data)
    died_data = hf.remove_non_ascii(died_data)

    born = hf.scrape_data()
    died = hf.scrape_data()

    # print("born->", born_data, "\ndied->", died_data)

    born.reset_scrape_data()
    hf.parse_date(born_data, born)
    born.clean_data()

    died.reset_scrape_data()
    hf.parse_date(died_data, died)
    died.clean_data()

    return (born, died)
