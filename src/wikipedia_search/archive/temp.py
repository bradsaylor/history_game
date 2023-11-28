import requests
from bs4 import BeautifulSoup


def scrape(url, verbose=False):
    month = None
    found_date = False
    found_month = False

    # pull html from page
    page = requests.get(url)
    # make the soup
    soup = BeautifulSoup(page.content, "html.parser")
    # pull the title
    title = soup.h1.string
    # search the soup for infobox
    my_table = soup.find("table", class_="infobox")

    # make sure a table exists before proceeding
    try:
        test = my_table.strings
    except AttributeError:
        # print('Could not scrape')
        return False

    # perform the actual search
    for string_uni in my_table.strings:
        string = str_unicode_to_ascii(string_uni)
        if verbose:
            print(repr(string))

        if string.startswith("Born"):
            if verbose:
                print("found", repr(string))
            found_date = True
            continue

        if found_date:
            if day_month_year_search(string):
                return (title, string)

            elif not found_month and day_month_search(string):
                month = string
                found_month = True

            elif found_month and year_search(string):
                return (title, month, string)
