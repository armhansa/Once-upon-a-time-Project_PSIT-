import csv
import plotly.plotly as py
from plotly.tools import FigureFactory as FF
from datetime import datetime

yy, mm, dd = 2015, 12, 1
name_hoon = input('ใส่ชื่อหุ้นที่ต้องการดูกราฟ : ').upper()
day_in = int(input('จำนวนวันที่ต้องการดูย้อนหลังของหุ้นตัวนั้น : '))
data_open, data_close, data_high, data_low, data_vol, date = [], [], [], [], [], []
while day_in > 0:
    step_day = 'set-history_EOD_'+'%d-%02d-%02d.csv' % (yy, mm, dd)
    try:
        file = open(step_day, 'r')
        temporary = csv.reader(file)
        for row in temporary:
            if row[0] == name_hoon:
                data_open.append(float(row[2]))
                data_high.append(float(row[3]))
                data_low.append(float(row[4]))
                data_close.append(float(row[5]))
                data_vol.append(float(row[6]))
                date.append(datetime(year = int(row[1][0:4]), month = int(row[1][4:6]), day = int(row[1][6:]))
        day_in -= 1
    except:
        pass

    dd -= 1
    if dd == 0:
        mm -= 1
        dd = 31
    if mm == 0:
        yy -= 1
        mm = 12

fig = FF.create_candlestick(open_data, high_data, low_data, close_data, dates=dates)

plot_url = py.plot(fig, filename='finance/simple-candlestick', validate=False)
