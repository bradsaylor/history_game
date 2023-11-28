from links_to_file import *
from scrape_to_file import *
from time import time


def full_test(min_index=0, max_index=100, print_out=False):
    url = "https://en.wikipedia.org/wiki/Julius_Caeser"
    links_file = "links.txt"
    links_to_file(url)
    scrape_count = scrape_to_file(links_file, min_index, max_index, True)
    print("scrape count:", scrape_count)


# scrape("https://en.wikipedia.org/wiki/Suetonius", True)


full_test(30, 40, True)
