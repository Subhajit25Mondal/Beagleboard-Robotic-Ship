import Adafruit_BBIO.GPIO as GPIO
import time
import os

Front_UltraTrig = "P9_15"
Front_UltraEcho = "P9_12"
Down_UltraTrig = "P9_11"
Down_UltraEcho = "P9_13"
led_R = "P8_8"

def distanceMeasurement(TRIG,ECHO):
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    pulseStart = time.time()
    
    while GPIO.input(ECHO) == 0:
        pulseStart = time.time()
    while GPIO.input(ECHO) == 1:
        pulseEnd = time.time()

    pulseDuration = pulseEnd - pulseStart
    distance = pulseDuration * 17150
    distance = round(distance, 2)
    return distance 

GPIO.setup(Front_UltraTrig, GPIO.OUT)
GPIO.setup(Front_UltraEcho, GPIO.IN)
GPIO.setup(Down_UltraTrig, GPIO.OUT)
GPIO.setup(Down_UltraEcho, GPIO.IN)
GPIO.setup(led_R, GPIO.OUT)
GPIO.output(Front_UltraTrig, False)
GPIO.output(Down_UltraTrig, False)
time.sleep(0.5)
try:
   while True:
     
      down_Dist = distanceMeasurement(Down_UltraTrig, Down_UltraEcho)
      print "Distance of obstacle Below: %.1f " % down_Dist
      time.sleep(0.3)      
      front_Dist= distanceMeasurement(Front_UltraTrig, Front_UltraEcho)
      print "Distance of Obstacle Ahead : %.1f  " % front_Dist
      time.sleep(0.3)
      os.system('clear')

      if (front_Dist <= 25):
        print " STOP "
        if (down_Dist < 25):
           GPIO.output(led_R, True)
        else:
           GPIO.output(led_R, False)
      else:
        print " GO "
        if (down_Dist < 25):
           GPIO.output(led_R, True)
        else:
           GPIO.output(led_R, False)  
except KeyboardInterrupt:
   print "\nMeasurement Stopped by user "
   GPIO.cleanup()         

