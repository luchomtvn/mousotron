import utils
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

df = pd.read_csv("mousotron_data.csv")

df['Date'] = df['Date'].apply(format_date)
df['Distance'] = df['Distance'].apply(get_cents)
df['Active time'] = df['Active time'].apply(get_seconds)
df['Idle time'] = df['Idle time'].apply(get_seconds)

df = df.astype({'Keystrokes': 'int64', 'Left clicks': 'int64', 'Right clicks': 'int64', 'Middle clicks': 'int64', 'Double clicks': 'int64', 'Wheel turn': 'int64'})

df.to_csv("mousotron_data_formated.csv", index=False)
