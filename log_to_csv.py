import pandas as pd
from functools import partial
import utils

# read the log file
with open('Mousotron.log', 'r') as log:
    logs = log.readlines()


cols = logs[0].split()
rows = [x.split() for x in logs[1:]]

# format a row using the space layout from spaces
def format_row(row, column_names=False):
    i_line = 0
    new_row = []
    spaces_idx = 0 if column_names else 1
    for col_spaces in utils.spaces:
        slice_range = col_spaces[spaces_idx] + 1
        new_row.append(" ".join(row[i_line:slice_range + i_line]))
        i_line += slice_range
    return new_row


new_cols = format_row(cols, column_names=True)
data = list(map(partial(format_row, column_names=False), rows)) # use partial to pass arguments to mapping function
df = pd.DataFrame(data, columns=new_cols)

df.drop(utils.drop_columns, inplace=True, axis=1) # can't get useful data from these
df.rename(utils.rename_dict, inplace=True, axis=1)
df.to_csv('mousotron_data.csv', index=False)