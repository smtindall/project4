import csv
from itertools import islice
import constants
import parse_utils


# for fname in constants.fnames:
#     print(f'{fname}')
#     with open(fname) as f:
#         print(next(f),end='')
#         print(next(f),end='')
#         print(next(f),end='')
#     print()


# for fname in constants.fnames:
#     print(fname)
#     reader = parse_utils.csv_parser(fname)
#     print(next(reader))
#     print(next(reader),end='\n')

# reader=parse_utils.csv_parser(constants.fname_update)
# for _ in range(3):
#     record = next(reader)


for fname, class_name, parser in zip(constants.fnames,constants.class_names,constants.parsers):
    file_iter = parse_utils.iter_file(fname,class_name, parser)
    print(fname)
    for _ in range(3):
        print(next(file_iter))
    print()
