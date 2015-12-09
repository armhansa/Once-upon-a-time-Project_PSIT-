import matplotlib.pyplot as ptl
import csv
import string
char = string.ascii_uppercase
data = {}
all_set = []
yy, mm, dd = 2015, 11, 23
name_hoon = input('ใส่ชื่อหุ้นที่ต้องการดูกราฟ : ').upper()
day_in = int(input('จำนวนวันที่ต้องการดูย้อนหลังของหุ้นตัวนั้น : '))
total = day_in
while total > 0:
    step_day = 'set-history_EOD_'+'%d-%02d-%02d.csv' % (yy, mm, dd)
    try:
        file = open(step_day, 'r')
        temporary = csv.reader(file)
        for row in temporary:
            if row[0] == name_hoon:
            #if len(row[0]) <= 6 and row[0][-1] in char and not '$' in row[0] and not '-' in row[0] and not '!' in row[0] and not 'SET' in row[0] and row[0] != 'MAI':
                #if not row[0] in data:
                    #data[row[0]] = []
                data[total] = int(row[5])
            elif row[0] == 'SET':
                all_set.append(row[1:])
        total -= 1
    except:
        pass
    if dd == 1:
        mm -= 1
        dd = 31
    if mm == 0:
        yy -= 1
        mm = 12
    dd -= 1 

x = list(data.keys())
y = list(data.values())

ptl.plot(list(data.keys()), list(data.values()), ':rs')
#ptl.axis(1, day_in, 0, 1000)
ptl.title('Graph of '+name_hoon)
ptl.xlabel("Day")
ptl.ylabel("Price")
ptl.show()
