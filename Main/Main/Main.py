

import time
import math

import serial
s = serial.Serial('/dev/ttyUSB0', 9600) # Namen ggf. anpassen
s.isOpen()
time.sleep(5) # der Arduino resettet nach einer Seriellen Verbindung, daher muss kurz gewartet werden
s.write("test")



try:
    while True:

        response = s.readline()
        #response = "47_22_22"



        responselist = response.split("_");


        humi = int(responselist[0]);
        rtemp = int(responselist[1]);
        wtemp = int(responselist[2]);
        


        if humi >= 90:
                    print("ACHTUNG!!!! Zimmer zu feucht! Feuchtigkeit = ",humi)
        else:
                    print("Zimmer OK. Feuchtigkeit = ", humi)

        if rtemp >= 23:
                    print("ACHTUNG!!!! Zimmer zu warm. Temperatur = ", rtemp)
        else:
                    print("Zimmer OK. Temperatur = ", rtemp)
        if wtemp >= 25:
                    print("AUCHTUNG!!!! Wasser zu warm. Temperatur = ", wtemp)
        else:
                    print("Wasser OK. Temperatur = ", wtemp)

except KeyboardInterrupt:
        print("nix")
        s.close()
