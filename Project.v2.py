import csv
import plotly.plotly as py
from plotly.tools import FigureFactory as FF
from plotly.graph_objs import *
from datetime import datetime
py.sign_in('armhansa', 'um3r605dt8')

year, month, day = 2015, 12, 11
name_stock = input('Stock Name : ').upper()
day_in = int(input('Rate Time : '))
future = int(input('Future : '))
total = day_in
data_ema, ema = [], 0
open_data, close_data, high_data, low_data, vol_data, dates = [], [], [], [], [], []
while day_in > 0:
    step_day = 'set-history_EOD_'+'%d-%02d-%02d.csv' % (year, month, day)
    try:
        temporary = csv.reader(open(step_day, 'r'))
        for row in temporary:
            if row[0] == name_stock:
                open_data.append(float(row[2]))
                high_data.append(float(row[3]))
                low_data.append(float(row[4]))
                close_data.append(float(row[5]))
                vol_data.append(float(row[6]))
                dates.append(datetime(year = int(row[1][0:4]), month = int(row[1][4:6]), day = int(row[1][6:])))
        day_in -= 1
    except:
        pass

    day -= 1
    if day == 0:
        month -= 1
        day = 31
    if month == 0:
        year -= 1
        month = 12

open_data, close_data, high_data, low_data, vol_data, dates = open_data[::-1], close_data[::-1], high_data[::-1], low_data[::-1], vol_data[::-1], dates[::-1]

data_sma, date_sma = [], []
for i in range(total):
    if i >= future-1:
        sma = 0
        for j in range(future):
            sma += close_data[i-j]
        data_sma.append(sma/future)
        if i != total-1:
            date_sma.append(dates[i+1])
        else:
            date_sma.append(datetime(year = 2015, month = 12, day = 12))
for i in range(total):
    data_ema.append(ema+(2/(future+1))*(close_data[i])-ema)
add_sma = Scatter(
    x=date_sma, 
    y=data_sma, 
    name= 'SMA', 
    line=Line(color='black')
    )
add_ema = Scatter(
    x=date_sma, 
    y=data_sma, 
    name= 'EMA', 
    line=Line(color='green')
    )
fig = FF.create_candlestick(open_data, high_data, low_data, close_data, dates=dates)
fig['layout'].update({
    'title': 'Stock',
    'yaxis': {'title': 'Price'},
    'xaxis': {'title': 'Time'}
})
fig['data'].extend([add_sma])
fig['data'].extend([add_ema])
plot_url = py.plot(fig, filename='finance/simple-candlestick', validate=False)
