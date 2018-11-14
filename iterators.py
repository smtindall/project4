import csv
from itertools import islice
import constants

def read_file(file_name):
    with open(file_name) as f:
        rows = csv.reader(f, delimiter=',', quotechar='"')
        yield from rows

for fname in constants.fnames:
    rows = read_file(fname)
    for row in islice(rows, 3):
        print(row)
    print()

