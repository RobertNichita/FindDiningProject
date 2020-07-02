# Load cuisine_dict into python set

import csv
import time
data = {}
start = time.time()

with open('cuisine_dict.csv', newline='', encoding='utf-8-sig') as f:
    data = {elem.lower() for line in list(csv.reader(f)) for elem in line}

print(data)
end = time.time()
print(str(len(data)) + ' item loaded in ' + str(end - start) + ' s')
