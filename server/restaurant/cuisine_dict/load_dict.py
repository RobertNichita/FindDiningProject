# Load cuisine_dict into python set
import csv


def read(file):
    s = {}
    with open(file, newline='', encoding='utf-8-sig') as f:
        s = {elem.lower().strip() for line in list(csv.reader(f)) for elem in line}

    return s
