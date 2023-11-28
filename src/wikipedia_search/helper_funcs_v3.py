import re
import string
import os

if True:
    os.system("cls")

months_list = (
    r"January|February|March|April|"
    r"May|June|July|August|"
    r"September|October|November|December"
)

# exclude list contains:
# - any sequence of 3 numbers separated by 2 dashes
#   - needed to remove hidden dates formatted this way in html
# - any sequence of 1 or 2 chars inside of square brackets
#   - needed to remove reference number links inside square brackets
# - any chars including and after 'or'
#   - needed to remove alternative dates which may be given
exclude_list = (
    r"[\d]+-[\d]+-[\d]+|" r"\[.{1,2}\]|" r"or [\d]+|" r"\(aged [\d]+\)"
)

num_re = re.compile(r"\d+")
month_re = re.compile(months_list)
exclude_re = re.compile(exclude_list)


class scrape_data:
    def __init__(self):
        self.type = None
        self.day = None
        self.month = None
        self.year = None
        self.adbc = None

    def reset_scrape_data(self):
        self.type = None
        self.day = None
        self.month = None
        self.year = None
        self.adbc = None

    @staticmethod
    def clean_str(str):
        if str:
            match_str = string.ascii_letters + string.digits
            return "".join(c for c in str if c in match_str)
        else:
            return False

    def clean_data(self):
        self.day = self.clean_str(self.day)
        self.month = self.clean_str(self.month)
        self.year = self.clean_str(self.year)
        self.adbc = self.clean_str(self.adbc)


def remove_non_ascii(text):
    # remove all unicode replace with space
    return re.sub(r"[^\x00-\x7F]", " ", text)


def try_adbc(results, index, data):
    try:
        ad_bc = results.group().split()[index]
    except:
        data.adbc = "AD"
    else:
        if ad_bc == "BC":
            data.adbc = "BC"
        else:
            data.adbc = "AD"
    return True


def assign_date(str, data):
    num_re = re.compile(r"\d+")


def parse_date(str, data):
    for item in exclude_re.findall(str):
        str = str.replace(item, "")

    num_list = [
        (match.group(), match.start()) for match in num_re.finditer(str)
    ]
    month_list = [
        (match.group(), match.start()) for match in month_re.finditer(str)
    ]
    if len(num_list) == 1:
        if month_list:
            data.month = month_list[0][0]
            if month_list[0][1] > num_list[0][1]:
                data.day = num_list[0][0]
            else:
                data.year = num_list[0][0]
        else:
            data.year = num_list[0][0]
    elif len(num_list) > 1:
        if month_list:
            data.day = num_list[0][0]
            data.year = num_list[len(num_list) - 1][0]
            data.month = month_list[0][0]
        else:
            data.year = num_list[0][0]
    else:
        assert len(num_list) >= 1, "ERROR: No number found"
