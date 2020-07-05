# Load cuisine_dict into python set

import csv
import time

cuisine = {}
dishes = {}


def main(cuisine_path, dish_path):
    start = time.time()
    global cuisine, dishes

    with open(cuisine_path, newline='', encoding='utf-8-sig') as f:
        cuisine = {elem.lower().strip() for line in list(csv.reader(f)) for elem in line}

    with open(dish_path, newline='', encoding='utf-8-sig') as f:
        dishes = {elem.lower().strip() for line in list(csv.reader(f)) for elem in line}

    end = time.time()
    print(str(len(cuisine)) + ' cuisine items and ' + str(len(dishes)) +
          ' dish items loaded in ' + str(end - start) + ' s')


if __name__ == '__main__ ':
    main('cuisine.csv', 'dishes.csv')
else:
    main('cuisine_dict/cuisine.csv', 'cuisine_dict/dishes.csv')
