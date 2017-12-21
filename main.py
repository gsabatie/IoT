#! /usr/bin/python2.7

import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import threading

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)

def RCtime (RCpin):
    reading = 0
    GPIO.setup(RCpin, GPIO.OUT)
    GPIO.output(RCpin, GPIO.LOW)
    time.sleep(0.1)

    GPIO.setup(RCpin, GPIO.IN)
    while (GPIO.input(RCpin) == GPIO.LOW):
        reading += 1
    return reading  / 1000

def readTempHum():
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 22)
        if humidity is not None and temperature is not None:
            print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))

class LumiThread(threading.Thread):
    def run(self):
        while True:
            print("Lumi={}".format(RCtime(6)))

class TempHumThread(threading.Thread):
    def run(self):
        readTempHum()
        
    
if __name__ == '__main__':
    t = TempHumThread()
    t.start()
    time.sleep(0.5)
    l = LumiThread()
    l.start()
