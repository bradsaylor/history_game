import re
import os

if True:
    os.system("cls")

months_list = (
    r"January|February|March|April|"
    r"May|June|July|August|"
    r"September|October|November|December"
)

exclude_list = r"\(.*\)|" r"\[.*\]|" r"or.*"

text = "690 August"
# text = r"123 [456] (789)"

year = None
month = None
day = None

print(f"original input: %s" % text)

num_re = re.compile(r"\d+")
month_re = re.compile(months_list)
exclude_re = re.compile(exclude_list)
for item in exclude_re.findall(text):
    text = text.replace(item, "")


print(f"formatted input: %s" % text)

num_list = num_re.findall(text)
month_list = month_re.findall(text)

if len(num_list) == 1:
    if month_list:
        day = num_list[0]
        month = month_list[0]
    else:
        year = num_list[0]
elif len(num_list) > 1:
    year = num_list[0]
    day = num_list[1]
    assert month_list, "ERROR: day given but no month given"
    month = month_list[0]
else:
    if month_list:
        month = month_list[0]

print("day: {0}".format(day))
print("month: {0}".format(month))
print("year: {0}".format(year))
