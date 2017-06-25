import serial

ser = serial.Serial('/dev/ttyUSB0',9600)
readings = []
while len(readings) < 5:
	try:
		r = float(ser.readline())
		readings.append(r)
	except:
		n = True
tot = 0
for reading in readings:
	tot += reading

avg = tot / len(readings)
print(avg)

