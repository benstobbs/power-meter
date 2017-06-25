import plotly.plotly as py
import plotly.graph_objs as go
import sys
import sqlite3
import time
from datetime import datetime, timedelta
import os

def getconn():
    return sqlite3.connect('/var/www/html/readings.db')

def collatehour():
    conn = getconn()
    c = conn.cursor()
    
    c.execute("SELECT * FROM readings WHERE date >=datetime('now', '-1 Hour')")
        
    res = c.fetchall()
    conn.close()
    
    os.remove('/var/www/html/readings.db')
    
    return res

try:
    open("/var/www/html/readings.db")
    data = collatehour()
except:
    sys.exit()
    
avg = 0
for d in data:
    avg += d[1]
kwh = avg / len(data)
lasth = int(str(data[-1][0])[11:13])
today = "/var/www/html/data/" + time.strftime("%Y%m%d")
try:
    open(today)
    f = open(today, "a")
except:
    open(today, "w")
    f = open(today, "a")

f.write(str(kwh)+"\n")

with open(today) as f:
    content = f.readlines()
    
content = [x.strip() for x in content] 
content = [float(x) for x in content]
final = []

if len(content) < 23:
    yesterday = "/var/www/html/data/" + datetime.strftime(datetime.now() - timedelta(1), '%Y%m%d')
    
    try:
        open(yesterday, "r")
    except:
        yest = open(yesterday, "w")
        for i in range(0, 24):
            yest.write("0\n")
    
    with open(yesterday) as y:
        yes = y.readlines()
    yes = [x.strip() for x in yes]
    yes = [float(x) for x in yes]
    

    for i in range(len(content), len(yes)):
        final.append(yes[i])
for c in content:
    final.append(c)
    
#writeout daily ussage
sig = 0
for f in final:
    sig += f
f = open("/var/www/html/lastday", "w")
f.write(str(sig))

py.sign_in('USERNAME', 'APIKEY')
nos = []
#print(lasth)
for i in range(lasth, lasth-24, -1):
    if i >= 0:
        nos.append(str(i)+"h")
    else:
        nos.append(str(24+i)+"h")
        
nos = nos[::-1]

data = [go.Bar(
            x=nos,
            y=final
    )]

py.plot(data, filename='twentyfour-hour')