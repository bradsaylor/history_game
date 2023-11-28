from bs4 import BeautifulSoup
import requests
import re


def return_links(url):
    base_url = "https://en.wikipedia.org"

    # Don't want links which match these re's:
    link_re = re.compile("File")
    link_re2 = re.compile("identifier")
    link_re3 = re.compile(":")

    # pull down page text and parse for links. HTML =  '<a ... '
    start_page = requests.get(url)
    soup = BeautifulSoup(start_page.text, "html.parser")
    links = soup.find_all("a")

    for link in links:
        # try to parse 'href=' attribute, skip if error
        try:
            term = link["href"]
        except:
            continue

        # Link  has to start with /wiki/ and not be equal to current page
        if term.startswith("/wiki/") and ((base_url + term) != url):
            if not (
                link_re.search(term)
                or link_re2.search(term)
                or link_re3.search(term)
            ):
                yield (base_url + term)


def links_to_file(url):
    links = return_links(url)

    with open("links.txt", "w", encoding="utf-8") as f:
        for count in range(100):
            f.write(next(links) + "\n")
