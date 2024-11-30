#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
import subprocess

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
pwm = GPIO.PWM(14,100)

#print("\nPress Ctrl+C to quit \n")
dc = 0
pwm.start(dc)

try:
    while True:
        temp = round((float(subprocess.getoutput("cat /sys/class/thermal/thermal_zone*/temp")) / 1000))
        if round(float(temp)) >= 45:
            dc = 100
            pwm.ChangeDutyCycle(dc)
            #print("CPU Temp:",float(temp)," Fan duty cycle:",dc)
            time.sleep(5.0)
        if 45 > round(float(temp)) >= 40:
            dc = 85
            pwm.ChangeDutyCycle(dc)
            #print("CPU Temp:",float(temp)," Fan duty cycle:",dc)
            time.sleep(5.0)
        if 40 > round(float(temp)) >= 38:
            dc = 70
            pwm.ChangeDutyCycle(dc)
            #print("CPU Temp:",float(temp)," Fan duty cycle:",dc)
            time.sleep(5.0)
        if 38 > round(float(temp)) >= 30:
            dc = 50
            pwm.ChangeDutyCycle(dc)
            #print("CPU Temp:",float(temp)," Fan duty cycle:",dc)
            time.sleep(5.0)
        elif 30 > round(float(temp)) >= 0:
            dc = 00
            pwm.ChangeDutyCycle(dc)
            #print("CPU Temp:",float(temp)," Fan duty cycle:",dc)
            time.sleep(5.0)

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
    #print("Ctrl + C pressed -- Ending program")
