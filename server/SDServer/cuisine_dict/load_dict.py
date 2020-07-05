# Load cuisine_dict into python set

import csv
import time
cuisine = {}
start = time.time()

with open('cuisine.csv', newline='', encoding='utf-8-sig') as f:
    cuisine = {elem.lower().strip() for line in list(csv.reader(f)) for elem in line}

end = time.time()
print(str(len(cuisine)) + ' cuisine items loaded in ' + str(end - start) + ' s')
