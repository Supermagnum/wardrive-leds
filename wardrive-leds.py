import RPi.GPIO as GPIO
import os
import subprocess
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(4, GPIO.OUT)#LED KISMET.
GPIO.setup(17, GPIO.OUT)#LED GPSD running.
#Makes sure all LED's are at the same state initially (off):
GPIO.output(4, True)
GPIO.output(17, True)
while 1 < 2:
        kismet = subprocess.Popen(['ps -ef | grep kismet_server'])#checks if kismet_server is running.
        stdout = subprocess.PIPE, shell=True() #Assigns the output from the grep to the kismet variable
        (output, error) = kismet.communicate()
        if 'kismet_server' in output: GPIO.output(4, False) #Turn on KISMET LED
else:
        GPIO.output(4, True) #Turn off KISMET LED
        gps = subprocess.Popen(['ps -ef | grep gpsd'],
        stdout = subprocess.PIPE, shell=True)#Assigns the output from the grep to the gps variable
        (output, error) = gps.communicate()
        if 'gpsd -F /var/run/gpsd.sock' in output: GPIO.output(17, False) #Turn on GPSD LED
        else:
              GPIO.output(17, True) #Turn off GPSD LED 
