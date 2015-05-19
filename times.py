import datetime
import serial

def add_zeroes(val):
	newval = str(val) if val >= 10 else "0"+str(val)
	return newval 


#connect to serial port
ser = serial.Serial('/dev/ttyACM0', 57600)

t = datetime.datetime.now()
dayofweek = 3

year = str(t.year)[2::]
month = add_zeroes(t.month)
day = add_zeroes(t.day)
hour = add_zeroes(t.hour)
minute = add_zeroes(t.minute)
sec = add_zeroes(t.second)

print t
print year 
print month 
print day
print hour 
print minute
print sec

cmdstr = "T"
cmdstr += str(sec)
cmdstr += str(minute)
cmdstr += str(hour)
cmdstr += str(dayofweek)
cmdstr += str(day)
cmdstr += str(month)
cmdstr += str(year)

ser.write(cmdstr)
print cmdstr
