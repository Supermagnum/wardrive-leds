#This script controlls a LED connected to the GPIO header,and lights it up if gpsd and kismet is running.
#kismet must be started automatic on boot with the command kismet_server --daemonize
import RPi.GPIO as GPIO
import os
import subprocess
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(04, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
#Makes sure all LED's are at the same state initially (off):
GPIO.output(04, False)
GPIO.output(17, False)
while 1 == 1:
        gps = subprocess.Popen(['ps -ef | grep gpsd'],
        stdout = subprocess.PIPE, shell=True) #Assigns the output from the grep to the gps variable
        (output, error) = gps.communicate()
        if 'gpsd -F /var/run/gpsd.sock' in output: GPIO.output(17, True) #Turn on GPSD LED
        else:
                GPIO.output(17, False) #Turn off GPSD LED
while 1 == 1:
        kismet = subprocess.Popen(['ps -ef | grep gpsd'],
        stdout = subprocess.PIPE, shell=True) #Assigns the output from the grep to the kismet variable
        (output, error) =kismet.communicate()
        if 'kismet_server --daemonize' in output: GPIO.output(04,True)
        else:
                GPIO.output(04, False)
#todo: implement automatic upload of logfiles to wigle.net,if a switch is toggled, password and username set in script or a separate file.
#implement GPS locked LED
#wigle.net upload in progress LED
#Please feel free to contribute to this script
