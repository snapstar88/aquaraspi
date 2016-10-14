import serial
import time
import math

s = serial.Serial('/dev/ttyUSB0', 9600) # Namen ggf. anpassen
s.isOpen()
time.sleep(5) # der Arduino resettet nach einer Seriellen Verbindung, daher muss kurz gewartet werden

s.write("test")



try:
    while True:
        
        response = s.readline()
        #response = "91_23_26"
        
           
        
        responselist = response.split("_");
        
        humi = responselist[0];
        ihumi = int(humi);
        humi = round(ihumi)
        rtemp = responselist[1];
        irtemp = int(rtemp);
        rtemp = round(irtemp)
        wtemp = responselist[2];
        iwtemp = int(wtemp);
        wtemp = round(iwtemp);

        if humi >= 90:
                    print("Zimmer zu feucht")
        else:
                    print("ok")

        if rtemp >= 23:
                    print("Zimmer zu warm")
        else:
                    print("ok")
        if wtemp >= 25:
                    print("Wasser zu warm")
        else:
                    print("ok")

except KeyboardInterrupt:
        #print("nix")
        s.close()
        
      
        
               


         
        

    
        
   






