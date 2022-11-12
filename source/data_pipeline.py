import pandas as pd
from functools import partial

import source.utils as utils
from source.re_format_data import get_seconds, get_cents, format_date, format_row


def run_pipe(input_data='input_data/Mousotron.log', output_csv="mousotron_data_formated.csv"):

    # read the log file
    with open(input_data, 'r') as log:
        logs = log.readlines()

    cols = logs[0].split()
    rows = [x.split() for x in logs[1:]]
    new_cols = format_row(cols, column_names=True)
    data = list(map(partial(format_row, column_names=False), rows)) # use partial to pass arguments to mapping function
    
    df = pd.DataFrame(data, columns=new_cols)
    df.drop(utils.drop_columns, inplace=True, axis=1) # can't get useful data from these
    df.rename(utils.rename_dict, inplace=True, axis=1)

    df['Date'] = df['Date'].apply(format_date)
    df['Distance'] = df['Distance'].apply(get_cents)
    df['Active time'] = df['Active time'].apply(get_seconds)
    df['Idle time'] = df['Idle time'].apply(get_seconds)

    df = df.astype({'Keystrokes': 'int64', 'Left clicks': 'int64', 'Right clicks': 'int64', 'Middle clicks': 'int64', 'Double clicks': 'int64', 'Wheel turn': 'int64'})

    df.to_csv(output_csv, index=False)