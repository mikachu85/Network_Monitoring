__author__ = 'Damien'

import csv
import sys
import os
import time

# csv - file loader
def data_loader(filename):
    records = []
    with open(filename, 'rb') as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ',')
        next(csvreader,'none') # Skips header line
        for row in csvreader:
            if len(row) == 4:
                records.append({
                    "datamaskinid": row[0].strip(), # Computer ID
                    "bygg": (row[1].strip()), # Building
                    "rom": (row[2].strip()), # Room number
                    "rad": float(row[3].strip()) # Row
                })
    return records

# csv - data
test_data = data_loader("Data/test.data")

datamaskinid = [x['datamaskinid'] for x in test_data]
bygg = [x['bygg'] for x in test_data]
rom = [x['rom'] for x in test_data]
rad = [x['rad'] for x in test_data]

for i in range(0, 7, 1):
    print '%18s, %5s, %5s, %1s' % (datamaskinid[i], bygg[i], rom[i], int(rad[i]))

# Response from computer lab rooms
for i in range(0,7, 1):
    response = os.system("ping " + datamaskinid[i] + ' -n ' + '1')





