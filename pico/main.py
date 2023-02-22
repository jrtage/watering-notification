from machine import Pin
import network
import urequests as requests
import time
from secrets import secrets

led = Pin('LED', Pin.OUT)
sensor = Pin(4, Pin.IN, Pin.PULL_DOWN)

ssid = 'WIFI SSID'
password = 'WIFI PASSWORD'

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(secrets['ssid'], secrets['password'])

while wifi.isconnected() == False:
    led.on()
    time.sleep(0.5)
    led.off()
    time.sleep(0.5)

led.on()
print('Connected to Wi-Fi network')
time.sleep(5)
led.off()

while True:
    if sensor.value() == False:
        request = requests.get(secrets['url'])
        request.close()
        while sensor.value == False:
            pass
