# Load cuisine_dict into python set

import csv

cuisine = {}
dishes = {}


def main(files):
    file_data = []

    for file in files:
        with open(file, newline='', encoding='utf-8-sig') as f:
            file_data.append({elem.lower().strip() for line in list(csv.reader(f)) for elem in line})

    return file_data


