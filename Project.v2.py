"""Make graph of Stock from OpenData"""
import csv
import plotly.plotly as py
from plotly.tools import FigureFactory as FF
import plotly.graph_objs as go
from plotly.graph_objs import *
from datetime import datetime
py.sign_in('armhansa', 'um3r605dt8')

def make_ema(smooting, data_close, dates):
    """make list with can graph of EMA"""
    data_ema, date_ema, alfa = [close_data[0]], [dates[0]], 2/(smooting+1)
    for i in range(1, len(close_data)+1):
        data_ema.append(data_ema[i-1]+(alfa*(close_data[i-1]-data_ema[i-1])))
        if i == len(close_data):
            date_ema.append(datetime(year = 2015, month = 12, day = 12))
        else:
            date_ema.append(dates[i])
    return data_ema, date_ema

def make_sma(future, data_close, dates):
    """make list with can graph of SMA"""
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
    return data_sma, date_sma

year, month, day = 2015, 12, 11
name_stock = input('Stock Name : ').upper()
day_in = int(input('Rate Time : '))
future = int(input('Future : '))
total = day_in
open_data, close_data, high_data, low_data, values_data, dates = [], [], [], [], [], []
while day_in > 0:
    step_day = 'set-history_EOD_'+'%d-%02d-%02d.csv' % (year, month, day)
    try:
        temporary = csv.reader(open(step_day, 'r'))
        bug = 1
        for row in temporary:
            if row[0] == name_stock:
                bug = 0
                open_data.append(float(row[2]))
                high_data.append(float(row[3]))
                low_data.append(float(row[4]))
                close_data.append(float(row[5]))
                values_data.append(float(row[6])*float(row[5]))
                dates.append(datetime(year = int(row[1][0:4]), month = int(row[1][4:6]), day = int(row[1][6:])))
        if bug == 1:
            it_bug ##if error
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

open_data, close_data, high_data, low_data, values_data, dates = open_data[::-1], close_data[::-1], high_data[::-1], low_data[::-1], values_data[::-1], dates[::-1]

data_sma, date_sma = make_sma(future, close_data, dates)
data_ema15, date_ema15 = make_ema(15, close_data, dates)
data_ema50, date_ema50 = make_ema(50, close_data, dates)

add_sma = Scatter(
    x=date_sma, 
    y=data_sma, 
    name= 'SMA%d' % (future), 
    line=Line(color='rgb(166,212,64)')
    )
add_ema15 = Scatter(
    x=date_ema15, 
    y=data_ema15, 
    name= 'EMA15', 
    line=Line(color='purple')
    )
add_ema50 = Scatter(
    x=date_ema50,
    y=data_ema50,
    name= 'EMA50',
    line=Line(color='blue')
    )
#add_value = Scatter(
#    x=dates,
#    y=values_data,
#    name= 'Value',
#    line=Line(color='purple')
#    )
fig = FF.create_candlestick(open_data, high_data, low_data, close_data, dates=dates)
fig['layout'].update({
    'title': name_stock,
    'yaxis': {'title': 'Price'},
    'xaxis': {'title': 'Dates'}
})
fig['data'].extend([add_sma])
fig['data'].extend([add_ema15])
fig['data'].extend([add_ema50])
plot_url = py.plot(fig, filename='candlestick', validate=False)

data = [
    go.Scatter(
        x=dates,
        y=values_data
    )
]

plot_url = py.plot(data, filename='python-datetime')
