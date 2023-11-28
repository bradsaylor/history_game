import re


class scrape_data:
    def __init__(self):
        self.type = None
        self.start_end = None
        self.start_day = None
        self.start_month = None
        self.start_year = None
        self.start_adbc = None
        self.end_day = None
        self.end_month = None
        self.end_year = None
        self.end_adbc = None

    def reset_scrape_data(self):
        self.type = None
        self.start_day = None
        self.start_month = None
        self.start_year = None
        self.start_adbc = None
        self.end_day = None
        self.end_month = None
        self.end_year = None
        self.end_adbc = None


def dmy_re(str, data):
    dmy_re = re.compile(r"\d+\s+[a-zA-z]+\s+[\d]+")
    mdy_re = re.compile(r"[a-zA-z]+\s+[\d]+(,*)\s+[\d]+")

    if results := dmy_re.search(str):
        data.type = "dmy"
        if data.start_end == "start":
            data.start_day = results.group().split()[0]
            data.start_month = results.group().split()[1]
            data.start_year = results.group().split()[2]

            try:
                ad_bc = results.group().split()[3]
            except:
                data.start_adbc = "AD"
            else:
                if ad_bc == "BC":
                    data.start_adbc = "BC"
                else:
                    data.start_adbc = "AD"

            return True

        elif data.start_end == "end":
            data.end_day = results.group().split()[0]
            data.end_month = results.group().split()[1]
            data.end_year = results.group().split()[2]

            try:
                ad_bc = results.group().split()[3]
            except:
                data.end_adbc = "AD"
            else:
                if ad_bc == "BC":
                    data.end_adbc = "BC"
                else:
                    data.end_adbc = "AD"

            return True

        else:
            return False

    elif results := mdy_re.search(str):
        data.type = "mdy"
        if data.start_end == "start":
            data.start_month = results.group().split()[0]
            data.start_day = results.group().split()[1]
            data.start_year = results.group().split()[2]

            try:
                ad_bc = results.group().split()[3]
            except:
                data.start_adbc = "AD"
            else:
                if ad_bc == "BC":
                    data.start_adbc = "BC"
                else:
                    data.start_adbc = "AD"

            return True

        elif data.start_end == "end":
            data.end_month = results.group().split()[0]
            data.end_day = results.group().split()[1]
            data.end_year = results.group().split()[2]

            try:
                ad_bc = results.group().split()[3]
            except:
                data.end_adbc = "AD"
            else:
                if ad_bc == "BC":
                    data.end_adbc = "BC"
                else:
                    data.end_adbc = "AD"

            return True

        else:
            return False

    else:
        return False


def dm_re(str, data):
    dm_re = re.compile(r"[\d]+,* [a-zA-z]+")
    yBC_re = re.compile("\d+ BC")
    yAD_re = re.compile("AD \d+")

    if (
        (results := dm_re.search(str))
        and not yBC_re.search(str)
        and not yAD_re.search(str)
    ):
        data.type = "dm"
        if data.start_end == "start":
            data.start_day = results.group().split()[0]
            data.start_month = results.group().split()[1]
            return True
        elif data.start_end == "end":
            data.end_day = results.group().split()[0]
            data.end_month = results.group().split()[1]
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
        if data.start_end == "start":
            data.start_year = results.group().split()[0]

            try:
                ad_bc = results.group().split()[1]
            except:
                data.start_adbc = "AD"
            else:
                if ad_bc == "BC":
                    data.start_adbc = "BC"
                else:
                    data.start_adbc = "AD"

            return True

        elif data.start_end == "end":
            data.end_year = results.group().split()[0]

            try:
                ad_bc = results.group().split()[1]
            except:
                data.end_adbc = "AD"
            else:
                if ad_bc == "BC":
                    data.end_adbc = "BC"
                else:
                    data.end_adbc = "AD"

            return True

        else:
            return False

    elif results := yAD_re.search(str):
        data.type = "yAD"
        if data.start_end == "start":
            data.start_year = results.group().split()[0]

            try:
                ad_bc = results.group().split()[1]
            except:
                data.start_adbc = "AD"
            else:
                if ad_bc == "BC":
                    data.start_adbc = "BC"
                else:
                    data.start_adbc = "AD"

            return True

        elif data.start_end == "end":
            data.end_year = results.group().split()[0]
            try:
                ad_bc = results.group().split()[1]
            except:
                data.end_adbc = "AD"
            else:
                if ad_bc == "BC":
                    data.end_adbc = "BC"
                else:
                    data.end_adbc = "AD"

            return True

        else:
            return False

    elif (results := y_re.search(str)) and not brackets_re.search(str):
        data.type = "y"
        if data.start_end == "start":
            data.start_year = results.group().split()[0]

            try:
                ad_bc = results.group().split()[1]
            except:
                data.start_adbc = "AD"
            else:
                if ad_bc == "BC":
                    data.start_adbc = "BC"
                else:
                    data.start_adbc = "AD"

            return True

        elif data.start_end == "end":
            data.end_year = results.group().split()[0]

            try:
                ad_bc = results.group().split()[1]
            except:
                data.end_adbc = "AD"
            else:
                if ad_bc == "BC":
                    data.end_adbc = "BC"
                else:
                    data.end_adbc = "AD"

            return True

        else:
            return False

    else:
        return False
