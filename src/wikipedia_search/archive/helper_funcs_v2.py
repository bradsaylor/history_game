import re
import string


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


def dmy_re(str, data):
    dmy_re = re.compile(r"\d+\s+[a-zA-z]+\s+[\d]+")
    mdy_re = re.compile(r"[a-zA-z]+\s+[\d]+(,*)\s+[\d]+")
    or_re = re.compile("or")
    aged_re = re.compile("aged")

    if (results := dmy_re.search(str)) and not or_re.search(str):
        data.type = "dmy"
        data.day = results.group().split()[0]
        data.month = results.group().split()[1]
        data.year = results.group().split()[2]
        try_adbc(results, 3, data)
        return True

    elif (results := mdy_re.search(str)) and not aged_re.search(str):
        data.type = "mdy"
        data.day = results.group().split()[0]
        data.month = results.group().split()[1]
        data.year = results.group().split()[2]
        try_adbc(results, 3, data)
        return True

    else:
        return False


def dm_re(str, data):
    dm_re = re.compile(r"[\d]+,* [a-zA-z]+")
    yBC_re = re.compile("\d+ BC")
    yAD_re = re.compile("AD \d+")
    or_re = re.compile("or")

    if (
        (results := dm_re.search(str))
        and not yBC_re.search(str)
        and not yAD_re.search(str)
        and not or_re.search(str)
    ):
        data.type = "dm"
        data.day = results.group().split()[0]
        data.month = results.group().split()[1]
        return True

    else:
        return False


def y_re(str, data):
    yBC_re = re.compile("\d+ BC")
    yAD_re = re.compile("AD \d+")
    y_re = re.compile(r"[\d]+")
    brackets_re = re.compile(r"[\d+]")

    if results := yBC_re.search(str):
        data.type = "yBC"
        data.year = results.group().split()[0]
        try_adbc(results, 1, data)
        return True

    elif results := yAD_re.search(str):
        data.type = "yAD"
        data.year = results.group().split()[0]
        try_adbc(results, 1, data)
        return True

    elif (results := y_re.search(str)) and not brackets_re.search(str):
        data.type = "y"
        data.year = results.group().split()[0]
        try_adbc(results, 1, data)
        return True

    else:
        return False
