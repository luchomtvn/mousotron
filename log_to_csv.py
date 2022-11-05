import pandas as pd
from functools import partial

'''
spaces between column names, spaces between row data for that column.

- Date: (0,3)
- days hour min sec: (3,7)
- Distance 1: (1,1)
- Distance 2: (1,1)
- Distance 3: (1,1)
- keystrokes: (0,0)
- left: (0,0)
- right: (0,0)
- middle: (0,0)
- double: (0,0)
- wheel: (0,0)
- x1 btn: (1,0)
- x2 btn: (1,0)
- idle days hour min sec: (4,7)

'''
spaces = [(0,3), (3,7), (1,1), (1,1), (1,1), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (1,0), (1,0), (4,7)]

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
    for col_spaces in spaces:
        slice_range = col_spaces[spaces_idx] + 1
        new_row.append(" ".join(row[i_line:slice_range + i_line]))
        i_line += slice_range
    return new_row


new_cols = format_row(cols, column_names=True)
data = list(map(partial(format_row, column_names=False), rows)) # use partial to pass arguments to mapping function
pd.DataFrame(data, columns=new_cols).to_csv('mousotron_data.csv') 