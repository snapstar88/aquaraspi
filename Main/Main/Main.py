import serial
import time
import math

s = serial.Serial('/dev/ttyUSB0', 9600) # Namen ggf. anpassen
s.isOpen()
time.sleep(5) # der Arduino resettet nach einer Seriellen Verbindung, daher muss kurz gewartet werden

s.write("test")



try:
    while True:
        timte.sleep(2);
        response = s.readline()
        #response = "47_22_22"
        
           
        
        responselist = response.split("_");
        
        humi = responselist[0];
        ihumi = int(humi);
        rtemp = responselist[1];
        irtemp = int(rtemp);
        wtemp = responselist[2];
        iwtemp = int(wtemp);
        

        if ihumi >= 90:
                    print("Zimmer zu feucht")
        else:
                    print("ok")

        if irtemp >= 23:
                    print("Zimmer zu warm")
        else:
                    print("ok")
        if iwtemp >= 25:
                    print("Wasser zu warm")
        else:
                    print("ok")

except KeyboardInterrupt:
        #print("nix")
        s.close()