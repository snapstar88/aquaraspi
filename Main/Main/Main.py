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
        #response = "47_22_22"
        
           
        
        responselist = response.split("_");
        
        
        humi = int(responselist[0]);
        ihumi = int(humi);
        rtemp = responselist[1];
        irtemp = int(rtemp);
        wtemp = responselist[2];
        iwtemp = int(wtemp);
        

        if ihumi >= 90:
                    print("ACHTUNG!!!! Zimmer zu feucht! Feuchtigkeit = " + humi)
        else:
                    print("Zimmer OK. Feuchtigkeit = " + ihumi)

        if irtemp >= 23:
                    print("ACHTUNG!!!! Zimmer zu warm. Temperatur = " + irtemp)
        else:
                    print("Zimmer OK. Temperatur = " + irtemp)
        if iwtemp >= 25:
                    print("AUCHTUNG!!!! Wasser zu warm. Temperatur = " + iwtemp)
        else:
                    print("Wasser OK. Temperatur = " + iwtemp)

except KeyboardInterrupt:
        #print("nix")
        s.close()
        
      
        
               


         
        

    
        
   






