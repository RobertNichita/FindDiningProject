# Load cuisine_dict into python set
import csv
file = 'restaurant/cuisine_dict/dishes.csv'
cuisine_dict = {}

s = {}
with open(file, newline='', encoding='utf-8-sig') as f:
    cuisine_dict = {elem.lower().strip() for line in list(csv.reader(f)) for elem in line}


