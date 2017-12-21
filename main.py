#! /usr/bin/python2.7

# Hardware related #
import RPi.GPIO as GPIO #GPIO lib
import Adafruit_DHT #temp and humidity sensor lib

# broker related #
import paho.mqtt.client as mqtt #mqtt client lib

# python related #
import time #time lib
import threading # thread lib

# setting RPI to use GPIO #
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)


client = mqtt.client() # mqtt client

# Read light
def RCtime (RCpin):
    reading = 0
    GPIO.setup(RCpin, GPIO.OUT)
    GPIO.output(RCpin, GPIO.LOW)
    time.sleep(0.1)

    GPIO.setup(RCpin, GPIO.IN)
    while (GPIO.input(RCpin) == GPIO.LOW):
        reading += 1
    client.publish("IoT/light", reading/1000)
    return reading  / 1000

# Read temperature and humidity
def readTempHum():
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 22)
        client.publish("IoT/humidity", humidity)
        client.publish("IoT/temperature", temperature)
        print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))

# light Thread
class LumiThread(threading.Thread):
    def run(self):
        while True:
            print("Lumi={}".format(RCtime(6)))

# temp and humidity thread
class TempHumThread(threading.Thread):
    def run(self):
        readTempHum()
        
#----------------#

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

#---------------#

# main
if __name__ == '__main__':
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("192.168.43.83", 1883, 60)
    t = TempHumThread()
    l = LumiThread()
    t.start()
    time.sleep(0.5)
    l.start()
    client.loop_forever()
