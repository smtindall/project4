import csv
from itertools import islice
import constants
import parse_utils
import itertools
from datetime import datetime



# for fname, class_name, parser in zip(constants.fnames,constants.class_names,constants.parsers):
#     file_iter = parse_utils.iter_file(fname,class_name, parser)
#     print(fname)
#     for _ in range(3):
#         print(next(file_iter))
#     print()
#
# gen = parse_utils.iter_combined_plain_tuple(constants.fnames, constants.class_names, constants.parsers,constants.compress_fields)
#
# print(list(next(gen)))
# print(list(next(gen)))

print('-' * 20)

def group_key(item):
    return item.gender, item.vehicle_make

cutoff_date = datetime (2017,3,1)
data = parse_utils.filtered_iter_combined(constants.fnames,constants.class_names,
                                                   constants.parsers,constants.compress_fields,
                                                   key=lambda row:row.last_updated >= cutoff_date)
sorted_data = sorted(data,key=group_key)

group_1 = itertools.groupby(sorted_data,key=group_key)
group_2 = itertools.groupby(sorted_data,key=group_key)


group_f = (item for item in group_1 if item[0][0] == 'Female')
data_f = ((item[0][1], len(list(item[1]))) for item in group_f)

for row in data_f:
    print(row)


group_m = (item for item in group_2 if item[0][0] == 'Male')
data_m = ((item[0][1], len(list(item[1]))) for item in group_m)

for row in data_m:
    print(row)
