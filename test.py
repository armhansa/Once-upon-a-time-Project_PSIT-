import csv
import string
char = string.ascii_uppercase
yy, mm, dd = 2015, 1, 5
step_day = 'set-history_EOD_'+'%d-%02d-%02d.csv' % (yy, mm, dd)
file = open(step_day, 'r')
temporary = csv.reader(file)
data = {}
all_set = []
for row in temporary:
    if len(row[0]) <= 6 and row[0][-1] in char and not '$' in row[0] and not '-' in row[0] and not '!' in row[0] and not 'SET' in row[0] and row[0] != 'MAI':
        if not row[0] in data:
            data[row[0]] = []
        data[row[0]].append(row[1:])
    elif row[0] == 'SET':
        all_set.append(row[1:])
