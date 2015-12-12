import csv
import plotly.plotly as py
from plotly.tools import FigureFactory as FF
from datetime import datetime
py.sign_in('5z3nnr8v', 'fqyao8qk62')
yy, mm, dd = 2015, 12, 1
name_hoon = input('Stock Name : ').upper()
day_in = int(input('Time : '))
future = int(input())
data_open, data_close, data_high, data_low, data_vol, data_values, date = [], [], [], [], [], [], []
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
                data_values.append(float(row[6])*float(row[5]))
                date.append(datetime(year = int(row[1][0:4]), month = int(row[1][4:6]), day = int(row[1][6:])))
        day_in -= 1
    except:
        pass
    data_sma, date_sma = [], []
    for i in range(day_in):
        if i >= future-1:
            sma = 0
            for j in range(future):
                sma += data_close[::-1][i-(future-1)-j]
            data_sma.append(sma/future)
            date_sma.append(datetime(year = int(date[i+1][0:4]), month = int(date[i+1][4:6]), day = int(date[i+1][6:])))
    dd -= 1
    if dd == 0:
        mm -= 1
        dd = 31
    if mm == 0:
        yy -= 1
        mm = 12
add_line = Scatter(
    x=date_sma, 
    y=data_sma, 
    name= 'Open Vals', 
    line=Line(color='black')
    )
fig = FF.create_candlestick(data_open, data_high, data_low, data_close, dates=date)
fig['data'].extend([add_line])
plot_url = py.plot(fig, filename='finance/simple-candlestick', validate=False)
