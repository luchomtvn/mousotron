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
spaces = [(0,3), (3,7), (5,5), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (1,0), (1,0), (4,7)]



rename_dict = {
    'days hour min sec': 'Active time',
    'Distance 1 Distance 2 Distance 3': 'Distance',
    'keystrokes': 'Keystrokes',
    'left': 'Left clicks',
    'right': 'Right clicks',
    'middle': 'Middle clicks',
    'double': 'Double clicks',
    'wheel': 'Wheel turn',
    'idle days hour min sec': 'Idle time'
}

drop_columns = ['x1 btn', 'x2 btn']


month_es_to_en = {
    "Ene": "Jan",
    "Feb": "Feb",
    "Mar": "Mar",
    "Abr": "Apr",
    "May": "May",
    "Jun": "Jun",
    "Jul": "Jul",
    "Ago": "Aug",
    "Sep": "Sep",
    "Oct": "Oct",
    "Nov": "Nov",
    "Dic": "Dec"
}