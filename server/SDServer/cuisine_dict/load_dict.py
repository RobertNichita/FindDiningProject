# Load cuisine_dict into python set

import csv
data = {}

with open('cuisine_dict.csv', newline='', encoding='utf-8-sig') as f:
    data = {elem for line in list(csv.reader(f)) for elem in line}

print(data)
