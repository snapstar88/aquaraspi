

import time
import math

import serial
s = serial.Serial('/dev/ttyUSB0', 9600) # Namen ggf. anpassen
s.isOpen()
time.sleep(5) # der Arduino resettet nach einer Seriellen Verbindung, daher muss kurz gewartet werden
s.write("test")



try:
    while True:
        time.sleep(1);
        response = s.readline()
        #response = "47_40_40"



        responselist = response.split("_");


        humi = int(responselist[0]);
        rtemp = int(responselist[1]);
        wtemp = int(responselist[2]);
        


        if humi >= 90:
                    print 'ACHTUNG!!!! Zimmer zu feucht! Feuchtigkeit = ', humi,'%'
        else:
                    print 'Zimmerfeuchtigkeit OK = ',humi ,'%'

        if rtemp >= 23:
                    print 'ACHTUNG!!!! Zimmer zu warm. Temperatur = ',rtemp,'Grad'
        else:
                    print 'Zimmertemperatur OK = ',rtemp, 'Grad'
        if wtemp >= 25:
                    print 'AUCHTUNG!!!! Wasser zu warm. Temperatur = ',wtemp,'Grad'
        else:
                    print 'Wassertemperatur OK = ',wtemp,'Grad'

except KeyboardInterrupt:
        print("nix")
        s.close()
