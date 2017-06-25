from random import randint
import sqlite3
import serial

def getconn():
    return sqlite3.connect('/var/www/html/readings.db')

def read():
    
    ser = serial.Serial('/dev/ttyUSB0',9600)
    readings = []
    while len(readings) < 50:
        try:
            r = float(ser.readline())
            readings.append(r)
        except:
            n = True
    tot = 0
    for reading in readings:
        tot += reading

    avg = tot / len(readings)
    f = open("/var/www/html/current", "w")
    f.write(str(avg*0.240))
    return avg * 0.240

def makedb():
    #print("makin")
    conn = getconn()
    c = conn.cursor()
    
    c.execute('''CREATE TABLE readings (date DATETIME, reading REAL)''')

    conn.commit()
    conn.close()

def store(reading):
    
    conn = getconn()
    c = conn.cursor()
    
    c.execute("INSERT INTO readings VALUES (datetime(),"+str(reading)+")")
    
    conn.commit()
    conn.close()

reading = read()

try:
    open("/var/www/html/readings.db")
    store(reading)
except:
    makedb()
    store(reading)
