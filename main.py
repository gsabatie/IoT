#! /usr/bin/python2.7

# Hardware related #
import RPi.GPIO as GPIO #GPIO lib
import Adafruit_DHT #temp and humidity sensor lib

# broker related #
import paho.mqtt.client as mqtt #mqtt client lib

# python related #
import time #time lib
import threading # thread lib
import signal # signal lib
import sys # sys lib

# setting RPI to use GPIO #
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)

# Leds pins
redLed = 14
whiteLed = 15
greenLed = 18
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

# mqtt client
client = mqtt.Client()

# signal handler for sigint
def signal_handler(signal, frame):
    client.disconnect()
    client.loop_stop(force=True)
    sys.exit(0)

# Read light
def readLumi(RCpin):
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
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 22)
    client.publish("IoT/humidity", humidity)
    client.publish("IoT/temperature", temperature)

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    if msg.topic == "IoT/redLed":
        if msg.payload == "1" and GPIO.input(redLed) is GPIO.LOW:
            let_the_sun_shine(redLed)
        elif msg.payload == "0" and GPIO.input(redLed) is GPIO.HIGH:
            hello_darkness_my_old_friend(redLed)
    if msg.topic == "IoT/whiteLed":
        if msg.payload == "1" and GPIO.input(whiteLed) is GPIO.LOW:
            let_the_sun_shine(whiteLed)
        elif msg.payload == "0" and GPIO.input(whiteLed) is GPIO.HIGH:
            hello_darkness_my_old_friend(whiteLed)
    if msg.topic == "IoT/greenLed":
        if msg.payload == "1" and GPIO.input(greenLed) is GPIO.LOW:
            let_the_sun_shine(greenLed)
        elif msg.payload == "0" and GPIO.input(greenLed) is GPIO.HIGH:
            hello_darkness_my_old_friend(greenLed)
    print(msg.topic+" "+str(msg.payload))


# Takes a pin as parameter and sets the state to HIGH. Used to light on leds
# lol. fun name.
def let_the_sun_shine(pin):
    if GPIO.input(pin) is GPIO.LOW:
        GPIO.output(pin, GPIO.HIGH)


# Takes a pin as parameter and sets the state to LOW if needed. Used to light off leds
# lol. such fun, much name, wow
def hello_darkness_my_old_friend(pin):
    if GPIO.input(pin) is GPIO.HIGH:
        GPIO.output(pin, GPIO.LOW)

# main
if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("192.168.43.83", 1883, 60)
    client.subscribe("IoT/whiteLed")
    client.subscribe("IoT/redLed")
    client.subscribe("IoT/greenLed")
    client.loop_start()
    while True:
        readLumi(6)
        readTempHum()

