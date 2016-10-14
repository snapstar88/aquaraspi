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

        if humi >= 70:
                    print 'Warnung!!! Zimmer zu feucht. ', humi, ' %'
        else:
                    print 'Zimmefeuchtigkeit OK ', humi, ' %'

        if rtemp >= 23:
                    print 'Warnung!!! Zimmer zu warm. ', rtemp,' C'
        else:
                    print 'Zimmertemperatur OK ', rtemp,' C'
        
        if wtemp >= 27:
                    print 'Warnung!!! Wasser zu warm.', wtemp, ' C'        
        else:
                    print 'Wassertemperatur OK ', wtemp, 'C'

except KeyboardInterrupt:
        #print("nix")
        s.close()
      
        
               


         
        

    
        
   


