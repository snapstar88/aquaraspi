import serial
import time

s = serial.Serial('/dev/ttyUSB0', 9600) # Namen ggf. anpassen
s.isOpen()
time.sleep(5) # der Arduino resettet nach einer Seriellen Verbindung, daher muss kurz gewartet werden

s.write("test")
wasser = "wasser";

try:
    while True:
        response = s.readline()
        print(response)
    
        print find.wasser(wasser)


except KeyboardInterrupt:
    s.close()



