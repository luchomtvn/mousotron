import source.utils as utils
import datetime
from functools import reduce
from datetime import datetime
import pandas as pd


# get the whole string and select only the month to replace without the dot and capitalized.
def format_date(date_string):
    date_string = date_string.replace(date_string.split(" ")[1], utils.month_es_to_en[date_string.split(" ")[1].replace(".", "").capitalize()])
    return datetime.strptime(date_string, '%Y %b %d %H:%M:%S')


def get_seconds(time):
    numbers = list(map(int, time.split(" ")[::2]))
    mult = 1
    for i in range(len(numbers)):
        if i == 0:
            mult = 24*60*60
        if i == 1:
            mult = 60*60
        if i == 2:
            mult = 60
        elif i == 3:
            mult = 1

        numbers[i] = numbers[i]*mult
    return reduce(lambda x, y: x+y, numbers)

def get_cents(time):
    numbers = list(map(int, time.split(" ")[::2]))
    mult = 1
    for i in range(len(numbers)):
        if i == 0:
            mult = 100*1000
        if i == 1:
            mult = 100
        elif i == 2:
            mult = 1

        numbers[i] = numbers[i]*mult
    return reduce(lambda x, y: x+y, numbers)

def format_row(row, column_names=False):
    i_line = 0
    new_row = []
    spaces_idx = 0 if column_names else 1
    for col_spaces in utils.spaces:
        slice_range = col_spaces[spaces_idx] + 1
        new_row.append(" ".join(row[i_line:slice_range + i_line]))
        i_line += slice_range
    return new_row