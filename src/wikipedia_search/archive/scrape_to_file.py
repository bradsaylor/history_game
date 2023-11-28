import requests
import re
from bs4 import BeautifulSoup
from time import time


class Search_Results:
    def __init__(self):
        self.start = None
        self.end = None
        self.summary = None


# re's to match day_month_year, month_day_year
# day_month, or year data fields
dmy_re = re.compile(r"[\d]+ [a-zA-z]+ [\d]+")
mdy_re = re.compile(r"[a-zA-z]+ [\d]+(,*) [\d]+")
yBC_re = re.compile("\d+ BC")
yAD_re = re.compile("AD \d+")
dm_re = re.compile(r"[\d]+,* [a-zA-z]+")
y_re = re.compile(r"[\d]+")


def measure(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result

    return wrapper


def day_month_year_search(string):
    if dmy_re.search(string):
        return True
    elif mdy_re.search(string):
        return True
    elif yBC_re.search(string):
        return True
    elif yAD_re.search(string):
        return True
    else:
        return False


def day_month_search(string):
    if dm_re.search(string):
        return True
    else:
        return False


def year_search(string):
    if y_re.search(string):
        return True
    else:
        return False


def str_unicode_to_ascii(string_uni):
    temp_str = string_uni.encode("ascii", "replace").decode()
    return temp_str.replace("?", " ")


def rtn_html_soup(url):
    page = requests.get(url)
    return BeautifulSoup(page.content, "html.parser")


def search_soup(soup, tag, class_):
    return soup.find(tag, class_)


def scrape_born_died(text, verbose):
    found_month = False
    born_died_flag = None
    found_data = False

    search_results = Search_Results()

    for string_uni in text.strings:
        string = str_unicode_to_ascii(string_uni)
        if verbose:
            print(repr(string))

        if string.startswith("Born"):
            if verbose:
                print("found", repr(string))
            born_died_flag = "born"
            continue

        if string.startswith("Died"):
            if verbose:
                print("found", repr(string))
            born_died_flag = "died"
            continue

        if born_died_flag:
            if day_month_year_search(string):
                if born_died_flag == "born":
                    search_results.start = string
                else:
                    search_results.end = string
                found_data = True
                found_month = False
                born_died_flag = None

            elif not found_month and day_month_search(string):
                month = string
                found_month = True

            elif found_month and year_search(string):
                if born_died_flag == "born":
                    search_results.start = month + string
                else:
                    search_results.end = month + string
                found_data = True
                found_month = False
                born_died_flag = None

    if found_data:
        return search_results
    else:
        return None


def scrape_soup(soup, search_type, verbose=False):
    title = soup.h1.string
    result = search_soup(soup, "table", "infobox")

    try:
        test = result.strings
    except AttributeError:
        # print('Could not scrape')
        return False

    if search_type == "born_died":
        if search_obj := scrape_born_died(result, verbose):
            return (title, "born-died", search_obj.start, search_obj.end)
        else:
            return None


def return_next_line(file_name):
    with open(file_name) as f:
        for line in f:
            yield line.strip("\n")


def scrape_to_file(file_name, min_index=0, max_index=100, print_out=False):
    success_counter = 0
    line_counter = 0

    with open("scrape_file.txt", "w", encoding="utf-8") as rf:
        for line in return_next_line(file_name):
            if line_counter in range(min_index, max_index):
                soup = rtn_html_soup(line)
                result = scrape_soup(soup, "born_died")
                if result:
                    success_counter += 1
                    rf.write(str(result) + "\n")
                    if print_out:
                        print(line_counter, str(result))
            line_counter += 1

    print("***END***\n\n")
    return success_counter
